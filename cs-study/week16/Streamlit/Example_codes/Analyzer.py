import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("데이터 분석 대시보드")
  
    # 파일 업로드
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=['csv'])
  
    if uploaded_file is not None:
        # 데이터 로드
        df = pd.read_csv(uploaded_file)
      
        # 데이터 미리보기
        st.subheader("데이터 미리보기")
        st.dataframe(df.head())
      
        # 기본 통계
        st.subheader("기술 통계량")
        st.write(df.describe())
      
        # 차트
        st.subheader("데이터 시각화")
        fig = px.scatter(df)
        st.plotly_chart(fig)

if __name__ == "__main__":
    main()
