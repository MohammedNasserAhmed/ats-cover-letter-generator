# Deployment Guide for Smart Cover Letter Generator

This guide provides detailed instructions for deploying the Smart Cover Letter Generator on various platforms.

## Table of Contents
- [Local Development](#local-development)
- [Streamlit Cloud](#streamlit-cloud)
- [Hugging Face Spaces](#hugging-face-spaces)
- [Docker Deployment](#docker-deployment)
- [Troubleshooting](#troubleshooting)

## Local Development

### Setup Development Environment

1. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```

2. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   Open your browser and navigate to `http://localhost:8501`

## Streamlit Cloud

Streamlit Cloud offers a straightforward way to deploy Streamlit apps directly from GitHub repositories.

1. **Prepare your GitHub repository**
   - Push your code to a GitHub repository
   - Ensure the repository includes:
     - `app.py` (main application file)
     - `requirements.txt` (dependencies)
     - `.streamlit` folder (optional, for configuration)

2. **Deploy on Streamlit Cloud**
   - Sign up/in at [Streamlit Cloud](https://streamlit.io/cloud)
   - Click "New app"
   - Select your repository, branch, and `app.py` as the main file
   - Set advanced settings if needed

3. **Configure secrets**
   - Navigate to your app settings
   - Click on "Secrets"
   - Add your API key:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

4. **Access your deployed app**
   - Streamlit Cloud will provide a public URL for your app
   - Share this URL with others who need to use the application

## Hugging Face Spaces

Hugging Face Spaces provides a platform for hosting Streamlit applications with free tier options.

1. **Prepare your repository**
   - Create a new repository on Hugging Face Spaces
   - Choose "Streamlit" as the SDK

2. **Upload files**
   Either:
   - Upload files directly through the web interface, or
   - Clone the repository and push changes:
     ```bash
     git clone https://huggingface.co/spaces/yourusername/your-space-name
     # Add your files
     git add .
     git commit -m "Initial commit"
     git push
     ```

3. **Set up secrets**
   - Go to the Settings tab of your Space
   - Add repository secrets:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

4. **Access your Space**
   - Your app will be available at `https://huggingface.co/spaces/yourusername/your-space-name`

## Docker Deployment

For more control over your deployment environment, you can use Docker.

1. **Create a Dockerfile**
   Create a file named `Dockerfile` in your project root:

   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   COPY . .

   EXPOSE 8501

   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build and run Docker container**
   ```bash
   # Build the Docker image
   docker build -t cover-letter-generator .

   # Run the container
   docker run -p 8501:8501 -e GROQ_API_KEY=your_groq_api_key_here cover-letter-generator
   ```

3. **Access the application**
   Open your browser and navigate to `http://localhost:8501`

## Troubleshooting

### API Key Issues
- Ensure your Groq API key is correctly set in the environment variables or secrets
- Verify the API key is valid by testing with a simple API call

### PDF Generation Problems
- Check that all required fonts are available in the deployment environment
- If using custom fonts, ensure they are included in your repository

### Job URL Scraping Issues
- Some websites may block scraping attempts
- Try providing job descriptions directly in the text area instead

### Performance Optimization
- If the app is slow to load, consider:
  - Reducing the size of any included assets
  - Optimizing API calls with caching
  - Using session state for storing intermediate results

### Dependencies Conflict
- If you encounter dependency conflicts, pin specific versions in `requirements.txt`
- For persistent issues, consider using Docker to ensure consistent environments