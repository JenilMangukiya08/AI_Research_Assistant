import streamlit as st
import pandas as pd
import json

with open("logs.json","r") as f:
    logs = json.load(f)

df = pd.DataFrame(logs)

st.title("Research Assistant")

st.metric("Total Runs", len(df))

st.metric("Average Latency", round(df["latency"].mean(),2))

st.dataframe(df)

st.bar_chart(df["latency"])

st.subheader("LangSmith")

st.markdown(
    "[Open LangSmith Project](https://smith.langchain.com/)",
)