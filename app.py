import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fc;
    }
    .stChatMessage {
        border-radius: 12px;
        padding: 10px;
        margin-bottom: 8px;
    }
    .title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #1f4e79;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🤖 AI Chatbot using LangChain</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Built with Streamlit + LangChain + OpenAI</div>', unsafe_allow_html=True)

# Validate API key
api_key = "ypurapikey"

# Create model
llm = ChatOpenAI(
    model="gpt-5-mini",
    temperature=0.7,
    api_key=api_key
)

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

if "chat_display" not in st.session_state:
    st.session_state.chat_display = []

# Show previous chat messages
for msg in st.session_state.chat_display:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Show user message
    st.session_state.chat_display.append({"role": "user", "content": user_input})
    st.session_state.messages.append(HumanMessage(content=user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(st.session_state.messages)
            bot_reply = response.content
            st.markdown(bot_reply)

    # Save assistant response
    st.session_state.messages.append(AIMessage(content=bot_reply))
    st.session_state.chat_display.append({"role": "assistant", "content": bot_reply})

# Sidebar
with st.sidebar:
    st.header("Settings")
    st.write("Simple AI chatbot interface")
    
    if st.button("Clear Chat"):
        st.session_state.messages = [
            SystemMessage(content="You are a helpful AI assistant.")
        ]
        st.session_state.chat_display = []
        st.rerun()