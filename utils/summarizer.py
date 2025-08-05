import requests
import streamlit as st

def generate_summary(text: str, topic: str = "") -> str:
    api_key = st.secrets["GROQ_API_KEY"]
    if not api_key:
        return "❌ Missing GROQ_API_KEY in Streamlit secrets."

    prompt = (
        f"You are an AI assistant analyzing Reddit sentiment.\n\n"
        f"Give a structured response with exactly 3 sections:\n"
        f"1. **Overall Public Sentiment:** One word - Positive, Negative, Neutral, or Mixed.\n"
        f"2. **Summary:** A short, neutral report-like overview of the public sentiment (max 100 words).\n"
        f"3. **TL;DR:** A 1-line casual takeaway.\n\n"
        f"Topic: \"{topic}\"\n\n"
        f"Reddit Posts:\n{text[:3000]}"
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
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
