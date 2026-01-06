import sys
import os

# Ensure backend directory is on Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel

from pdf_utils import extract_text_from_pdf, convert_text_to_json
from gemini_utils import ask_gemini

app = FastAPI()

DOCUMENT_CONTEXT = ""


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    global DOCUMENT_CONTEXT

    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    text = extract_text_from_pdf(file.file)

    if not text.strip():
        raise HTTPException(status_code=400, detail="No text found in PDF")

    DOCUMENT_CONTEXT = convert_text_to_json(text)["document"]

    return {"message": "PDF processed successfully"}


class QuestionRequest(BaseModel):
    question: str


@app.post("/ask-question")
async def ask_question(req: QuestionRequest):
    if not DOCUMENT_CONTEXT:
        raise HTTPException(status_code=400, detail="Please upload a PDF first")

    answer = ask_gemini(DOCUMENT_CONTEXT, req.question)
    return {"answer": answer}
