import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

st.title("☀️ Solar Data Dashboard - Cross-Country Comparison")

@st.cache_data
def load_data():
    togo = pd.read_csv("data/togo_clean.csv")
    benin = pd.read_csv("data/benin_clean.csv")
    sierra_leone = pd.read_csv("data/sierra_leone_clean.csv")

    togo["Country"] = "Togo"
    benin["Country"] = "Benin"
    sierra_leone["Country"] = "Sierra Leone"

    return pd.concat([togo, benin, sierra_leone], ignore_index=True)

df = load_data()

selected_countries = st.sidebar.multiselect(
    "Select Countries", options=df["Country"].unique(), default=df["Country"].unique()
)

filtered_df = df[df["Country"].isin(selected_countries)]

metric = st.selectbox("Select Metric to Plot", options=["GHI", "DNI", "DHI"])

st.subheader(f"{metric} Distribution by Country")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=filtered_df, x="Country", y=metric, palette="Set2", ax=ax)
st.pyplot(fig)

st.subheader(f"Average {metric} by Country")
mean_data = filtered_df.groupby("Country")[metric].mean().sort_values()
st.bar_chart(mean_data)
print('Made by Ermias')