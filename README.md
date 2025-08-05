
# BuzzInsight

**BuzzInsight** is a real-time public sentiment dashboard powered by Reddit data. It fetches recent Reddit discussions based on a keyword or topic, performs sentiment analysis using VADER NLP, and generates a clear summary with AI using Groq's LLaMA 3 model.

---

## Features

- Fetches latest Reddit posts for any keyword
- Performs sentiment classification (Positive, Neutral, Negative)
- Generates a word cloud from post contents
- Displays sentiment metrics and distribution
- Summarizes public sentiment using LLaMA 3 via Groq API
- Built with Python, Streamlit, and minimal dependencies

---

## Demo

[https://buzz-insight.streamlit.app/]

---

## Tech Stack

- Python 3.10+
- Streamlit
- PRAW (Reddit API)
- NLTK (VADER Sentiment Analysis)
- Requests (for Groq API)
- WordCloud
- Matplotlib

---

## Project Structure

```

BuzzInsight/
│
├── utils/
│   ├── extractor.py       # Reddit data scraper
│   ├── analyzer.py        # Sentiment analyzer using VADER
│   └── summarizer.py      # AI summarizer using Groq + LLaMA 3
│
├── assets/                # (optional) images, logo etc.
├── .env                   # API keys (excluded from Git)
├── .gitignore
├── requirements.txt
├── streamlit\_app.py       # Main Streamlit application

````

---

## Flowchart

```mermaid
graph TD
    A[User enters topic & clicks Run] --> B[Fetch Reddit Posts via PRAW]
    B --> C[Apply VADER Sentiment Analysis]
    C --> D[Generate Sentiment Metrics]
    C --> E[Create Word Cloud]
    C --> F["Generate Summary with LLaMA 3 via Groq API"]
    D --> G[Display Results in Streamlit]
    E --> G
    F --> G

````

---

## Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/BuzzInsight.git
cd BuzzInsight
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Create `.env` file**

```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_secret
REDDIT_USER_AGENT=your_app_name
GROQ_API_KEY=your_groq_api_key
```

4. **Run locally**

```bash
streamlit run streamlit_app.py
```

---

## Deployment

To deploy on **Streamlit Cloud**:

* Add `.env` variables in the **Secrets** tab in your Streamlit Cloud dashboard.
* Make sure `.env` is listed in `.gitignore` and not pushed to GitHub.
* Push the repo and connect to Streamlit Cloud.

---

## License

MIT License. See `LICENSE` file for details.

---

## Acknowledgements

* Reddit API via PRAW
* VADER from NLTK
* LLaMA 3 via GroqCloud
* Streamlit for the frontend




