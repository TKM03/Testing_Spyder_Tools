import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud
import os

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Load and preprocess text
def load_text(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return ""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    words = [word for word in tokens if word.isalnum() and word not in stop_words]
    return words

# Word frequency analysis
def word_frequency(words):
    word_counts = Counter(words)
    return pd.DataFrame(word_counts.items(), columns=['Word', 'Count']).sort_values(by='Count', ascending=False)

# Sentiment analysis
def sentiment_analysis(text):
    sentences = nltk.sent_tokenize(text)
    sentiment_scores = []
    for sentence in sentences:
        score = sia.polarity_scores(sentence)
        sentiment_scores.append({
            'Sentence': sentence,
            'Positive': score['pos'],
            'Negative': score['neg'],
            'Neutral': score['neu'],
            'Compound': score['compound']
        })
    return pd.DataFrame(sentiment_scores)

# Visualizations
def plot_word_cloud(word_freq):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(
        dict(word_freq.values)
    )
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def plot_sentiment(sentiment_df):
    fig = px.line(sentiment_df, x=sentiment_df.index, y=['Positive', 'Negative', 'Neutral'], 
                  title="Sentiment Trends Across Text",
                  labels={'value': 'Score', 'index': 'Sentence Number'})
    fig.update_layout(showlegend=True)
    fig.show()

# Main program
def main():
    print("--- Text Analysis and Sentiment Visualization Tool ---")
    file_path = input("Enter the path to your text file (e.g., sample.txt): ")
    
    # Load and process text
    text = load_text(file_path)
    if not text:
        return
    
    words = preprocess_text(text)
    
    # Word frequency
    word_freq = word_frequency(words)
    print("\nTop 10 Most Frequent Words:")
    print(word_freq.head(10))
    
    # Sentiment analysis
    sentiment_df = sentiment_analysis(text)
    print("\nSentiment Summary:")
    print(sentiment_df[['Positive', 'Negative', 'Neutral', 'Compound']].mean())
    
    # Visualizations
    print("\nGenerating visualizations...")
    plot_word_cloud(word_freq)
    plot_sentiment(sentiment_df)

if __name__ == "__main__":
    main()