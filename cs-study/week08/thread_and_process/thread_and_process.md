# 멀티스레드와 멀티프로세스

## 1. 멀티프로세스의 개념

- 프로세스: 운영체제에서 실행되는 독립적인 프로그램 단위
- 각 프로세스는 독립적인 메모리 공간을 가지며, 서로 간섭 없이 실행
- 멀티프로세스: 여러 개의 프로세스를 동시에 실행하는 것

## 2. 멀티스레드의 개념

- 스레드: 프로세스 내에서 실행되는 작업 단위
- 여러 스레드는 같은 메모리 공간을 공유하며, 데이터 교환과 자원 공유가 용이
- 멀티스레드: 하나의 프로세스 내에서 여러 스레드를 동시에 실행하는 것

### 1.1. 멀티프로세스의 일상 사례

- **웹 브라우저**
  - 각 탭을 별도의 프로세스로 실행하여, 한 탭에서 오류가 발생해도 다른 탭에 영향을 미치지 않도록 함.
  
- **운영체제**
  - 여러 애플리케이션이 동시에 실행될 때, 각각 별도의 프로세스로 관리함.
  
- **서버 애플리케이션**
  - 웹 서버나 데이터베이스 서버가 각 클라이언트 요청을 별도의 프로세스로 처리하여 독립성을 유지함.


### 2.1. 멀티스레드의 일상 사례

- **웹 브라우저**
  - 웹 페이지 로딩 시, 이미지 다운로드, 텍스트 렌더링, 자바스크립트 실행 등이 별도의 스레드로 동시에 처리됨.
  
- **게임**
  - 렌더링, 물리 연산, 오디오 처리, 네트워크 통신 등이 각각의 스레드에서 동시에 수행됨.
  
- **채팅 애플리케이션**
  - 메시지 수신, 전송, UI 업데이트 등을 각각의 스레드에서 처리하여 반응성을 유지함.

## 3. 멀티프로세스와 멀티스레드의 비교

| **특징**           | **멀티프로세스**                  | **멀티스레드**                                  |
|-------------------|---------------------------------|-------------------------------------------------|
| **메모리 공간**    | 독립적인 메모리 공간            | 동일한 메모리 공간 공유                        |
| **자원 소비**      | 높은 메모리 소비                | 낮은 메모리 소비                                |
| **통신 비용**      | 높은 IPC 비용                   | 낮은 통신 비용 (공유 메모리 이용)               |
| **안정성**         | 한 프로세스 실패 시 다른 프로세스에 영향 없음 | 한 스레드 실패 시 전체 프로세스에 영향        |
| **생성 및 전환 비용** | 상대적으로 높음                  | 상대적으로 낮음                                |
| **동기화**         | 비교적 쉬움 (독립된 메모리)      | 복잡함 (공유 메모리로 인한 동기화 필요)         |
| **적합한 용도**    | 독립적인 작업, 보안이 중요한 작업, 안정성이 중요한 경우 | 높은 성능이 요구되며, 자원 공유가 필요한 경우 |

## 4. 게임에서 멀티프로세스와 멀티스레드의 활용 차이

### 4.1. 멀티프로세스로 처리할 경우의 문제점

- **자원 공유의 어려움**
  - 프로세스 간 메모리 공간이 분리되어 있어, 데이터 공유가 복잡하고 비효율적임.
  
- **성능 저하**
  - 프로세스 간 컨텍스트 스위칭 비용이 높아, 성능이 저하될 수 있음.
  
- **관리의 복잡성**
  - 프로세스 간의 상태 관리, 종료 처리, 예외 처리 등이 복잡해짐.
  
- **디버깅의 어려움**
  - 여러 프로세스가 연관된 작업을 디버깅하기가 어려워짐.

## 5. 결론

- **멀티프로세스**는 안정성과 독립성이 필요한 경우에 유리하며, 주로 독립적인 작업이 필요할 때 사용된다.
- **멀티스레드**는 자원 공유와 성능 최적화가 필요한 경우에 적합하며, 서로 연관된 작업을 효율적으로 처리할 수 있다.
- 게임과 같은 애플리케이션에서는 멀티스레드를 사용하여 성능을 최적화하고, 사용자 경험을 향상시킨다.
