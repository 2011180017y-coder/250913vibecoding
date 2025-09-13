import streamlit as st
import pandas as pd
import altair as alt
import os

st.title("MBTI 국가별 분포 시각화")
st.write("각 MBTI 유형에 대해 비율이 가장 높은 상위 10개 국가를 보여줍니다.")

# 기본 파일 경로
default_path = "countriesMBTI_16types.csv"

# 파일 존재 여부 확인
if os.path.exists(default_path):
    df = pd.read_csv(default_path)
    st.success("기본 CSV 파일을 불러왔습니다.")
else:
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("업로드한 파일을 불러왔습니다.")
    else:
        st.warning("CSV 파일이 필요합니다.")
        st.stop()

# 데이터 전처리
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df_melted = df.melt(id_vars=["Country"], var_name="MBTI_Type", value_name="Proportion")

# MBTI 유형별 상위 10개국 추출
top10_df = (
    df_melted.sort_values(by=["MBTI_Type", "Proportion"], ascending=[True, False])
    .groupby("MBTI_Type")
    .head(10)
)

# Altair 그래프 생성
chart = alt.Chart(top10_df).mark_bar().encode(
    x=alt.X("Proportion:Q", title="비율"),
    y=alt.Y("Country:N", sort="-x", title="국가"),
    color="MBTI_Type:N",
    tooltip=["Country", "MBTI_Type", "Proportion"]
).properties(
    width=700,
    height=400,
    title="MBTI 유형별 비율이 가장 높은 국가 Top 10"
).interactive()

# 그래프 출력
st.altair_chart(chart, use_container_width=True)
