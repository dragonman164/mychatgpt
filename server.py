from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# ENV Setup
load_dotenv()
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# Enabling LangSmith Tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt Template
question = "What is the capital of France?"
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful chat assistant. Please answer the user queries.?"),
    ("user", "Question: {question}"),
])

# Gemini Call 
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", model_kwargs={"generation_config": {"temperature": 0.1, "top_p": 1, "top_k": 1, "max_output_tokens": 1024}})
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

# Streamlit UI
st.title("Gemini Chat Assistant")

user_question = st.text_input("Ask a question:", value=question)

if st.button("Get Answer"):
    response = chain.invoke({"question": user_question})
    st.write("**Answer:**", response)

