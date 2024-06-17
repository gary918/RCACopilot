from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from langchain_core.messages import HumanMessage
#from langchain.callbacks import get_openai_callback
from langchain_community.callbacks.manager import get_openai_callback
from langchain_core.messages import AIMessage

import json

import streamlit as st
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file


def get_messages():
    messages=[]
    for message in st.session_state.messages:
        msg=None
        if message["role"] == "user":
            msg = HumanMessage(content=message["content"])
        elif message["role"] == "assistant":
            msg = AIMessage(content=message["content"])
        if msg is not None:
            messages.append(msg)
    return messages

st.title("Chat")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "user":
            st.markdown(message["content"])
        elif message["role"] == "assistant":
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        model = AzureChatOpenAI(
            openai_api_version="2023-07-01-preview",
            azure_deployment="gpt-4-32k",
        )
        messages = get_messages()
        
        with get_openai_callback() as cb:
            response = model(messages).content
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})


