import os
import praw
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def get_reddit_posts(query: str, limit: int = 100) -> pd.DataFrame:
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    results = []
    for submission in reddit.subreddit("all").search(query, sort="new", limit=limit):
        results.append({
            "content": submission.title + "\n" + (submission.selftext or ""),
            "author": str(submission.author),
            "date": pd.to_datetime(submission.created_utc, unit='s')
        })

    return pd.DataFrame(results)
