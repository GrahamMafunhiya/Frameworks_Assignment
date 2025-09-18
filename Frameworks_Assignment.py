import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
import streamlit as st
from wordcloud import WordCloud

# ---------------------------
#Load CSV
# ---------------------------
file_path = "/Users/GRAHAM/Documents/Frameworks_Assignment/metadata.csv"
df = pd.read_csv(file_path)

# ---------------------------
#Handle missing values
# Drop rows with missing 'title' (critical)
df = df.dropna(subset=['title'])

# Fill missing abstracts with placeholder
if 'abstract' in df.columns:
    df['abstract'] = df['abstract'].fillna('No abstract')

# ---------------------------
#Convert publication date to datetime
# ---------------------------
date_column = 'publish_time'  # adjust if different
df[date_column] = pd.to_datetime(df[date_column], errors='coerce')

# Extract publication year
df['pub_year'] = df[date_column].dt.year.astype('Int64')  # integer type
# Optional: month and day
df['pub_month'] = df[date_column].dt.month
df['pub_day'] = df[date_column].dt.day

# ---------------------------
#Count papers by publication year
# ---------------------------
papers_per_year = df['pub_year'].value_counts().sort_index()
print("Papers per year:\n", papers_per_year)

# Plot
plt.figure(figsize=(10,5))
papers_per_year.plot(kind='bar', color='skyblue')
plt.xlabel("Publication Year")
plt.ylabel("Number of Papers")
plt.title("COVID-19 Papers by Publication Year")
plt.show()

# ---------------------------
#Top journals publishing COVID-19 research
# ---------------------------
if 'journal' in df.columns:
    top_journals = df['journal'].dropna().value_counts().head(10)
    print("\nTop 10 Journals:\n", top_journals)

    # Plot
    plt.figure(figsize=(8,5))
    top_journals.plot(kind='barh', color='lightgreen')
    plt.xlabel("Number of Papers")
    plt.ylabel("Journal")
    plt.title("Top 10 Journals Publishing COVID-19 Research")
    plt.gca().invert_yaxis()
    plt.show()

# ---------------------------
# Most frequent words in titles
# ---------------------------
all_titles = " ".join(df['title'].dropna()).lower()
words = re.findall(r'\b\w+\b', all_titles)
word_counts = Counter(words)
most_common_words = word_counts.most_common(20)
print("\n20 Most Common Words in Titles:\n", most_common_words)


# Count papers per source
source_counts = df['source_x'].value_counts()
print(source_counts)

#Ploting the Horizontal plot of paper counts by source
plt.figure(figsize=(8,5))
source_counts.plot(kind='barh', color='coral')
plt.xlabel("Number of Papers")
plt.ylabel("Source")
plt.title("Distribution of COVID-19 Papers by Source")
plt.gca().invert_yaxis()  # highest count on top
plt.show()

#Streamlit_App

# App title
st.title("COVID-19 Research Explorer")

# App description
st.write("This is a simple Streamlit app to explore the CORD-19 dataset.You can visualize the number of papers per year, top journals, and more.")

#Title and Description
st.title("COVID-19 Research Explorer")
st.write("Explore the CORD-19 dataset interactively: paper counts, journals, and popular keywords in titles.")

#Add a year slider
min_year = int(df['pub_year'].min())
max_year = int(df['pub_year'].max())

selected_year = st.slider(
    "Select publication year:",
    min_year, max_year,
    (min_year, max_year)  # default range
)

# Filter dataframe based on slider
df_year_filtered = df[(df['pub_year'] >= selected_year[0]) & (df['pub_year'] <= selected_year[1])]
st.write(f"Showing papers from {selected_year[0]} to {selected_year[1]}")
st.dataframe(df_year_filtered[['title', 'journal', 'pub_year']].head(10))

# Example: papers per year bar chart
fig, ax = plt.subplots(figsize=(10,5))
papers_per_year.plot(kind='bar', color='skyblue', ax=ax)
ax.set_xlabel("Publication Year")
ax.set_ylabel("Number of Papers")
ax.set_title("COVID-19 Papers by Publication Year")

# Display in Streamlit
st.pyplot(fig)

# Generate WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)

# Display in Streamlit
st.image(wordcloud.to_array(), use_container_width=True)

