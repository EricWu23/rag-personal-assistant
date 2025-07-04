from langchain_openai import ChatOpenAI
from langchain.llms import HuggingFaceHub
from langchain_core.language_models import BaseLanguageModel
from rag_assistant.config import LLM_TYPE, LOCAL_MODEL_PATH, OPENAI_API_KEY, OPENAI_MODEL_NAME,LLAMA_CPP_N_CTX,LLAMA_CPP_N_GPU_LAYERS
from openai import OpenAIError
import os

def get_llm() -> BaseLanguageModel:
    if LLM_TYPE == "openai":
        try:
            from langchain_openai import ChatOpenAI
            print("🔌 Using OpenAI Chat Model:", OPENAI_MODEL_NAME)
            return ChatOpenAI(model=OPENAI_MODEL_NAME, api_key=OPENAI_API_KEY)
        except Exception as e:
            print(f"⚠️ OpenAI failed: {e}")
            print("⏬ Fallback to local GGUF model...")
            return _load_local_llm()

    elif LLM_TYPE == "local":
        return _load_local_llm()

    else:
        raise ValueError(f"❌ Unsupported LLM_TYPE: {LLM_TYPE}")

def _load_local_llm():
    try:
        from langchain.llms import LlamaCpp
        print("💻 Using Local GGUF Model:", LOCAL_MODEL_PATH)
        return LlamaCpp(
            model_path=str(LOCAL_MODEL_PATH),
            n_ctx=LLAMA_CPP_N_CTX,
            n_gpu_layers=LLAMA_CPP_N_GPU_LAYERS,
            temperature=0.7,
            top_p=0.95,
            max_tokens=512,
            verbose=False
        )
    except ImportError:
        raise ImportError("Please install llama-cpp-python with: pip install llama-cpp-python")