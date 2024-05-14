from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from langchain_community.llms import Ollama

import os

import streamlit as st

from dotenv import load_dotenv


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## PROMT TEMPLATE

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","Use AI to respond to queries responsibly!"),
        ("user","Question:{question}")
    ]
)

## STREAMLIT framework
st.title("Langchain Demo 2 with Llama2 API")
input_text=st.text_input("Search for a particular topic")

## call Llama2 llm
llm=Ollama(model="llama2")

output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke(
        {'question':input_text}
    ))
