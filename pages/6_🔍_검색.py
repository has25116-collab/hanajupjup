import streamlit as st
import pandas as pd
import base64

st.title("🔍 분실물 검색")

df = pd.read_csv("data/lost_items.csv")

name = st.text_input("물건명 검색")
floor = st.selectbox("층수 검색", ["전체", "지하", "1층", "2층", "3층", "4층"])
place = st.text_input("장소 키워드")

result = df.copy()

if name:
    result = result[result["name"].str.contains(name)]
if place:
    result = result[result["place"].str.contains(place)]
if floor != "전체":
    result = result[result["floor"] == floor]

for _, row in result.iterrows():
    st.subheader(f"{row['name']} ({row['floor']})")
    st.write(f"{row['place']} / {row['date']}")
    img = base64.b64decode(row["image"])
    st.image(img, width=250)
    st.markdown("---")
