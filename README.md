# 📚 RAG Personal Assistant

A personal Retrieval-Augmented Generation (RAG) system that answers user questions over your own documents using either cloud or local LLMs.  

This project is designed to **demonstrate production-ready patterns** for building an end-to-end RAG pipeline, suitable for personal use, local deployment.

---

## 🚀 Features

✅ Ingest PDF documents into a vector database  
✅ Semantic chunking with metadata (e.g., source path)  
✅ Local or OpenAI Embeddings (configurable)  
✅ FAISS vector store for offline search  
✅ Retrieval + Augmented Generation pipeline  
✅ Supports:
- OpenAI GPT models (fallback)
- Local GGUF LLMs via llama-cpp-python

✅ Modular and configurable project structure  
✅ CLI and notebook demos

---

## ⚙️ Architecture

[ PDF ] --> [ Chunking & Embeddings ] --> [ FAISS Vector Store ]
↘
[ Retrieval ]
↘
[ LLM ]
↘
[ Answer ]

## 🗂️ Project Structure
rag-personal-assistant/
├── models/ # (Put your downloaded GGUF models here)
├── vector_db/ # Local FAISS DB
├── data/ # Your PDFs
├── notebooks/ # Interactive notebooks
└── src/
└── rag_assistant/
├── config.py
├── ingest.py
├── retrieve.py
├── rag_chain.py
├── llm_loader.py
└── utils.py

## 💾 Local Model Support

This project supports local LLM inference using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python). 

**Recommended model:**  
- [TheBloke/Mistral-7B-Instruct-v0.1-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)

✅ Recommended quantization: `Q4_K_M` (suitable for CPU-only inference)

### Download Instructions

1️⃣ Go to [Hugging Face link](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)  
2️⃣ Download `mistral-7b-instruct-v0.1.Q4_K_M.gguf`  
3️⃣ Place it in your local `models/` folder:
rag-personal-assistant/
└── models/
└── mistral-7b-instruct-v0.1.Q4_K_M.gguf

✅ *Note: This model file is large (several GB) and is NOT included in this repo.*

---

## 🧪 Quickstart

1️⃣ Install dependencies:

```bash
pip install -r requirements.txt

2️⃣ Set your .env file:

3️⃣ Ingest your documents:
python -m src.rag_assistant.ingest

4️⃣ Retrieve and answer:
python -m src.rag_assistant.retrieve

5️⃣ Use in notebooks for rapid prototyping!

⚙️ Configuration
All settings are managed in src/rag_assistant/config.py:

* Embedding Model Type (OpenAI vs Local)

* OpenAI model + key

* Local GGUF model path

* FAISS DB path

* Verbose logging

Example:

LLM_TYPE = "local"   # "openai" or "local"
LOCAL_MODEL_PATH = PROJECT_ROOT / "models" / "mistral-7b-instruct-v0.1.Q4_K_M.gguf"

🌐 OpenAI + Local Fallback
✨ This project supports automatic fallback:

Primary: OpenAI GPT (if available)

Fallback: Local GGUF model (if OpenAI is rate-limited / unavailable)

🤖 Why This Project?
This is not "just calling an API" — it demonstrates:

✅ Real retrieval-augmented generation pipeline
✅ Local/offline-friendly architecture
✅ Configurable multi-backend support
✅ Practical engineering for real-world use cases

Perfect for:

Personal assistants

Enterprise knowledge bases

📜 License
Code: MIT License
Content (docs, images): CC-BY-NC 4.0

🙏 Acknowledgements
LangChain

llama-cpp-python

sentence-transformers

FAISS