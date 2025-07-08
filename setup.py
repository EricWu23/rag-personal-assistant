from setuptools import setup, find_packages
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="rag_assistant",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "packaging==24.0",
        "llama-cpp-python>=0.2.24",
        "openai==1.93.1",
        "langchain==0.2.17",
        "langchain-community==0.2.19",
        "langchain-openai==0.1.25",
        "tokenizers>=0.19.1,<0.20",
        "langchain_huggingface",
        "faiss-cpu==1.8.0.post1",
        "pypdf==5.7.0",
        "python-dotenv==1.0.1",
        "tiktoken==0.7.0",
        "fastapi>=0.100",
        "uvicorn>=0.22",
        "gunicorn",
        "pydantic>=1.10,<2",
    ],
    author="Yujiang Wu",
    description="A RAG-based personal assistant using LangChain and OpenAI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)