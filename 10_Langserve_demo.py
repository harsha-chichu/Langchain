import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes
import uvicorn

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# Load API keys
load_dotenv()
GROQ_API_KEY = os.environ["GROQ_API_KEY"]

# Define LLM
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.7,
)

# Define parser
parser = StrOutputParser()

# Prompt template
system_template = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}'),
])

# Chain
chain = prompt_template | llm | parser

# FastAPI app
app = FastAPI(
    title="Simple Translator",
    version="0.1",
    description="A simple translation app using Groq and LangServe",
)

# Expose chain at /chain
add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
