import streamlit as st
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

st.title("Netflix Movie Data Analysis")

df = pd.read_csv("./data/mymoviedb.csv")

st.write("### Sample Data")
st.dataframe(df.head())

st.write("### Vote Average Distribution")
fig, ax = plt.subplots()
sns.countplot(y='Vote_Average', data=df, ax=ax)
st.pyplot(fig)