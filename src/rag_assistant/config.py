from pathlib import Path
# 自动获取项目根目录（config.py 的上上级）
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# 数据路径
DATA_DIR = PROJECT_ROOT / "data" / "pdf" / "embedded"

# 向量数据库路径
VECTORDB_DIR = PROJECT_ROOT / "vector_db"

# 嵌入模型类型: "openai" 或 "huggingface"
EMBEDDING_MODEL_TYPE = "huggingface"

# HuggingFace 模型名（仅当 EMBEDDING_MODEL_TYPE 为 huggingface 时生效）
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"