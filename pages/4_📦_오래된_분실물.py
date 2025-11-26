import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import base64

st.title("📦 오래된 분실물")

df = pd.read_csv("data/lost_items.csv")

threshold = datetime.now() - timedelta(days=14)
old = df[df["date"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M") < threshold)]

for _, row in old.iterrows():
    st.subheader(row["name"])
    st.write(f"{row['place']} / {row['date']}")
    img = base64.b64decode(row["image"])
    st.image(img, width=250)
    st.markdown("---")
