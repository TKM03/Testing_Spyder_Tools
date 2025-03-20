# Text Analysis and Sentiment Visualization Tool

A Python-based tool built in Spyder to analyze text files for word frequency and sentiment, with visualizations including word clouds and sentiment trends. This project demonstrates proficiency in Spyder's editor, IPython console, variable explorer, and plotting capabilities, alongside NLP techniques.

## Features
- **Text Processing**: Loads text files, tokenizes words, and removes stopwords using NLTK.
- **Word Frequency Analysis**: Calculates and displays the most frequent words in the text.
- **Sentiment Analysis**: Evaluates text sentiment (positive, negative, neutral) using NLTK's VADER.
- **Visualizations**:
  - Word cloud of frequent words (via Matplotlib).
  - Interactive sentiment trend plot (via Plotly).
- **Spyder Integration**: Leverages Spyder’s features for development, debugging, and data exploration.

## Prerequisites
- Python 3.6+
- Spyder IDE (recommended via Anaconda)
- Required libraries:
  - `nltk`
  - `pandas`
  - `matplotlib`
  - `plotly`
  - `wordcloud`

## Installation
1. **Clone or Download the Project**:
   - Download this repository or copy the `text_analyzer.py` file into a folder named `TextAnalyzer`.

2. **Set Up Environment**:
   - Open Spyder (install via [Anaconda](https://www.anaconda.com/) if needed).
   - Create a new project in Spyder: `Projects > New Project`, name it "TextAnalyzer", and select your folder.

3. **Install Dependencies**:
   - Open a terminal in Spyder (Tools > Open a terminal) or use your system terminal.
   - Run:
     ```bash
     pip install nltk pandas matplotlib plotly wordcloud
