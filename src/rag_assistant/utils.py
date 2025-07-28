# src/rag_assistant/utils.py
from pathlib import Path
from src.rag_assistant.ingest import main as update_db
import requests
from tqdm import tqdm

def get_project_root() -> Path:
    # 假设 utils.py 一定在项目 src/rag_assistant/ 目录
    return Path(__file__).resolve().parents[2]  # 往上跳两级到项目根目录

def vector_db_exists() -> bool:
    from src.rag_assistant.config import VECTORDB_DIR
    return (
        (VECTORDB_DIR / "index.faiss").exists()
        and (VECTORDB_DIR / "index.pkl").exists()
    )

def ensure_vector_db_exists():
    from src.rag_assistant.config import VECTORDB_DIR
    if not vector_db_exists():
        print("🔍 Vector DB not found. Starting ingestion pipeline...")
        update_db()
        print("✅ Vector DB created and saved to:", VECTORDB_DIR)
    else:
        print(f"✅ Vector DB already exists at: {VECTORDB_DIR}")


def ensure_model_exists():
    from src.rag_assistant.config import LOCAL_MODEL_PATH,LOCAL_MODEL_DIR,LOCAL_MODEL_URL
    if not LOCAL_MODEL_PATH.exists():
        print(f"🔻 Model not found at {LOCAL_MODEL_PATH}. Downloading from HuggingFace...")
        LOCAL_MODEL_DIR.mkdir(parents=True, exist_ok=True)

        with requests.get(LOCAL_MODEL_URL, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            block_size = 8192  # 8KB
            t = tqdm(total=total_size, unit='iB', unit_scale=True, desc="Downloading Model")

            with open(LOCAL_MODEL_PATH, 'wb') as f:
                for chunk in r.iter_content(chunk_size=block_size):
                    if chunk:
                        f.write(chunk)
                        t.update(len(chunk))
            t.close()

        print("✅ Model downloaded successfully.")
    else:
        print(f"✅ Model already exists at {LOCAL_MODEL_PATH}.")