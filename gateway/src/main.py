from fastapi import FastAPI, Depends, Request
import requests
import os
from dotenv import load_dotenv
from src.auth_middleware import verify_token

# Load environment variables
load_dotenv()

# FastAPI App
app = FastAPI(title="API Gateway")

# Microservices URLs
CHATBOT_SERVICE_URL = os.getenv("CHATBOT_SERVICE_URL", "http://localhost:8001")
AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://localhost:8002")

@app.get("/")
async def home():
    return {"message": "API Gateway is running"}

@app.get("/chat/")
async def chat_endpoint(request: Request, q: str, user=Depends(verify_token)):
    """ Forward request to Chatbot Service """
    response = requests.get(f"{CHATBOT_SERVICE_URL}/chat/", params={"q": q})
    return response.json()

@app.post("/login/")
async def login(request: Request):
    """ Forward request to Authentication Service """
    data = await request.json()
    response = requests.post(f"{AUTH_SERVICE_URL}/login/", json=data)
    return response.json()
