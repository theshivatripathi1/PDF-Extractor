# PDF Document Q&A System (Gemini Flash)

## Features
- Upload text-based PDF
- Convert PDF → JSON automatically
- Ask questions from document
- Gemini Flash API (Free / Fast)
- Streamlit UI + FastAPI backend

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Start Backend
cd backend
uvicorn main:app --reload

### 3. Start Frontend
cd frontend
streamlit run app.py

## Notes
- Only TEXT PDFs supported
- No scanned/image PDFs
- API key stored securely in .env
