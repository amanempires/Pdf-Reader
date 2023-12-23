import streamlit as st
import openai
import fitz  # PyMuPDF for PDF extraction
import os
from openai import OpenAI

# Set up OpenAI API key
openai.api_key = "Put your API Key"

def extract_text_from_pdf(pdf_file):
    try:
        # Check if the provided file is a PDF
        if not pdf_file.name.lower().endswith('.pdf'):
            st.error("Please upload a valid PDF file.")
            return ""

        # Save the PDF file temporarily
        with open("temp_pdf_file.pdf", "wb") as temp_file:
            temp_file.write(pdf_file.read())

        pdf_document = fitz.open("temp_pdf_file.pdf")
        text = ""
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text += page.get_text()

        # Close the PDF document
        pdf_document.close()

        # Remove the temporary file
        os.remove("temp_pdf_file.pdf")

        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
        return ""

def get_answer(question, pdf_content):
    # Combine context and question
    prompt = f"Context: {pdf_content}\n\nQuestion: {question}"

    try:
        # Use OpenAI API for text completion
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=150
        )

        return response['choices'][0]['text'].strip()
    except Exception as e:
        st.error(f"Error getting answer from OpenAI: {e}")
        return ""

def display_pdf_content(pdf_content):
    # Display PDF content with Markdown
    st.markdown(f"```{pdf_content}```", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="PDF Reader with Q&A (API)")
    st.title("ASK anything from Your PDF 💭!")

    pdf = st.file_uploader("Insert Your PDF File", type="pdf")

    if pdf is not None:
        pdf_content = extract_text_from_pdf(pdf)

        """st.header("PDF Content:")
        display_pdf_content(pdf_content)
"""
        st.header("Ask Question:")
        que = st.text_input("Type your question here:")

        if st.button("Ask"):
            if que:
                answer = get_answer(que, pdf_content)
                st.header("Answer:")
                st.write(answer)
            else:
                st.warning("Please type your question.")

if __name__ == "__main__":
    main()
