import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from data_loader import load_data

load_dotenv()

def create_agent():
    df = load_data()

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    prompt = ChatPromptTemplate.from_template("""
You are a data analyst.

Here is a summary of the Titanic dataset:

Total rows: {rows}
Columns: {columns}

User question:
{question}

Give a clear and concise answer.
""")

    return llm, df, prompt