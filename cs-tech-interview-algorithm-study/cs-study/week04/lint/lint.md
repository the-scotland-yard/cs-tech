# Lint와 Linter에 대해 (feat: ESLint, Prettier)

## 개요

프로젝트를 생성해 개발을 진행하거나, 협업을 진행하다보면 lint라는 것을 한 번씩 들어보셨을 것이라 생각합니다.

누군가 lint에 대해 설명해보라고 했을 때, `코드를 작성할 때의 규칙을 정하기 위한 도구` 라고만 설명하고 그 이외의 것을 설명할 수 없는 저의 모습을 보고, lint에 대해 자세히 학습하는 시간을 가져보려 합니다.

> 린트(lint) 또는 린터(linter)는 소스 코드를 분석하여 프로그램 오류, 버그, 스타일 오류, 의심스러운 구조체에 표시(flag)를 달아놓기 위한 도구들을 가리킨다.[2] 이 용어는 C 언어 소스 코드를 검사하는 유닉스 유틸리티에서 기원한다.[1]
>
> [출처: 위키백과](<https://ko.wikipedia.org/wiki/%EB%A6%B0%ED%8A%B8_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4)>)

## 린트(Lint)와 린터(Linter)

**린트(Lint)** 는 코드에서 잠재적인 오류나 스타일 문제를 찾아내는 `과정`을 의미합니다. 린팅은 코드의 일관성을 유지하고 오류를 사전에 방지하는 데 중요한 역할을 합니다.

**린터(Linter)** 는 린팅 과정을 자동으로 수행해주는 `도구`입니다. 린터는 코드베이스를 분석하여 규칙에 어긋나는 부분을 찾아내고 이를 개발자에게 알려줍니다.

## ESLint와 Prettier

### ESLint

**ESLint**는 JavaScript와 TypeScript 코드의 `린팅을 위한 도구`입니다. ESLint는 다양한 규칙과 플러그인을 통해 `코드 스타일과 잠재적인 오류를 검사`합니다.

### Prettier

**Prettier**는 `코드 포맷팅 도구`입니다. Prettier는 코드의 일관된 형식을 유지하도록 코드를 `자동으로 포맷팅`합니다. Prettier는 규칙이 고정되어 있으며 설정이 단순합니다.

## ESLint와 Prettier의 차이점

**기능적 차이**:

- **ESLint**: 코드 스타일 규칙, 베스트 프랙티스 관련 경고, 오류를 감지합니다. 잠재적 버그를 찾아내고 코드 품질을 향상시키는 데 중점을 둡니다.
- **Prettier**: 코드 포맷팅에 특화되어 있으며, 코드의 일관된 스타일을 유지합니다. 규칙이 엄격하게 고정되어 있어 사용이 간편합니다.

**사용 목적**:

- **ESLint**: 코딩 규칙 준수, 잠재적 오류 탐지, 코드 품질 유지.
- **Prettier**: 코드 포맷팅 일관성 유지.

**설정 및 확장성**:

- **ESLint**: 다양한 플러그인과 규칙을 통해 설정 및 확장 가능.
- **Prettier**: 설정이 단순하며, 일관된 코드 스타일을 강제.

## 함께 사용하는 방법

ESLint와 Prettier를 함께 사용하면 코드 품질과 스타일을 동시에 유지할 수 있습니다. 이 때, ESLint와 Prettier가 충돌하지 않도록 하기 위해서 `eslint-config-prettier`와 `eslint-plugin-prettier` 플러그인을 사용하여 Prettier 규칙을 ESLint에 통합할 수 있습니다.

```bash
npm install eslint prettier eslint-config-prettier eslint-plugin-prettier --save-dev
```

## 참고 링크

- [ESLint 공식 문서](https://eslint.org/docs/user-guide/getting-started)
- [Prettier 공식 문서](https://prettier.io/docs/en/index.html)
- [eslint-config-prettier GitHub 리포지토리](https://github.com/prettier/eslint-config-prettier)
