import streamlit as st
import sys
sys.path.append("src/generation")
sys.path.append("src/ingestion")

from chain import ask

st.title("RAG Document QnA")

#store chat history in session
if "history" not in st.session_state:
    st.session_state.history = []

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
if prompt := st.chat_input("Ask a question about your document..."):
    with st.chat_message("user"):
        st.write(prompt)
    result = ask(prompt, st.session_state.history)
    with st.chat_message("assistant"):
        st.write(result["answer"])
        st.write(f"Sources: pages {result["sources"]}")
    st.session_state.history.append({"role":"user", "content":prompt})
    st.session_state.history.append({"role":"assistant", "content":answer})
