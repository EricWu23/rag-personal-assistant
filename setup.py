from setuptools import setup, find_packages

setup(
    name="rag_assistant",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "openai",
        "langchain",
        "langchain-community",
        "faiss-cpu",
        "pypdf",
        "python-dotenv",
        "tiktoken",
    ],
    author="Yujiang Wu",
    description="A RAG-based personal assistant using LangChain and OpenAI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)