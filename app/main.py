
from fastapi import FastAPI
from app import api_router

app = FastAPI(
  title="RAG Personal Assistant API",
  description="An API for answering questions with Retrieval-Augmented Generation.",
  version="1.0.0"
)

app.include_router(api_router.router)


