from langchain.tools import Tool

from utils.retriever import retrieve


def create_pdf_tool(collection):

    def search_documents(query):

        results = retrieve(
            collection,
            query
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        context = []

        for doc, meta in zip(
            documents,
            metadatas
        ):

            source = meta.get(
                "source",
                "Unknown"
            )

            context.append(
                f"Source: {source}\n{doc}"
            )

        return "\n\n".join(context)

    return Tool(
        name="Document_Search",
        func=search_documents,
        description="""
Useful for answering questions
about the uploaded documents.
Use this tool whenever the
question may be answered
from the internal knowledge base.
"""
    )