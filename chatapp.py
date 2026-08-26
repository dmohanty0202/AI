# install ollama
# install pip install streamlit ollama

import streamlit as st
import ollama

st.set_page_config(
    page_title="AI-103 Local Chat",
    page_icon="🤖"
)

st.title("🤖 Local AI Chat Application")
st.caption("Powered by Ollama - no Azure or Microsoft Foundry required")

MODEL_NAME = "llama3.2"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant."
        }
    ]

# Display previous messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Get user input
prompt = st.chat_input("Ask me anything...")

if prompt:
    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Ollama
    response = ollama.chat(
        model=MODEL_NAME,
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]

    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)
