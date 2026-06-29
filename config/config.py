import os

from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st

    GEMINI_API_KEY = st.secrets.get(
        "GEMINI_API_KEY",
        os.getenv("GEMINI_API_KEY")
    )

    SERPER_API_KEY = st.secrets.get(
        "SERPER_API_KEY",
        os.getenv("SERPER_API_KEY")
    )

except Exception:

    GEMINI_API_KEY = os.getenv(
        "GEMINI_API_KEY"
    )

    SERPER_API_KEY = os.getenv(
        "SERPER_API_KEY"
    )


MODEL_NAME = "gemini-2.5-flash"

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K = 4

DOCUMENT_FOLDER = "documents"

CHROMA_DB_PATH = "chroma_db"
