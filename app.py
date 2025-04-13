import streamlit as st
import numpy as np
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

# Page configuration
st.set_page_config(page_title="🎬 Netflix Data Explorer", layout="wide", initial_sidebar_state="expanded")

# 🔒 Hide top-right menu & bottom-right "Manage app"
hide_streamlit_style = """
    <style>
        /* Hide Streamlit's top-right hamburger menu and Share button */
        header, .stActionButton, .st-emotion-cache-18ni7ap, .st-emotion-cache-1v0mbdj {
            visibility: hidden;
        }
        footer, ._terminalResizable_rix23_1{
            visibility: hidden;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Title Section
st.markdown("<h1 style='text-align: center; color: #e50914;'>🎬 Netflix Movie Data Analysis Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")

# Load dataset
df = pd.read_csv("./data/mymoviedb.csv", lineterminator="\n")

# Clean 'Vote_Count' and 'Vote_Average'
df['Vote_Count'] = df['Vote_Count'].astype(str).str.replace(',', '').str.strip()
df['Vote_Count'] = pd.to_numeric(df['Vote_Count'], errors='coerce').astype('Int64')
df['Vote_Average'] = df['Vote_Average'].astype(str).str.replace(',', '').str.strip()
df['Vote_Average'] = pd.to_numeric(df['Vote_Average'], errors='coerce').astype('float64')

# Convert 'Release_Date' to Year
df['Release_Date'] = pd.to_datetime(df['Release_Date'], format="%d-%m-%Y", errors='coerce')
df['Release_Date'] = df['Release_Date'].dt.year.astype("Int64")

# Drop unnecessary columns
df.drop(['Overview', 'Original_Language', 'Poster_Url\r'], axis=1, inplace=True)

# Categorize Vote_Average
def categorize_col(df, col, labels):
    stats = df[col].describe()
    edges = [stats['min'], stats['25%'], stats['50%'], stats['75%'], stats['max']]
    df[col] = pd.cut(df[col], bins=edges, labels=labels, include_lowest=True, duplicates='drop')
    return df

labels = ['Not Popular', 'Below Average', 'Average', 'Popular']
categorize_col(df, 'Vote_Average', labels)

# Clean Genre
df.dropna(inplace=True)
df['Genre'] = df['Genre'].str.split(", ")
df = df.explode('Genre').reset_index(drop=True)
df['Genre'] = df['Genre'].astype('category')

# 📊 Visualizations
st.markdown("## 📊 Exploratory Data Analysis")
sns.set_style("whitegrid")

st.markdown("### 🎭 Most Frequent Genres")
fig1 = sns.catplot(y='Genre', data=df, kind='count', order=df['Genre'].value_counts().index, color='#e50914', height=5, aspect=1.5)
fig1.set_axis_labels("Count", "Genre")
st.pyplot(fig1)

st.markdown("### ⭐ Vote Average Distribution")
fig2 = sns.catplot(y='Vote_Average', data=df, kind='count', order=df['Vote_Average'].value_counts().index, color='#f5c518', height=5, aspect=1.5)
fig2.set_axis_labels("Count", "Vote Category")
st.pyplot(fig2)

st.markdown("### 🎯 Movie Popularity Highlights")

st.success("🎖️ Highest Popularity Movie")
st.dataframe(df[df['Popularity'] == df['Popularity'].max()], use_container_width=True)

st.error("📉 Lowest Popularity Movie")
st.dataframe(df[df['Popularity'] == df['Popularity'].min()], use_container_width=True)

# Yearly Distribution
st.markdown("### 🎬 Release Year Distribution")
fig3, ax = plt.subplots()
df['Release_Date'].hist(ax=ax, color='#66c2a5', bins=20)
ax.set_title("Number of Movies Released per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Movie Count")
st.pyplot(fig3)

st.markdown("---")
st.markdown("<center><sub>Made with ❤️ by Dipankar | Powered by Streamlit</sub></center>", unsafe_allow_html=True)
