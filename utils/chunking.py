from langchain.text_splitter import RecursiveCharacterTextSplitter

from config.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


def create_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = []

    for doc in documents:

        text_chunks = splitter.split_text(
            doc["content"]
        )

        for chunk in text_chunks:

            chunks.append({
                "content": chunk,
                "metadata": doc["metadata"]
            })

    return chunks