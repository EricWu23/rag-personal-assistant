
import os
from dotenv import load_dotenv
# 自动加载 .env 文件
load_dotenv()

from fastapi import FastAPI
from app import api_router
from tqdm import tqdm
from src.rag_assistant.utils import ensure_vector_db_exists,ensure_model_exists

if os.getenv("AUTO_DOWNLOAD_MODEL", "true").lower() == "true":
    ensure_model_exists()
if os.getenv("UPDATE_KNOWLEDGE_BASE","true").lower() == "true":
    from src.rag_assistant.ingest import main as update_db
    update_db()
ensure_vector_db_exists()

app = FastAPI(
  title="RAG Personal Assistant API",
  description="An API for answering questions with Retrieval-Augmented Generation.",
  version="1.0.0"
)

@app.get("/")
def read_root():
  return {"message": "Hello, this is your RAG assistant backend is alive!"}

app.include_router(api_router.router)


