import streamlit as st  
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.cluster import KMeans
import json

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize an empty list to store articles
articles = []

# Open the JSON file with the articles
with open("nyt_articles.json", 'r', encoding='utf-8') as file:
    # Load the JSON data
    articles = json.load(file)

# Extract descriptions
descriptions = [article['description'] for article in articles]

# Text preprocessing
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Tokenization
    words = word_tokenize(text.lower())
    # Remove stopwords and single character words
    words = [word for word in words if word.isalnum() and word not in stop_words]
    return ' '.join(words)

# Preprocess descriptions
preprocessed_descriptions = [preprocess_text(desc) for desc in descriptions]

# Feature extraction
count_vectorizer = CountVectorizer()
tfidf_transformer = TfidfTransformer()

# Fit and transform CountVectorizer
count_matrix = count_vectorizer.fit_transform(preprocessed_descriptions)

# Transform CountVectorizer output using TfidfTransformer
tfidf_matrix = tfidf_transformer.fit_transform(count_matrix)

# Clustering
kmeans = KMeans(n_clusters=9, random_state=1)
clusters = kmeans.fit_predict(tfidf_matrix)

# Create an array of arrays of articles in each cluster
articles_by_cluster = [[] for _ in range(9)]
for idx, article in enumerate(articles):
    cluster_num = clusters[idx]
    articles_by_cluster[cluster_num].append(article)

# Set page title and icon
st.set_page_config(
    page_title="Articles Clustering",
    page_icon="images/nyt_logo.png"
)
st.title("📰 The NYT Clustered Articles 📰")
st.markdown("<div style='padding: 5px'></div>", unsafe_allow_html=True)
st.markdown("""Explore clusters of news articles from around the world conveniently grouped based on their similarity of content. """)
st.markdown("<div style='padding: 10px'></div>", unsafe_allow_html=True)

# Display articles grouped by cluster
for cluster_num, cluster_articles in enumerate(articles_by_cluster):
    st.markdown("<div style='padding: 5px'></div>", unsafe_allow_html=True)
    current_cluster = cluster_num + 1
    cluster_title = f'<h3 style="color:darkgreen; font-weight:bold;">Cluster {cluster_num + 1} - {len(cluster_articles)} articles </h3>'
    st.markdown(cluster_title, unsafe_allow_html=True)
    
    for article in cluster_articles:
        st.subheader(article['title'])
        st.write(article['description'])
        st.write(f"[Read more]({article['link']})")
        st.markdown("---")   
    st.markdown("<div style='padding: 20px'></div>", unsafe_allow_html=True)
