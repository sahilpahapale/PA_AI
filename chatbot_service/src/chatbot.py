import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Load OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chatbot_response(user_input: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
