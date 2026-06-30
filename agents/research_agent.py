from langchain.agents import (
    initialize_agent,
    AgentType
)

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from config.config import GEMINI_API_KEY
from tools.web_tool import web_tool
from tools.pdf_tool import create_pdf_tool
from config.config import MODEL_NAME


def create_agent(collection):

    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        google_api_key=GEMINI_API_KEY,
        temperature=0.2
    )

    pdf_tool = create_pdf_tool(
        collection
    )

    tools = [
        pdf_tool,
        web_tool
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors = True,
        max_iterations=3
    )

    return agent
