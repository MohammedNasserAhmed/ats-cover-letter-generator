### **📝 ATS Cover Letter Generator**  
**An AI-powered ATS-optimized cover letter generator leveraging LLaMA-3.1-8B-Instant via Groq's API.**  

![GitHub stars](https://img.shields.io/github/stars/MohammedNasserAhmed/ats-cover-letter-generator?style=social)  
![GitHub license](https://img.shields.io/github/license/MohammedNasserAhmed/ats-cover-letter-generator) <img src="https://img.shields.io/badge/Python-3.12-blue" alt="Python version"> <img src="https://img.shields.io/badge/Streamlit-1.26.0-red" alt="Streamlit">

---

## **✨ Key Features**  

✅ **Resume/CV Parsing** – Extracts text from uploaded PDFs  
✅ **Job Description Input** – Paste job details or fetch via URL  
✅ **AI-Powered Matching** – LLaMA-3.1-8B-Instant tailors cover letters dynamically  
✅ **ATS Optimization** – Ensures compliance with hiring algorithms  
✅ **Side-by-Side Review** – Compare your resume with the job description  
✅ **Professional PDF Output** – Generates a polished, ready-to-submit cover letter  
✅ **Signature Generation** – Auto-generates a digital signature  
✅ **Cloud-Ready Deployment** – Compatible with Streamlit Cloud & Hugging Face Spaces  

---

## **🚀 Installation & Setup**  

### **🔹 Prerequisites**  
- Python **3.8+** (Recommended: 3.12)  
- Groq API Key ([Get one here](https://console.groq.com/))  

### **🔹 Local Setup**  

1⃣ **Clone the repository:**  
   ```bash
   git clone https://github.com/MohammedNasserAhmed/ats-cover-letter-generator.git
   cd ats-cover-letter-generator
   ```

2⃣ **Create & activate a virtual environment:**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3⃣ **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

4⃣ **Set up environment variables:**  
   Create a `.env` file and add your API key:  
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5⃣ **Run the application:**  
   ```bash
   streamlit run src/ats_cover_letter_generator/app.py
   ```

6⃣ **Access the app** at [`http://localhost:8501`](http://localhost:8501)  

---

## **🌐 Deployment Options**  

### **1⃣ Deploy on Streamlit Cloud**  
1. Push your code to a **public GitHub repository**  
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud)  
3. Create a new app & select your repository  
4. **Add API secrets** under **"Secrets Management"**  
5. Click **Deploy** 🎉  

---

### **2⃣ Deploy on Hugging Face Spaces**  
1. Create a Hugging Face account  
2. Create a new **Space** (select **Streamlit SDK**)  
3. Upload your app files  
4. Add `GROQ_API_KEY` in **Settings → Secrets**  
5. Deploy 🚀  

---

### **3⃣ Run on a Local Server**  
To keep it running in the background:  
```bash
nohup streamlit run src/ats_cover_letter_generator/app.py --server.port 8501 &
```

---

## **⚙️ Customization**  

🔹 **AI Creativity Control** – Adjust temperature in the sidebar  
🔹 **Template Customization** – Modify PDF styling in `create_pdf_cover_letter()`  
🔹 **Prompt Engineering** – Tweak `generate_cover_letter()` for different outputs  

---

## **🤝 Contributing**  
💡 **Contributions are welcome!** If you find a bug or have an idea for improvement:  
1. **Fork the repository**  
2. **Create a new branch** (`feature-xyz`)  
3. **Submit a Pull Request (PR)**  

---

## **📝 License**  
**MIT License** – Free to use & modify. See `LICENSE` for details.  

---

### **📩 Contact & Support**  
🔗 **GitHub Issues** – Report bugs or feature requests [here](https://github.com/MohammedNasserAhmed/ats-cover-letter-generator/issues)  
📝 **Email** – [abunasserip@gmail.com](mailto:abunasserip@gmail.com)  

---

🚀 **Empower your job applications with AI. Build ATS-optimized cover letters in seconds!**
