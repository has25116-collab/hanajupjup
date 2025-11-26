import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="하나줍줍", page_icon="🎒")

st.title("🎒 하나고 온라인 분실물함 : 하나줍줍")

st.write("""
하나고 학생들의 분실물을 더 빠르고 정확하게 찾아주는 온라인 분실물함입니다.  
왼쪽 사이드바에서 분실물 업로드, 검색, 최근 게시판, 오래된 분실물, 랭킹을 확인할 수 있어요!
""")

csv_path = Path("data/lost_items.csv")
if not csv_path.exists():
    df = pd.DataFrame(columns=["name", "place", "floor", "date", "image"])
    csv_path.parent.mkdir(exist_ok=True)
    df.to_csv(csv_path, index=False)
