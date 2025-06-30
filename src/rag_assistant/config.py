from pathlib import Path
# 数据源路径
DATA_DIR = Path("data/pdf/embedded")

# 向量数据库路径
VECTORDB_DIR = Path("vector_db")

# 嵌入模型类型: "openai" 或 "huggingface"
EMBEDDING_MODEL_TYPE = "huggingface"

# HuggingFace 模型名（仅当 EMBEDDING_MODEL_TYPE 为 huggingface 时生效）
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"