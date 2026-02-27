import streamlit as st
import requests

st.set_page_config(page_title="Titanic AI Agent", layout="centered")

st.title("🚢 Titanic AI Data Agent")

question = st.text_input("Ask a question about the Titanic dataset")

if st.button("Ask"):

    if question.strip() != "":
        with st.spinner("Thinking... Please wait ⏳"):

            try:
                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={"question": question},
                    timeout=180
                )

                if response.status_code == 200:
                    data = response.json()

                    st.subheader("Answer")
                    st.write(data["answer"])

                    if data.get("plot"):
                        st.image(f"http://127.0.0.1:8000{data['plot']}")
                else:
                    st.error(f"Backend error: {response.text}")

            except Exception as e:
                st.error(f"Connection failed: {e}")