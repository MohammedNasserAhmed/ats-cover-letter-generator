from io import BytesIO
from unittest.mock import patch

import pytest
from PIL import Image

from ats_cover_letter_generator.app import (
    create_pdf_cover_letter,
    extract_job_description_from_url,
    extract_text_from_pdf,
    generate_cover_letter,
    generate_signature,
)


@pytest.fixture
def mock_pdf_file():
    pdf_content = b"%PDF-1.4\n%..."
    return BytesIO(pdf_content)


@pytest.fixture
def mock_image_file():
    img = Image.new("RGB", (100, 100), color=(255, 255, 255))
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    return img_bytes


def test_extract_text_from_pdf(mock_pdf_file):
    with patch("fitz.open") as mock_fitz_open:
        mock_doc = mock_fitz_open.return_value.__enter__.return_value
        mock_page = mock_doc.load_page.return_value
        mock_page.get_text.return_value = "Sample text from PDF"
        text = extract_text_from_pdf(mock_pdf_file)
        assert text == "Sample text from PDF"


def test_extract_job_description_from_url():
    url = "http://example.com/job"
    html_content = "<html><body><p>Job description here</p></body></html>"
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = html_content
        job_description = extract_job_description_from_url(url)
        assert job_description == "Job description here"


def test_generate_signature():
    name = "John Doe"
    signature_image = generate_signature(name)
    assert isinstance(signature_image, bytes)


def test_generate_cover_letter():
    resume_text = "Sample resume text"
    job_description = "Sample job description"
    with patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "choices": [{"message": {"content": "Generated cover letter"}}]
        }
        cover_letter = generate_cover_letter(resume_text, job_description)
        assert cover_letter == "Generated cover letter"


def test_create_pdf_cover_letter(mock_image_file):
    cover_letter_text = "Dear Hiring Manager,\n\nThis is a sample cover letter."
    signature_image = mock_image_file.read()
    pdf_bytes = create_pdf_cover_letter(cover_letter_text, signature_image)
    assert isinstance(pdf_bytes, bytes)
    assert pdf_bytes.startswith(b"%PDF")
