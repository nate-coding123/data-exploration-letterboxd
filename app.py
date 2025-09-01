import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your processed data (assumes you ran run.sh or scraped already)
df = pd.read_csv("analysis/results/diary.csv")

st.title("Letterboxd Data Exploration")

st.write("### Raw Data")
st.dataframe(df.head())

st.write("### Ratings Distribution")
fig, ax = plt.subplots()
sns.histplot(df["rating"], bins=10, kde=False, ax=ax)
st.pyplot(fig)

st.write("### Films Watched Over Time")
fig, ax = plt.subplots()
df["date"] = pd.to_datetime(df["date"])
df.groupby(df["date"].dt.to_period("M")).size().plot(ax=ax)
st.pyplot(fig)
