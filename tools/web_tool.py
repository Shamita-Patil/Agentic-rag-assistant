import requests

from langchain.tools import Tool

from config.config import SERPER_API_KEY


def web_search(query):

    url = (
        "https://google.serper.dev/search"
    )

    payload = {
        "q": query
    }

    headers = {
        "X-API-KEY":
        SERPER_API_KEY,
        "Content-Type":
        "application/json"
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    data = response.json()

    snippets = []

    for item in data.get(
        "organic",
        []
    )[:5]:

        title = item.get(
            "title",
            ""
        )

        snippet = item.get(
            "snippet",
            ""
        )

        link = item.get(
            "link",
            ""
        )

        snippets.append(
            f"""
Title: {title}

Snippet: {snippet}

URL: {link}
"""
        )

    return "\n".join(snippets)


web_tool = Tool(
    name="Web_Search",
    func=web_search,
    description="""
Useful for:
latest news,
recent events,
industry trends,
internet research,
facts not available
in the document collection.
"""
)