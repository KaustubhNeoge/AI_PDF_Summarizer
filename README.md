# AI PDF Summarizer

A web app that reads PDFs and generates detailed summaries using AI (Groq API). Built with **Python** and **Streamlit**, this project demonstrates practical use of generative AI for document understanding.

---

## **Features**

- Upload PDF files directly through a web interface.
- Extract text from PDF using Python utilities.
- Generate **detailed summaries** of the content with AI.
- Download the summarized content as a new PDF.
- Clean, modular codebase suitable for learning and portfolio projects.

---

## **Folder Structure**

AI_PDF_Summarizer/
│
├─ ai-pdf-summarizer/
│ ├─ app.py # Streamlit main app
│ ├─ requirements.txt # Python dependencies
│ ├─ .gitignore
│ ├─ .env.example # Placeholder for API key
│ └─ utils/ # Helper modules
│ ├─ pdf_reader.py
│ ├─ pdf_writer.py
│ └─ summarizer.py
