import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.pdf_writer import create_summary_pdf
from utils.summarizer import summarize_text

st.set_page_config(page_title="AI PDF Summarizer", layout="wide")

st.title("📑 AI-Powered PDF Summarizer")
st.write("Upload a PDF, and get a detailed summary generated with Groq Llama-3.")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

detail_level = st.selectbox("Select Summary Detail Level", ["short", "medium", "detailed"])

if uploaded_file:
    if st.button("Generate Summary"):
        with st.spinner("Reading and summarizing..."):
            text = extract_text_from_pdf(uploaded_file)
            summary = summarize_text(text, detail_level)

            st.subheader("📄 Summary Output")
            st.write(summary)

            buffer = create_summary_pdf(summary)
            st.download_button(
                label="Download Summary PDF",
                data=buffer,
                file_name="summary.pdf",
                mime="application/pdf"
            )
