import praw
import pandas as pd

def get_reddit_posts(query: str, limit: int = 100) -> pd.DataFrame:
    reddit = praw.Reddit(
        client_id="F8cmDkkYtdBMEmeNr5FaXg",
        client_secret="um97McZhsjo-cs-6gw7gTDN7Wr9P6Q",
        user_agent="PulseBoardApp by Afham"
    )

    results = []
    for submission in reddit.subreddit("all").search(query, sort="new", limit=limit):
        results.append({
            "content": submission.title + "\n" + (submission.selftext or ""),
            "author": str(submission.author),
            "date": pd.to_datetime(submission.created_utc, unit='s')
        })

    return pd.DataFrame(results)
