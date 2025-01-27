import os
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Load environment variables
load_dotenv()

# Client configuration
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": request.message}
        ]
    )
    return {"reply": response.choices[0].message.content}

from fastapi.responses import FileResponse

@app.get("/")
def read_index():
    return FileResponse("index.html")