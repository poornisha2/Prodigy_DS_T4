# Task 4: Twitter Entity Sentiment Analysis — Comillas Negras Dataset

## 📌 Objective

The goal of this task is to explore and analyze the **Comillas Negras Twitter dataset**, which focuses on sentiment analysis related to specific entities mentioned in tweets. The task aims to uncover patterns in sentiment distribution and prepare the data for future modeling or classification tasks.

---

## 📁 Dataset Overview

The **Comillas Negras** dataset includes tweets annotated for sentiment in relation to entities such as games (e.g., Borderlands). It is useful for analyzing how users feel about certain topics or entities on Twitter.

### 🔑 Sample Columns

| Column | Description |
|--------|-------------|
| `id` | Tweet ID |
| `entity` | Entity referenced in the tweet (e.g., "Borderlands") |
| `sentiment` | Sentiment label (Positive, Negative, Neutral) |
| `text` | Actual tweet text content |

> Note: Column names may need renaming or cleaning due to formatting issues in the raw dataset.

---

## 🧹 Data Cleaning

- Renamed confusing column headers for clarity
- Removed rows with missing or null tweet content
- Verified consistency of sentiment labels
- Handled unnecessary whitespaces and encoding issues

---

## 🔍 Exploratory Data Analysis (EDA)

Performed the following analyses:

1. **Sentiment Distribution**
   - Bar chart of positive, negative, and neutral tweet counts

2. **Top Entities**
   - Frequency analysis of entities mentioned in the dataset

3. **Word Frequency**
   - Word clouds for each sentiment class

4. **Tweet Length Analysis**
   - Distribution of tweet lengths and their relation to sentiment

5. **Missing Values**
   - Evaluated and visualized missing data patterns

---

## 📦 Tools Used

- Python  
- Pandas  
- Seaborn  
- Matplotlib  
- WordCloud  
- scikit-learn (for future validation splitting)

---

## ✂️ Dataset Split

- Stratified train-validation split using `train_test_split`
- Output files:
  - `twitter_train.csv`
  - `twitter_validation.csv`

Contact Me:www.linkedin.com/in/poornisha-krishnan-0579802a6
