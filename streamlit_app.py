import streamlit as st

from agentic_rag import initialize_agent, ask_question


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Agentic RAG Assistant",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🤖 Agentic RAG")

    st.markdown("---")

    st.markdown("### 📚 Supported Documents")

    st.markdown("""
- 📄 PDF
- 📝 TXT
- 📘 DOCX
- 📊 XLSX
""")

    st.markdown("---")

    st.markdown("### ⚡ Tech Stack")

    st.markdown("""
- Google Gemini
- LangChain
- ChromaDB
- Sentence Transformers
- Serper Search
""")

    st.markdown("---")

    st.success("Agent Ready")


# -----------------------------
# Main Page
# -----------------------------
st.title("🤖 Agentic RAG Assistant")

st.write(
    """
Ask questions from enterprise documents or the web.

The AI Agent intelligently decides whether to retrieve
information from your document collection or perform
a real-time web search.
"""
)


# -----------------------------
# Initialize Agent (Only Once)
# -----------------------------
if "agent" not in st.session_state:

    with st.spinner("Initializing AI Agent..."):

        st.session_state.agent = initialize_agent()


# -----------------------------
# User Input
# -----------------------------
question = st.text_input(
    "Ask your question",
    placeholder="Example: What is the leave policy?"
)


# -----------------------------
# Ask Button
# -----------------------------
if st.button("Ask"):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating answer..."):

            try:

                answer = ask_question(
                    st.session_state.agent,
                    question
                )

                st.markdown("## ✅ Answer")

                st.write(answer)

            except Exception as e:

                st.error(f"Error: {e}")


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "Built using Google Gemini • LangChain • ChromaDB • Sentence Transformers • Serper API"
)