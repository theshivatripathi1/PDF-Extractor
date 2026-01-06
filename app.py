import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="PDF Q&A", layout="centered")
st.title("📄 PDF Document Q&A")

# STEP 1: Upload PDF
st.header("Step 1: Upload PDF")

uploaded_file = st.file_uploader("Upload a text-based PDF", type=["pdf"])

if uploaded_file:
    response = requests.post(
        f"{BACKEND_URL}/upload-pdf",
        files={"file": uploaded_file}
    )

    if response.status_code == 200:
        st.success("PDF processed successfully!")
    else:
        st.error(response.json().get("detail", "Upload failed"))

st.divider()

# STEP 2: Ask Question
st.header("Step 2: Ask Question")

question = st.text_input("Enter your question")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question")
    else:
        response = requests.post(
            f"{BACKEND_URL}/ask-question",
            json={"question": question}
        )

        if response.status_code == 200:
            st.subheader("Answer")
            st.write(response.json()["answer"])
        else:
            st.error(response.json().get("detail", "Backend error"))
