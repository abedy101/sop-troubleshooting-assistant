import streamlit as st
from rag_engine import get_qa_chain

st.set_page_config(page_title="SOP Troubleshooting Assistant")

st.title("📄 SOP Troubleshooting Assistant")
st.caption("Ask questions based on your uploaded SOP/manual")

qa_chain = get_qa_chain()

st.caption("📄 Currently loaded document: iPhone User Guide (for demo)")
question = st.text_input("Welcome. How May I help you today?", "")

if question:
    with st.spinner("Searching..."):
        response = qa_chain.run(question)
        st.success(response)

