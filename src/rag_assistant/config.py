from pathlib import Path
import os


# 自动获取项目根目录（config.py 的上上级）
PROJECT_ROOT = Path(__file__).resolve().parents[2]
# 数据路径
DATA_DIR = PROJECT_ROOT / "data" / "pdf" / "embedded"

# 向量数据库路径
VECTORDB_DIR = PROJECT_ROOT / "vector_db"
VDB_INDEX_FAISS  = VECTORDB_DIR / "index.faiss"
VDB_INDEX_PKL  = VECTORDB_DIR / "index.pkl"

# 嵌入模型类型: "openai" 或 "huggingface"
EMBEDDING_MODEL_TYPE = "huggingface"

# HuggingFace 模型名（仅当 EMBEDDING_MODEL_TYPE 为 huggingface 时生效）
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# 模型类型: "openai" / "huggingface" / "local"
LLM_TYPE = "openai"

# 本地 GGUF 模型路径
LOCAL_MODEL_FILENAME = "mistral-7b-instruct-v0.1.Q4_K_M.gguf"
LOCAL_MODEL_DIR = PROJECT_ROOT/"models"
LOCAL_MODEL_PATH = LOCAL_MODEL_DIR/LOCAL_MODEL_FILENAME
LLAMA_CPP_N_CTX = 4096
LLAMA_CPP_N_GPU_LAYERS = 0

# OpenAI 设置
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL_NAME = "gpt-4"

# HUGGINGFACE 设置
HUGGINGFACEHUB_API_TOKEN =os.getenv("HUGGINGFACEHUB_API_TOKEN", "")

VERBOSE_MODE = False

LOCAL_MODEL_URL = (
    "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/"
    + LOCAL_MODEL_FILENAME
)