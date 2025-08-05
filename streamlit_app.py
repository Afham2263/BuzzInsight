import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime

from utils.extractor import get_reddit_posts
from utils.analyzer import analyze_sentiment
from utils.summarizer import generate_summary

st.set_page_config(
    page_title="BuzzInsight - Public Sentiment Dashboard",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align: center; color: #00BFFF;'>BuzzInsight</h1>
    <h4 style='text-align: center; color: white; font-weight: 300;'>Real-Time Public Sentiment Dashboard</h4>
    <hr style="border: 1px solid #00BFFF; margin-bottom: 2rem;">
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("Tracking Settings")
    query = st.text_input("Enter keyword/topic", value="AI")
    limit = st.slider("Number of posts to fetch", 10, 200, 100)
    run_button = st.button("Run Sentiment Analysis")

if run_button:
    st.info("Fetching data...")

    posts_df = get_reddit_posts(query=query, limit=limit)
    if posts_df.empty:
        st.error("No data retrieved. Try a different topic.")
        st.stop()

    posts_df = analyze_sentiment(posts_df)
    st.success(f"{len(posts_df)} posts retrieved and analyzed.")

    st.markdown("###  AI-Generated Sentiment Summary")
    text_blob = " ".join(posts_df['content'].dropna().values[:25])
    summary = generate_summary(text_blob, topic=query)
    st.info(summary)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Positive", f"{(posts_df['sentiment'] == 'Positive').mean() * 100:.2f}%")
        st.metric("Neutral", f"{(posts_df['sentiment'] == 'Neutral').mean() * 100:.2f}%")
        st.metric("Negative", f"{(posts_df['sentiment'] == 'Negative').mean() * 100:.2f}%")
    with col2:
        st.markdown("**Sentiment distribution**")
        sentiment_counts = posts_df['sentiment'].value_counts()
        st.bar_chart(sentiment_counts)

    st.markdown("###  Word Cloud")
    full_text = " ".join(posts_df['content'].dropna().values)
    wordcloud = WordCloud(width=1000, height=400, background_color='white', colormap='viridis').generate(full_text)
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)

    st.markdown("###  Raw Data")
    st.dataframe(posts_df)

else:
    st.warning("Enter a topic and click Run to start.")
