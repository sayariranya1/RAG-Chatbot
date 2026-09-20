import streamlit as st
import requests


st.set_page_config(
    page_title="RAG CV Chatbot",
    page_icon="🤖"
)


st.title("🤖 Ranya CV Assistant")


question = st.text_input(
    "Ask something about my CV:"
)


if st.button("Send"):

    if question:

        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={
                "question": question
            }
        )

        answer = response.json()["answer"]

        st.write("### Answer:")
        st.write(answer)