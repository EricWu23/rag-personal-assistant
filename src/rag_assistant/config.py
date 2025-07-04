from pathlib import Path
from dotenv import load_dotenv
import os

# 自动获取项目根目录（config.py 的上上级）
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# 自动加载 .env 文件
load_dotenv()

# 数据路径
DATA_DIR = PROJECT_ROOT / "data" / "pdf" / "embedded"

# 向量数据库路径
VECTORDB_DIR = PROJECT_ROOT / "vector_db"

# 嵌入模型类型: "openai" 或 "huggingface"
EMBEDDING_MODEL_TYPE = "huggingface"

# HuggingFace 模型名（仅当 EMBEDDING_MODEL_TYPE 为 huggingface 时生效）
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# 模型类型: "openai" / "huggingface" / "local"
LLM_TYPE = "openai"

# 本地 GGUF 模型路径
LOCAL_MODEL_PATH = Path("models") / "mistral-7b-instruct-v0.1.Q4_K_M.gguf"

# OpenAI 设置
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL_NAME = "gpt-4"

# HUGGINGFACE 设置
HUGGINGFACEHUB_API_TOKEN =os.getenv("HUGGINGFACEHUB_API_TOKEN", "")