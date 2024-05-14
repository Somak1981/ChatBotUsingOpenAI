import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",json={'input':{'topic':input_text}})
    
    return response.json()['output']['content']


def get_ollama_response(input_text1):
    response=requests.post("http://localhost:8000/story/invoke",json={'input':{'topic':input_text1}})
    
    return response.json()['output']['content']

st.title('Langchain Demo with OpenAI and Llama2')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a story on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))