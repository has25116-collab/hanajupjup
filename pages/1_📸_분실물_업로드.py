import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path
import base64
import os

st.title("📸 분실물 업로드")

csv_path = Path("data/lost_items.csv")
df = pd.read_csv(csv_path)

name = st.text_input("물건 이름")
place = st.text_input("발견 장소")
floor = st.selectbox("층수", ["지하", "1층", "2층", "3층", "4층"])
image = st.file_uploader("사진 업로드", type=["jpg", "png"])

if st.button("업로드 하기"):
    if image:
        img_bytes = image.getvalue()
        img_b64 = base64.b64encode(img_bytes).decode()

        new = pd.DataFrame([{
            "name": name,
            "place": place,
            "floor": floor,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "image": img_b64
        }])

        df = pd.concat([df, new], ignore_index=True)
        df.to_csv(csv_path, index=False)
        st.success("업로드 완료!")
    else:
        st.error("사진을 업로드해주세요!")
