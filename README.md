# **📝 ATS Cover Letter Generator**  
**An AI-powered ATS-optimized cover letter generator leveraging LLaMA-3.1-8B-Instant via Groq's API.**  

![GitHub stars](https://img.shields.io/github/stars/MohammedNasserAhmed/ats-cover-letter-generator?style=social)  
![GitHub license](https://img.shields.io/github/license/MohammedNasserAhmed/ats-cover-letter-generator) <img src="https://img.shields.io/badge/Python-3.12-blue" alt="Python version"> <img src="https://img.shields.io/badge/Streamlit-1.26.0-red" alt="Streamlit"> ![Docker](https://img.shields.io/badge/Docker-Supported-blue?logo=docker) 

---

## **🌟 Overview**

The **ATS Cover Letter Generator** bridges the gap between job seekers and employers by leveraging AI to create perfectly tailored, Applicant Tracking System (ATS) optimized cover letters. Using Groq's high-performance LLaMA-3.1-8B-Instant API, the application analyzes your resume and job descriptions to craft compelling cover letters that increase your chances of interview selection.

## **✨ Key Features**

| Feature | Description |
|---------|-------------|
| 📄 **Resume/CV Parsing** | Extracts text from uploaded PDFs automatically |
| 🔍 **Job Description Analysis** | Paste job details directly or fetch via URL |
| 🧠 **AI-Powered Matching** | LLaMA-3.1-8B-Instant tailors content to highlight relevant skills |
| 🎯 **ATS Optimization** | Strategic keyword placement ensures visibility to hiring algorithms |
| 👁️ **Side-by-Side Review** | Compare your resume with job requirements in real-time |
| 📑 **Professional PDF Output** | Generate polished, ready-to-submit cover letters |
| ✍️ **Digital Signature** | Auto-generates signature for a professional touch |
| ☁️ **Flexible Deployment** | Deploy via Docker, Streamlit Cloud, or Hugging Face Spaces |

## **🚀 Quick Start**

### **Using Docker (Recommended)**

```bash
# Pull the image
docker pull mohammednasserahmed/ats-cover-letter-generator:latest

# Run the container
docker run -d -p 8501:8501 -e GROQ_API_KEY=your_groq_api_key_here mohammednasserahmed/ats-cover-letter-generator
```

### **Local Installation**

```bash
# Clone the repository
git clone https://github.com/MohammedNasserAhmed/ats-cover-letter-generator.git
cd ats-cover-letter-generator

# Create & activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variable
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# Run the application
streamlit run src/ats_cover_letter_generator/app.py
```

Then access the app at [http://localhost:8501](http://localhost:8501)

## **🌐 Deployment Options**

### **🐳 Docker Deployment**

```bash
# Build the Docker image
docker build -t ats-cover-letter-generator .

# Run the container
docker run -p 8501:8501 --env-file .env ats-cover-letter-generator
```

### **☁️ Streamlit Cloud**

1. Fork this repository to your GitHub account
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app & point to your forked repository
4. Set the main file path to `src/ats_cover_letter_generator/app.py`
5. Add your `GROQ_API_KEY` under "Secrets Management"
6. Deploy and share your application

### **🤗 Hugging Face Spaces**

1. Create a Hugging Face account
2. Create a new Space (select Streamlit SDK)
3. Configure the repository settings to point to your GitHub repo
4. Add `GROQ_API_KEY` in Settings → Secrets
5. Deploy and share your Space URL

### **🖥️ Production Server (Background Process)**

```bash
nohup streamlit run src/ats_cover_letter_generator/app.py --server.port 8501 &
```

## **⚙️ Customization & Advanced Usage**

### **Adjusting AI Parameters**

The sidebar provides controls for adjusting the AI's creativity level (temperature):
- **Low (0.1-0.3)**: More conservative, follows templates closely
- **Medium (0.4-0.7)**: Balanced creativity and precision
- **High (0.8-1.0)**: More innovative, varied outputs

### **Modifying Templates**

Edit the PDF template in `src/ats_cover_letter_generator/utils/pdf_generator.py`:

```python
def create_pdf_cover_letter(content, name, signature_image):
    # Customize styling, layout and formatting here
    ...
```

### **Custom Prompts**

Enhance the AI prompting in `src/ats_cover_letter_generator/utils/ai_helpers.py`:

```python
def generate_cover_letter(resume_text, job_description, temp=0.7):
    # Modify the prompt template to adjust tone, style, or focus
    ...
```

## **📊 Performance & Limitations**

- **Processing Time**: ~5-15 seconds depending on input length
- **Token Limits**: Maximum combined resume + job description ~8,000 tokens
- **Best Results**: Achieved with clean, well-structured resumes and detailed job descriptions

## **🤝 Contributing**

Contributions are welcome! Help improve this tool by:

1. Forking the repository
2. Creating a feature branch (`git checkout -b feature/amazing-improvement`)
3. Committing your changes (`git commit -am 'Add amazing improvement'`)
4. Pushing to the branch (`git push origin feature/amazing-improvement`)
5. Opening a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## **🔍 Architecture**

```
ats-cover-letter-generator/
├── .venv/                        # Virtual environment
├── assets/                       # Assets like images and demo GIFs
├── src/
│   └── ats_cover_letter_generator/
│       ├── __init__.py           # Package initialization
│       ├── app.py                # Main Streamlit application
│       ├── test_app.py           # Unit tests for the application
│    
├── Dockerfile                    # Docker configuration
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── .env                          # Environment variables                    # Project documentation
```

## **📝 License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **📩 Contact & Support**

- **GitHub Issues**: [Report bugs or request features](https://github.com/MohammedNasserAhmed/ats-cover-letter-generator/issues)
- **Email**: [abunasserip@gmail.com](mailto:abunasserip@gmail.com)

---

<p align="center">
  <b>Empower your job search with AI-crafted, ATS-optimized cover letters in seconds!</b>
</p>