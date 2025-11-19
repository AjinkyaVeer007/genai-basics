from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("GEMINI_BASE_URL")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

res = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "system",
            "content": "You are an maths professionist and you will only answer maths related questions. If someone ask you other than maths questions then simply say Sorry i can only assist you with maths related questions."
        },
        {
            "role": "user",
            "content": "What is the factorial of 69"
        }
    ]
)

print(res.choices[0].message.content)