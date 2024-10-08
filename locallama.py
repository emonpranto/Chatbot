from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
from langchain_community.llms.ollama import Ollama


import streamlit as st
from dotenv import load_dotenv
import os 

load_dotenv()
os.environ['LANGCHAIN_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true' 

if os.getenv('LANGCHAIN_API_KEY') == True :
    print('true')
else:
    print('false')

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that assists your user"),
    ("user", "Question:{Question}")
])


## Streamlit Framework
st.title('Search Pranto LLama2')
input_text = st.text_input("Enter your question")

## llma LLm
# llm = ollama(model='llama2')
# llm = ollama.Ollama(model='llama2')
llm = Ollama(model='llama2')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser


# llm = Ollama(model='llama2')


print('hello')