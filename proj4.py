import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\POORINSHA\Documents\project.py\Task 4\twitter_training.csv")

# Rename columns for clarity
df.columns = ['id', 'topic', 'sentiment', 'text']

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())

# Drop rows where 'text' is missing
df = df.dropna(subset=['text'])

# Show sample data
print("\nSample Data:")
print(df.head())

# Sentiment distribution
plt.figure(figsize=(6, 4))
df['sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'blue'])
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.tight_layout()
plt.show()

# Word Cloud of all tweets
text_data = ' '.join(df['text'].tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white',
                      stopwords=set(STOPWORDS)).generate(text_data)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Common Words in Tweets")
plt.tight_layout()
plt.show()
