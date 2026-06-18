from utils.embeddings import get_embedding


def retrieve(
    collection,
    query,
    top_k=4
):

    query_embedding = get_embedding(
        query
    )

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=top_k
    )

    return results