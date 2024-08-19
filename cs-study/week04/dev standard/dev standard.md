# 개발 표준 Development Standard
코드의 가독성, 유지보수성, 안정성, 일관성을 높이기 위해 정의된 규칙과 지침
각 언어마다 특성에 맞는 개발 표준이 있으며, 이를 통해 높은 품질의 소프트웨어를 개발할 수 있다.

개발 표준 ≈ 개발 스타일 가이드

## 언어별 개발 표준
<details>
<summary>Python</summary>
<div markdown="1">

[PEP8 Style Guide](https://peps.python.org/pep-0008/)

```
pip install autopep8
```
^^^ autopep8을 설치하여 자동으로 코딩 컨벤션을 따르도록 할 수 있다.

---
코드 레이아웃:

    들여쓰기: 4칸 스페이스 사용.
    최대 줄 길이: 79자.
    함수와 클래스 정의 사이에는 두 줄의 빈 줄 삽입.
    클래스 내부의 메서드 정의 사이에는 한 줄의 빈 줄 삽입.
네이밍 규칙:

    함수와 변수: lowercase_with_underscores.
    클래스 이름: CapWords (PascalCase).
    상수: UPPERCASE_WITH_UNDERSCORES.
문자열:

    작은 따옴표(') 또는 큰 따옴표(")를 사용하되 일관성 유지.
    Docstring은 삼중 따옴표(""" """) 사용.
임포트:

    한 줄에 하나의 모듈만 임포트.
    표준 라이브러리, 서드파티 라이브러리, 로컬 모듈의 순서로 임포트.
기타 규칙:

    불필요한 공백 피하기.
    비교 연산자는 상수 앞에 사용하지 않음.
    예외 처리는 명확하고 구체적으로 작성.

</div>
</details>

<details>
<summary>C</summary>
<div markdown="1">

[Misra C](https://misra.org.uk/publications/)
[CERT C](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard)

#### Misra C
코딩 규칙:

    위험한 함수 사용 금지: gets(), strcpy() 등.
    전역 변수 사용 최소화.
    매직 넘버 사용 금지: 의미 있는 상수로 대체.
    포인터 연산을 최소화하고 명확하게 사용할 것.
안전한 코드 작성:

    모든 변수는 초기화할 것.
    메모리 누수 방지: 동적 할당된 메모리는 반드시 해제.
    배열 범위를 벗어난 접근 금지.
    타입 변환은 명시적으로 할 것.
제어 구조:

    단일 입출력 구조를 사용: 한 함수 내 여러 개의 return 문 금지.
    모든 if 문에 else를 추가하여 예외 상황을 처리.
    반복문은 명확하고 제한된 범위 내에서 사용할 것.
네이밍 규칙:

    변수 및 함수: lower_case_with_underscores.
    상수: UPPER_CASE_WITH_UNDERSCORES.
    타입 및 구조체: CapWords.

</div>
</details>

<details>
<summary>C++</summary>
<div markdown="1">

[Misra C++](https://misra.org.uk/publications/)
[Cert C++](https://wiki.sei.cmu.edu/confluence/pages/viewpage.action?pageId=88046682)
[Google C++ Style Guide]()

##### Google C++ Style Guide
코드 레이아웃:

    들여쓰기: 2칸 스페이스 사용.
    최대 줄 길이: 80자.
    네임스페이스, 클래스, 함수 정의 사이에 한 줄의 빈 줄 삽입.
네이밍 규칙:

    변수 및 함수: mixedCase 또는 under_score.
    클래스 이름: CapWords.
    상수: kCamelCase.
문자열:

    작은 따옴표(') 또는 큰 따옴표(")를 사용하되 일관성 유지.
    Raw 문자열 리터럴 사용을 권장: R"delimiter(raw_characters)delimiter".
헤더 파일:

    헤더 가드 사용: #ifndef, #define, #endif.
    필요한 헤더 파일만 포함.
    전방 선언을 사용하여 헤더 파일 포함 최소화.
기타 규칙:

    자동 타입 추론(auto) 사용을 권장.
    스마트 포인터(std::shared_ptr, std::unique_ptr) 사용.
    C++11/14/17의 최신 기능을 활용.

</div>
</details>

## 후기
지난 주의 개발 문서에 이어, 개발자가 인지해야할 기본적인 부분들을 살펴보았다. 학습 목적은 "기본적인 부분을 잘 지킬 수 있는 개발자가 되기 위함"이다.
