# src/rag_assistant/utils.py
from pathlib import Path
def get_project_root() -> Path:
    # 假设 utils.py 一定在项目 src/rag_assistant/ 目录
    return Path(__file__).resolve().parents[2]  # 往上跳两级到项目根目录