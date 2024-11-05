# 기본 사용
import streamlit as st

## 기본 텍스트 요소
st.title('Streamlit 시작하기')
st.header('이것은 헤더입니다')
st.subheader('이것은 서브헤더입니다')
st.text('일반 텍스트입니다')
st.markdown('**마크다운**을 사용할 수 있습니다')

## 데이터 표시
import pandas as pd
df = pd.DataFrame({
    '이름': ['John', 'Mary', 'Bob'],
    '나이': [25, 30, 35]
})
st.dataframe(df)


###############################
# 컴포넌트

## 입력 위젯
name = st.text_input('이름을 입력하세요')
age = st.number_input('나이를 입력하세요', min_value=0, max_value=120)
is_happy = st.checkbox('행복한가요?')

## 선택 위젯
option = st.selectbox(
    '좋아하는 색상을 선택하세요',
    ['빨강', '파랑', '초록']
)

## 파일 업로드
uploaded_file = st.file_uploader("파일을 선택하세요")

###############################
# 레이아웃

## 컬럼 레이아웃
col1, col2 = st.columns(2)
with col1:
    st.header("첫번째 컬럼")
    st.write("여기는 왼쪽 컬럼입니다")
with col2:
    st.header("두번째 컬럼")
    st.write("여기는 오른쪽 컬럼입니다")

## 사이드바
with st.sidebar:
    st.header("사이드바")
    st.write("사이드바 내용")
