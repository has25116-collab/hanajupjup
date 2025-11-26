import streamlit as st
import pandas as pd

st.title("🏆 분실물 업로드 랭킹")

df = pd.read_csv("data/lost_items.csv")

df["uploader"] = "학생"  # 단일 사용자이므로 형식적으로만

ranking = df["uploader"].value_counts().reset_index()
ranking.columns = ["사용자", "업로드 수"]

st.table(ranking)
