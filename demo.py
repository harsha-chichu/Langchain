import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=GEMINI_API_KEY)

for chunk in llm.stream(
    "Tell me one fun fact about the kennedy family. i need in detail response."
):
    print(chunk.content, end="",flush=True)