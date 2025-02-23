from fastapi import FastAPI, Query
from src.chatbot import get_chatbot_response

app = FastAPI(title="Chatbot Service")

@app.get("/")
async def home():
    return {"message": "Chatbot Service is running"}

@app.get("/chat/")
async def chat(q: str = Query(..., description="User input for chatbot")):
    response = get_chatbot_response(q)
    return {"user_input": q, "response": response}
