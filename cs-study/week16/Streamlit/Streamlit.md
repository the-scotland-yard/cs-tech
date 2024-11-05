# Streamlit

- [Streamlit](#streamlit)
  - [핵심 특징](#핵심-특징)
  - [주요 장점](#주요-장점)
  - [사용하기](#사용하기)
    - [설치 및 실행](#설치-및-실행)
    - [기본 사용](#기본-사용)
    - [컴포넌트 섹션](#컴포넌트-섹션)
    - [레이아웃](#레이아웃)
    - [with pandas : 간단한 데이터 분석 대시보드](#with-pandas--간단한-데이터-분석-대시보드)
  - [Deploy](#deploy)
    - [Streamlit Cloud 배포](#streamlit-cloud-배포)
    - [Docker 배포](#docker-배포)
  - [Reference](#reference)

데이터 사이언스와 머신러닝 프로젝트를 위한 오픈소스 Python 웹 프레임워크

## 핵심 특징

- 순수 Python 코드만으로 웹 앱 개발 가능
- 실시간 데이터 시각화 지원
- 간단한 UI 컴포넌트 제공 (버튼, 슬라이더, 입력폼 등)
- Hot-reloading 지원 (코드 수정시 자동 새로고침)

## 주요 장점

- 매우 낮은 진입장벽
- 빠른 프로토타이핑 가능
- 데이터 사이언티스트 친화적
- 풍부한 위젯과 플러그인 생태계

## 사용하기

### 설치 및 실행

```bash
pip install streamlit

streamlit run app.py
```

### 기본 사용

```python
import streamlit as st

# 기본 텍스트 요소
st.title('Streamlit 시작하기')
st.header('이것은 헤더입니다')
st.subheader('이것은 서브헤더입니다')
st.text('일반 텍스트입니다')
st.markdown('**마크다운**을 사용할 수 있습니다')

# 데이터 표시
import pandas as pd
df = pd.DataFrame({
    '이름': ['John', 'Mary', 'Bob'],
    '나이': [25, 30, 35]
})
st.dataframe(df)
```

### 컴포넌트 섹션

```python
# 입력 위젯
name = st.text_input('이름을 입력하세요')
age = st.number_input('나이를 입력하세요', min_value=0, max_value=120)
is_happy = st.checkbox('행복한가요?')

# 선택 위젯
option = st.selectbox(
    '좋아하는 색상을 선택하세요',
    ['빨강', '파랑', '초록']
)

# 파일 업로드
uploaded_file = st.file_uploader("파일을 선택하세요")
```

### 레이아웃

```python
# 컬럼 레이아웃
col1, col2 = st.columns(2)
with col1:
    st.header("첫번째 컬럼")
    st.write("여기는 왼쪽 컬럼입니다")
with col2:
    st.header("두번째 컬럼")
    st.write("여기는 오른쪽 컬럼입니다")

# 사이드바
with st.sidebar:
    st.header("사이드바")
    st.write("사이드바 내용")
```

### with pandas : 간단한 데이터 분석 대시보드

```python
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
```

## Deploy

### Streamlit Cloud 배포

1. GitHub에 코드 푸시
2. Streamlit Cloud (https://streamlit.io/cloud) 접속
3. "New app" 클릭
4. GitHub 저장소 선택
5. 배포 설정 구성
6. 배포 완료

### Docker 배포

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD streamlit run app.py
```

## Reference

- [Streamlit 공식 문서](https://streamlit.io/)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Components](https://streamlit.io/components)
- [Streamlit Forum](https://discuss.streamlit.io/)
- [Streamlit GitHub](https://github.com/streamlit/streamlit)
