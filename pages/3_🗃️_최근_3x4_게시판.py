import streamlit as st
import pandas as pd
import base64

st.title("🗃️ 최근 분실물 3×4")

df = pd.read_csv("data/lost_items.csv")
df_recent = df.tail(12).iloc[::-1]

cols = st.columns(4)
i = 0

for _, row in df_recent.iterrows():
    col = cols[i % 4]
    with col:
        st.text(row['name'])
        img = base64.b64decode(row["image"])
        st.image(img, width=120)
    i += 1
