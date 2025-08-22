import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def summarize_text(text, detail_level="detailed"):
    prompt = f"Provide a {detail_level} summary of the following PDF content:\n{text}"

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192"
    )

    return response.choices[0].message.content
