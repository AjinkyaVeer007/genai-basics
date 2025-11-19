from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

res = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are an maths professionist and you will only answer maths related questions. If someone ask you other than maths questions then simply say Sorry i can only assist you with maths related questions."
        },
        {
            "role": "user",
            "content": "what is 2+2"
        }
    ]
)

print(res.choices[0].message.content)