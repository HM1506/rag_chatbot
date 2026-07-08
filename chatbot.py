from dotenv import load_dotenv
from anthropic import Anthropic
import chromadb
from chromadb.utils import embedding_functions
import os

# Load API key
load_dotenv()
client_ai = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Connect to our existing vector database
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
client_db = chromadb.PersistentClient(path="./chroma_db")
collection = client_db.get_or_create_collection(
    name="my_documents",
    embedding_function=embedding_function
)

def ask_question(question):
    # 1. RETRIEVAL: find the most relevant chunks for this question
    results = collection.query(
        query_texts=[question],
        n_results=2  # get the top 2 most relevant chunks
    )
    relevant_chunks = results["documents"][0]

    print("\n📚 Retrieved these relevant chunks:")
    for chunk in relevant_chunks:
        print(f"  - {chunk[:80]}...")

    # 2. Combine the chunks into context text
    context = "\n\n".join(relevant_chunks)

    # 3. GENERATION: ask Claude to answer using only this context
    prompt = f"""Answer the question using ONLY the information in the context below.
If the answer isn't in the context, say "I don't have that information."

Context:
{context}

Question: {question}"""

    response = client_ai.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text

# Simple loop to keep asking questions
print("💬 RAG Chatbot ready! Type 'quit' to exit.\n")
while True:
    question = input("Your question: ")
    if question.lower() == "quit":
        break
    answer = ask_question(question)
    print(f"\n🤖 Answer: {answer}\n")