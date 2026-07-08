import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# ----------------------------------------------------
# Paths
# ----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INDEX_PATH = os.path.join(BASE_DIR, "faiss_index.index")
META_PATH = os.path.join(BASE_DIR, "metadata.pkl")

# ----------------------------------------------------
# Load FAISS index
# ----------------------------------------------------
try:
    index = faiss.read_index(INDEX_PATH)
except Exception as e:
    raise RuntimeError(f"Unable to load FAISS index: {e}")

# ----------------------------------------------------
# Load metadata
# ----------------------------------------------------
try:
    with open(META_PATH, "rb") as f:
        metadata = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Unable to load metadata: {e}")

# ----------------------------------------------------
# Load embedding model
# ----------------------------------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")


def search_similar_cases(query, top_k=5):
    """
    Search the FAISS vector database for similar historical incidents.

    Parameters
    ----------
    query : str
        User incident description.

    top_k : int
        Number of similar incidents to return.

    Returns
    -------
    list
        List of similar incident dictionaries.
    """

    if not query or not query.strip():
        return []

    # Generate embedding
    embedding = model.encode([query], convert_to_numpy=True)
    embedding = embedding.astype(np.float32)

    # Search
    distances, indices = index.search(embedding, top_k)

    results = []

    for rank, (idx, distance) in enumerate(zip(indices[0], distances[0]), start=1):

        if idx == -1:
            continue

        ticket = metadata[idx]

        results.append({
            "rank": rank,
            "distance": float(distance),
            "ticket_number": ticket.get("Number", ""),
            "description": ticket.get("Description", ""),
            "close_notes": ticket.get("Close notes", ""),
            "root_cause": ticket.get("root_cause", ""),
            "similarity_score": round(1 / (1 + float(distance)), 4)
        })

    return results


# ----------------------------------------------------
# Testing
# ----------------------------------------------------
if __name__ == "__main__":

    query = "Orders not showing complete status in POS system"

    similar_cases = search_similar_cases(query)

    for case in similar_cases:

        print(f"Rank : {case['rank']}")
        print(f"Similarity : {case['similarity_score']}")
        print(f"Distance : {case['distance']}")
        print(f"Ticket : {case['ticket_number']}")
        print(f"Root Cause : {case['root_cause']}")
        print(f"Description : {case['description']}")
        print("-" * 80)
