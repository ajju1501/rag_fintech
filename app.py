import streamlit as st
from rag_utils import ask_query

st.set_page_config(page_title="📈 Fintech RAG Assistant", layout="centered")

st.title("📊 AI Stock Analyst for Indian Market")
st.markdown("Ask any query about listed companies (e.g., *What is the ROE of TCS?*)")

query = st.text_input("🔍 Enter your query", placeholder="e.g. What is the PE ratio of Reliance?")

if st.button("Ask AI") and query:
    with st.spinner("Fetching real-time data & generating answer..."):
        answer = ask_query(query)
    st.success("✅ Answer")
    st.write(answer)
