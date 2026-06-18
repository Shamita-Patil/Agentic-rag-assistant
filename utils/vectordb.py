import chromadb

from utils.embeddings import get_embedding


def build_vector_db(chunks):

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    try:
        client.delete_collection(
            "agentic_rag"
        )
    except:
        pass

    collection = client.create_collection(
        name="agentic_rag"
    )

    for idx, chunk in enumerate(chunks):

        collection.add(
            ids=[str(idx)],
            documents=[
                chunk["content"]
            ],
            embeddings=[
                get_embedding(
                    chunk["content"]
                )
            ],
            metadatas=[
                chunk["metadata"]
            ]
        )

    return collection