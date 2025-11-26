import streamlit as st
import pandas as pd
import base64
from io import BytesIO

st.title("🗂️ 전체 분실물")

df = pd.read_csv("data/lost_items.csv")

for _, row in df.iterrows():
    st.subheader(f"📌 {row['name']} ({row['floor']})")
    st.write(f"📍 {row['place']} / 📅 {row['date']}")
    img = base64.b64decode(row["image"])
    st.image(img, width=250)
    st.markdown("---")
