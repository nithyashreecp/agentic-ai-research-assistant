import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

INDEX_NAME = os.getenv("PINECONE_INDEX")

# Load embedding model locally
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Init Pinecone
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

#  CREATE INDEX IF IT DOES NOT EXIST
existing_indexes = [index["name"] for index in pc.list_indexes()]

if INDEX_NAME not in existing_indexes:
    print(f"Creating Pinecone index: {INDEX_NAME}")

    pc.create_index(
        name=INDEX_NAME,
        dimension=384,              
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

# 🔹 CONNECT TO INDEX
index = pc.Index(INDEX_NAME)


# STORE FUNCTION
def store_text(text, doc_id):
    vector = embedding_model.encode(text).tolist()
    index.upsert([
        {
            "id": doc_id,
            "values": vector,
            "metadata": {"text": text}
        }
    ])


# RETRIEVE FUNCTION
def retrieve_similar(query, top_k=5, score_threshold=0.40):
    vector = embedding_model.encode(query).tolist()

    res = index.query(
        vector=vector,
        top_k=top_k,
        include_metadata=True
    )

    filtered = []
    for match in res["matches"]:
        if match["score"] >= score_threshold:
            filtered.append(match["metadata"]["text"])

    return filtered







