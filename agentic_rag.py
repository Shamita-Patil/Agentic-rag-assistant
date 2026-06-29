import os

from utils.document_processor import load_documents
from utils.chunking import create_chunks
from utils.vectordb import build_vector_db

from agents.research_agent import create_agent

from config.config import DOCUMENT_FOLDER


def initialize_agent():
    """
    Loads documents, creates chunks,
    builds the vector database,
    and returns the initialized AI agent.
    """

    print("\nLoading documents...")

    documents = load_documents(
        DOCUMENT_FOLDER
    )

    print(
        f"Loaded {len(documents)} documents"
    )

    print(
        "\nCreating chunks..."
    )

    chunks = create_chunks(
        documents
    )

    print(
        f"Created {len(chunks)} chunks"
    )

    print(
        "\nBuilding vector database..."
    )

    collection = build_vector_db(
        chunks
    )

    print(
        "Vector DB ready"
    )

    print(
        "\nStarting Agent..."
    )

    agent = create_agent(
        collection
    )

    return agent


def ask_question(agent, question):
    """
    Returns the AI-generated answer
    for the given question.
    """

    return agent.run(question)


def main():

    agent = initialize_agent()

    while True:

        question = input(
            "\nAsk Question (type exit): "
        )

        if question.lower() == "exit":

            print("\nGoodbye!")

            break

        try:

            answer = ask_question(
                agent,
                question
            )

            print(
                "\nAnswer:\n"
            )

            print(answer)

        except Exception as e:

            print(
                f"\nError: {e}"
            )


if __name__ == "__main__":

    main()
