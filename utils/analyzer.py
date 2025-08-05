import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon", quiet=True)
analyzer = SentimentIntensityAnalyzer()

def classify_sentiment(text: str) -> tuple:
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        label = "Positive"
    elif score <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"
    return label, score

def analyze_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    results = df["content"].apply(classify_sentiment)
    df["sentiment"] = results.apply(lambda x: x[0])
    df["sentiment_score"] = results.apply(lambda x: x[1])
    return df
