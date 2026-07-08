import chromadb
from chromadb.utils import embedding_functions

# 1. Read the document
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 2. Split into chunks (using blank lines as separators)
chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

print(f"Split document into {len(chunks)} chunks:")
for i, chunk in enumerate(chunks):
    print(f"  Chunk {i}: {chunk[:60]}...")

# 3. Set up the embedding function (converts text to "fingerprints")
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# 4. Create a database client (stores everything in a local folder called "chroma_db")
client = chromadb.PersistentClient(path="./chroma_db")

# 5. Create (or get) a collection - think of this like a table in a database
collection = client.get_or_create_collection(
    name="my_documents",
    embedding_function=embedding_function
)

# 6. Add our chunks to the collection, each with a unique ID
collection.add(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)

print(f"\n✅ Successfully stored {len(chunks)} chunks in the vector database!")