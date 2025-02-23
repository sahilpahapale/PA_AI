from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer
import requests
import os

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://localhost:8002")

security = HTTPBearer()

def verify_token(token: str = Security(security)):
    """Verify JWT token via Auth Service"""
    headers = {"Authorization": f"Bearer {token.credentials}"}
    response = requests.get(f"{AUTH_SERVICE_URL}/verify-token/", headers=headers)
    
    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    
    return response.json()  # Return user data
