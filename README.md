# RAG Chatbot

A simple Retrieval-Augmented Generation (RAG) chatbot built with Python, ChromaDB, and Claude (Anthropic API). 
It answers questions using only the content of a provided document, instead of relying on general AI knowledge.

## How it works

1. A text document is split into chunks (by paragraph)
2. Each chunk is converted into an embedding using `sentence-transformers`
3. Embeddings are stored in a local vector database (ChromaDB)
4. When a question is asked, the most relevant chunks are retrieved
5. Those chunks are sent to Claude along with the question, so it answers using only that context

## Tech stack

- Python
- [ChromaDB](https://www.trychroma.com/) — vector database
- [sentence-transformers](https://www.sbert.net/) — embedding model (`all-MiniLM-L6-v2`)
- [Anthropic API](https://www.anthropic.com/) — Claude for generating answers

## Setup

1. Clone this repo
```bash
   git clone https://github.com/HM1506/rag_chatbot.git
   cd rag_chatbot
```

2. Create a virtual environment and install dependencies
```bash
   python -m venv venv
   source venv/Scripts/activate   # Windows
   pip install chromadb sentence-transformers anthropic python-dotenv
```

3. Add your Anthropic API key
   Create a `.env` file in the project root:
   ANTHROPIC_API_KEY=your-key-here

4. Build the vector database from your document
```bash
   python build_database.py
```

5. Run the chatbot
```bash
   python chatbot.py
```

## Example
Your question: What GPA do I need for Computer Science?
Retrieved relevant chunks:

Admission to the Computer Science program requires a minimum GPA of 3.0...

Answer: According to the context, you need a minimum GPA of 3.0 for admission.

## Future improvements

- Support PDF documents instead of plain text
- Add a simple web interface
- Allow multiple documents to be loaded at once