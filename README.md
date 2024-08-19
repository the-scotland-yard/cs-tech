# 기술면접 & CS & 알고리즘 학습 스터디

<br>

### 스터디 소개

---

**스터디 구성원**

| [김지용](https://github.com/ssafyjiyong) | [오유진](https://github.com/OHNEUL1999) | [이민규](https://github.com/leeminkyu1212) | [최성호](https://github.com/seonghoho) |
|:---:|:---:|:---:|:---:|
| <img alt="지용" src="https://github.com/ssafyjiyong.png" width="230" height="100%"/> | <img alt="유진" src="https://github.com/OHNEUL1999.png" width="230" height="100%"/> | <img alt="민규" src="https://github.com/leeminkyu1212.png" width="230" height="100%"/> | <img alt="성호" src="https://github.com/seonghoho.png" width="230" height="100%"/> |

<br>

**날짜** : 매주 수요일 온라인 21:00 ~ 23:00

**목표**

- 매주 지식 공유 세션을 통한 발표 및 면접 능력 향상
- 주기적인 학습 내용 공유로 CS 지식 향상
- 꾸준한 알고리즘 풀이를 통한 SW 문제 해결 능력 향상

<br>

### 스터디 진행 방식

--- 매주 수요일 밤 21:00 시작

**스터디 준비**

1. 각자 선정한 주제를 바탕으로 발표 준비 (10분 내외)
2. 주제는 일요일 자정 전까지 공유
3. 발표 자료는 회의 전까지 레포지토리에 푸시
4. 알고리즘 문제 풀이는 당일 문제 랜덤 선정
5. 매일 공부한 내용 공유
   
```
#연속풀이날 yyyymmdd (day)
1. 알고리즘 1문제
 백준 #12345 문제이름 문제풀이법
1. 공부한 내용 & 오늘 한 일  요약

https://github.com/***
```
---
<br>

**스터디 당일**
<br>

| 시간 | 진행 |
|:--:|:--:|
| 21:00 ~ 22:00 | CS 발표 및 지식 공유 |
| 22:00 ~ 23:00 | 알고리즘 문제 풀이 및 풀이방법 공유 |



<br>

### Commit & PR Convention

---

**폴더 및 파일 구조**

1. 발표자는 cs-study, 기술면접대비자는 tech-interview week{00}폴더 하위에 자신의 github-id로 폴더를 생성합니다.
2. 매주 제출할 파일들을 해당 폴더에 업로드 합니다.
3. 닉네임 폴더 하위 구조는 자유롭게 구성해도 무방합니다. (이미지 추가 등 가능)
   - 전체적인 자료를 정리한 md 파일이 꼭 하나는 필요합니다. (초안 피드백용/자료체크용)

<br>


     
     
     cs-study
     ├── topic.md
     ├── week01
     │   ├── {cs-study-topic-1}
     │   └── {cs-study-topic-2}
     └── week02
         ├── {cs-study-topic-3}
         │     └── 이주제로발표합니다.md
         └── {cs-study-topic-4}
               ├── 메인피드백을받을.md
               └── 자유로운업로드방식.ppt



<br>

**Commit Message Convention**

*임의의 커밋tag를 활용합니다.*

|             | 설명            |
| ----------- |---------------|
| feat     | 자료 제출 / 내용 추가 |
| fix      | 틀린 부분 수정      |
| chore    | 폴더 구조 수정      |
| merge    | merge         |

<br>

*커밋 구조*

```
feat(week00):{자신이 고른 주제}-{초안/수정/보완/추가}
- {구체적인 설명(옵션)}
```

<br>

*커밋 예시*

```
feat(week01):네트워크7계층-추가
- 계층 별 개념 설명 추가
- 계층 분리 방식 이론 단점 추가
```

<br>

