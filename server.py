# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

import google.generativeai as genai

import streamlit as st
import os
from dotenv import load_dotenv


# ENV Setup
load_dotenv()
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# # Enabling LangSmith Tracing
# os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt Template
question = "What is the capital of France?"
model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')

# Streamlit UI
st.title("Gemini Chat Assistant")

user_question = st.text_input("Ask a question:", value=question)

if st.button("Get Answer"):
    response = model.generate_content(user_question).text
    st.write("**Answer:**", response)

