"""
ATS Cover Letter Generator App
This Streamlit application generates ATS-optimized, professional cover letters tailored to specific job applications using AI.
Users can upload their CV, provide the job description, and get a customized cover letter in seconds.
Modules:
- base64: Encoding and decoding of base64 strings.
- os: Miscellaneous operating system interfaces.
- re: Regular expression operations.
- tempfile: Generate temporary files and directories.
- io: Core tools for working with streams.
- pathlib: Object-oriented filesystem paths.
- fitz: PyMuPDF library for PDF processing.
- numpy: Scientific computing with Python.
- requests: HTTP library for making requests.
- streamlit: Framework for creating web apps.
- bs4: BeautifulSoup library for web scraping.
- dotenv: Load environment variables from .env file.
- fpdf: PDF generation library.
- PIL: Python Imaging Library for image processing.
Functions:
- extract_text_from_pdf(pdf_file): Extracts text from a PDF file.
- extract_job_description_from_url(url): Extracts job description text from a given URL.
- generate_signature(name): Generates a signature image from a given name.
- generate_cover_letter(resume_text, job_description): Calls the Groq API to generate a cover letter based on the resume and job description.
- create_pdf_cover_letter(cover_letter_text, signature_image): Converts the generated cover letter to a PDF with an optional signature image.
Usage:
1. Upload your resume (PDF).
2. Provide a job description either by URL or by pasting the text.
3. Adjust AI creativity settings if needed.
4. Generate and download the cover letter as a PDF.
"""

# import base64
import os
import re
import tempfile
from io import BytesIO
from pathlib import Path

import fitz  # PyMuPDF
import numpy as np
import requests
import streamlit as st
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont
from streamlit_pdf_viewer import pdf_viewer

# Load the .env file from the source path
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

# Page configuration
st.set_page_config(
    page_title="ATS Cover Letter Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

# App title and description
st.title("ATS Cover Letter Generator")
st.markdown("""
Generate ATS-optimized, professional cover letters tailored to specific job applications using AI.
Upload your CV, provide the job description, and get a customized cover letter in seconds.
""")

# Sidebar for API configuration
with st.sidebar:
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        st.error("Groq API key is missing! Please check your .env file.")

    st.header("App Information")
    st.info("""
    This app uses:
    - LLaMA-3.1-8B-Instant for content generation
    - PDF processing for document handling
    - ATS optimization techniques
    """)

    st.header("Settings")
    temperature = st.slider("AI Creativity (Temperature)", 0.0, 1.0, 0.4, 0.1)


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file.

    Args:
        pdf_file: A file-like object representing the PDF.

    Returns:
        A string containing the extracted text from the PDF, or None if an error occurs.
    """
    try:
        # Read the PDF file bytes
        pdf_bytes = pdf_file.read()

        # Open the PDF document using PyMuPDF's Document class
        doc = fitz.Document(stream=pdf_bytes, filetype="pdf")
        text = ""
        # Iterate through each page and extract text
        for page in doc:
            text += page.get_text()
        doc.close()  # Explicitly close the document

        return text

    except Exception as e:
        # Display an error message if text extraction fails
        st.error(f"Error extracting text from PDF: {e}")
        return None


# Function to extract content from job URL
def extract_job_description_from_url(url: str) -> str | None:
    """
    Extracts the job description text from a given URL.

    Args:
        url: The URL to extract the job description from.

    Returns:
        The extracted job description text, or None if an error occurs.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        # Strip HTML tags and get text
        job_text = soup.get_text(separator=" ", strip=True)

        # Clean up whitespace
        job_text = re.sub(r"\s+", " ", job_text)

        return job_text
    except Exception as e:
        st.error(f"Error extracting job description from URL: {e}")
        return None


# Function to generate a signature image
def generate_signature(name: str) -> bytes:
    """
    Generates a signature image from a given name.

    Args:
        name: The name to generate the signature for.

    Returns:
        The generated signature image as bytes.
    """
    # Create a blank image with a white background
    img = Image.new("RGB", (400, 200), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    try:
        # Try to use a cursive font
        font = ImageFont.truetype("DejaVuSans.ttf", 36)
    except OSError:
        font = ImageFont.load_default()

    # Generate a signature-like curve
    points = []
    x_offset = 50
    y_baseline = 100

    # Create signature points
    for i, _char in enumerate(name):
        x = x_offset + i * 20
        # Add some randomness to y position for a more natural look
        y = y_baseline + np.sin(i * 0.5) * 10
        points.append((x, y))

    # Draw the signature
    if len(points) > 1:
        d.line(points, fill=(0, 0, 0), width=3)

    # Add the text below
    d.text((x_offset, y_baseline + 30), name, fill=(0, 0, 0), font=font)

    # Convert to bytes
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return buffered.getvalue()


# Function to call Groq API
def generate_cover_letter(resume_text: str, job_description: str) -> str | None:
    """
    Calls the Groq API to generate a cover letter based on the resume and job description.

    Args:
        resume_text (str): The resume text.
        job_description (str): The job description.

    Returns:
        The generated cover letter as a string, or None if an error occurs.
    """
    if not groq_api_key:
        st.error("Please enter your Groq API key in the sidebar.")
        return None

    # Prepare the prompt
    prompt = f"""
    Create a professional, ATS-optimized cover letter based on the following resume and job description.
    
    RESUME:
    {resume_text[:2000]}  # Limiting to 2000 chars to avoid token limits
    
    JOB DESCRIPTION:
    {job_description[:2000]}  # Limiting to 2000 chars to avoid token limits
    
    Instructions:
    1. Create a formal, well-structured cover letter
    2. Match relevant skills and experiences from the resume to the job requirements
    3. Use a professional tone and format
    4. Include a compelling introduction, 2-3 paragraphs for the body, and a confident closing
    5. Make it ATS-friendly by including relevant keywords from the job description
    6. Keep it under 400 words
    7. Format it as a business letter with today's date, addressed to the hiring manager
    
    
    The cover letter should be ready to use without any additional instructions or explanations.
    """

    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {groq_api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": 1024,
        }

        with st.spinner("Generating cover letter..."):
            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 200:
                result = response.json()
                cover_letter = result["choices"][0]["message"]["content"]
                return cover_letter
            else:
                st.error(f"API Error: {response.status_code} - {response.text}")
                return None
    except Exception as e:
        st.error(f"Error calling Groq API: {e}")
        return None


# Function to convert cover letter to PDF
def create_pdf_cover_letter(cover_letter_text, signature_image):
    """
    Converts the generated cover letter into a PDF with an optional signature image.

    Args:
        cover_letter_text (str): The text content of the cover letter.
        signature_image (bytes): The signature image as bytes.

    Returns:
        bytes: The generated PDF as a byte string, or None if an error occurs.
    """
    try:
        # Initialize PDF
        pdf = FPDF()
        pdf.add_page()

        # Set title font
        pdf.set_font("Arial", size=12)

        # Add content with proper line breaks
        pdf.set_font("Arial", size=11)

        # Process cover letter text and wrap lines
        lines = cover_letter_text.split("\n")
        for line in lines:
            if line.strip() == "":
                # Add space for empty lines
                pdf.ln(5)
            else:
                # Add text lines with automatic wrapping
                pdf.multi_cell(0, 5, line)

        # Add space for signature
        pdf.ln(15)

        # Add signature image if provided
        if signature_image:
            # Save signature image to temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
                temp.write(signature_image)
                temp_path = temp.name

            # Add the image with a width of approximately 4 cm
            pdf.image(temp_path, x=pdf.get_x(), y=pdf.get_y(), w=40)

            # Remove temporary file
            os.unlink(temp_path)

        # Get the PDF as bytes
        pdf_bytes = pdf.output(dest="S").encode("latin1")
        return pdf_bytes

    except Exception as e:
        # Display an error message if PDF creation fails
        st.error(f"Error creating PDF: {e}")
        return None


# Main form
with st.form("cover_letter_form"):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Resume Upload")
        resume_file = st.file_uploader("Upload your Resume/CV (PDF)", type=["pdf"])
        signature_file = st.file_uploader(
            "Upload signature image (optional)", type=["png", "jpg", "jpeg"]
        )

    with col2:
        st.subheader("Job Description")
        job_url = st.text_input("Job Posting URL (optional)")
        job_description_input = st.text_area("Or paste the job description here")

    submit_button = st.form_submit_button("Generate Cover Letter")

# Process form submission
if submit_button:
    if not resume_file:
        st.error("Please upload your resume PDF.")
    elif not job_url and not job_description_input:
        st.error("Please provide either a job URL or paste the job description.")
    else:
        # Extract resume text
        resume_text = extract_text_from_pdf(resume_file)

        # Get job description
        job_description = ""
        if job_url:
            job_description = extract_job_description_from_url(job_url)
            if not job_description and not job_description_input:
                st.error(
                    "Could not extract job description from URL. Please paste the job description manually."
                )

        if job_description_input:
            job_description = job_description_input

        if resume_text and job_description:
            # Display inputs side by side
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Your Resume")
                # Display the uploaded resume
                binary_data = resume_file.getvalue()
                pdf_viewer(binary_data, width=700)

                # Create a PDF viewer for the resume
                # base64_resume = base64.b64encode(resume_bytes).decode("utf-8")
                # pdf_viewer = f'<iframe src="data:application/pdf;base64,{base64_resume}" width="100%" height="500" type="application/pdf"></iframe>'
                # st.markdown(pdf_viewer, unsafe_allow_html=True)

                # Still keep text view as an option
                with st.expander("View Resume as Text", expanded=False):
                    st.text_area("Resume Text", resume_text, height=300, disabled=True)

            with col2:
                st.subheader("Job Description")
                with st.expander("View Job Description", expanded=False):
                    st.text_area(
                        "Job Details", job_description, height=300, disabled=True
                    )

            # Generate cover letter
            cover_letter = generate_cover_letter(resume_text, job_description)

            if cover_letter:
                st.success("Cover letter generated successfully!")

                # Display the cover letter
                st.subheader("Your Cover Letter")
                st.write(cover_letter)

                # Handle signature - either uploaded or generated
                signature_bytes = None
                if "signature_file" in locals() and signature_file is not None:
                    signature_bytes = signature_file.getvalue()
                else:
                    # Generate signature as before
                    signature_bytes = ""

                # Create PDF with the signature
                pdf_bytes = create_pdf_cover_letter(cover_letter, signature_bytes)

                if pdf_bytes:
                    # Provide download link
                    st.download_button(
                        label="Download Cover Letter as PDF",
                        data=pdf_bytes,
                        file_name=f"{'cover letter'.replace(' ', '_')}_Cover_Letter.pdf",
                        mime="application/pdf",
                        key="download-pdf",
                    )

                    # Preview PDF
                    pdf_viewer(pdf_bytes, width=700)
                    # base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
                    # display_pdf = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="600" type="application/pdf"></iframe>'
                    # st.markdown(display_pdf, unsafe_allow_html=True)

# Tips and instructions
with st.expander("Tips for Better Results"):
    st.markdown("""
    ### Tips for Better Results
    
    1. **Ensure your resume is up-to-date** and includes relevant skills and experience for the position.
    
    2. **Use a detailed job description** - the more information provided, the better the tailored cover letter.
    
    3. **Adjust the AI Creativity setting** in the sidebar:
       - Lower values (0.1-0.3) produce more formal, conservative letters
       - Higher values (0.6-0.9) produce more unique, creative letters
    
    4. **Review and personalize** the generated cover letter before submitting it to employers.
    
    5. **Always proofread** the final output to ensure it accurately represents your qualifications.
    """)
