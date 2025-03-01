FROM python:3.12-slim

WORKDIR /app



# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libfontconfig1 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN python -m ensurepip && python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expose port for Streamlit
EXPOSE 8501

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Start the application
CMD ["streamlit", "run", "src/ats_cover_letter_generator/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
