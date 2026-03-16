from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()

load_dotenv()

import os

app = FastAPI(title="Langchain Server")

qwen = OllamaLLM(model="qwen2.5:7b")
llama = OllamaLLM(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5 years child with 100 words")

add_routes(app, prompt1 | qwen, path="/essay")
add_routes(app, prompt2 | llama, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)