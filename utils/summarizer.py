import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_summary(text: str, topic: str = "") -> str:
    if not GROQ_API_KEY:
        return "❌ Missing GROQ_API_KEY environment variable."

    prompt = f"""
You are an AI assistant analyzing Reddit sentiment.

Give a structured response with exactly 3 sections:
1. **Overall Public Sentiment:** One word - Positive, Negative, Neutral, or Mixed.
2. **Summary:** A short, neutral report-like overview of the public sentiment (max 100 words).
3. **TL;DR:** A 1-line casual takeaway.

Topic: "{topic}"

Reddit Posts:
{text[:3000]}
"""


    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that summarizes Reddit discussions."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"
