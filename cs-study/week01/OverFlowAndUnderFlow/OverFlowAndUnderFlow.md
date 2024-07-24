# Overflow와 Underflow
## 개념 정의
- 오버플로우 (Overflow): 자료구조나 변수의 저장 용량을 초과하여 더 이상의 데이터가 저장되지 못하는 상황
- 언더플로우 (Underflow): 자료구조나 변수에서 데이터가 존재하지 않는데 데이터를 삭제하려는 상황

### 자료구조에서의 예시 - 스택(Stack)
#### 스택의 최대 크기를 초과하여 데이터를 삽입하려 할 때 Overflow 발생
```python
def recursive_function(n):
    if n > 0:
        recursive_function(n - 1)
    else:
        pass

recursive_function(10000)
```
#### 빈 스택에서 pop 연산을 시도할 때 Underflow 발생
```python
stack = []
try:
    stack.pop()
except IndexError as e:
    print("스택 언더플로우 발생:", e)
```

### 오버플로우와 언더플로우 해결 방안
1. 크기 조절
- 자료구조의 크기를 동적으로 조절
- 예시: deque를 사용하여 큐의 크기를 동적으로 조절
2. 시전 검사
- 자료구조에서 데이터를 삽입하거나 삭제하기 전에 상태를 검사
- 예시: if stack: 구문으로 스택이 비어 있는지 확인
3. 예외 처리
- 예외 처리 구문을 사용하여 오류를 처리
- 예시: try-except 구문 사용
4. 테스트와 검증
- 다양한 경계 조건을 테스트하여 자료구조가 예상대로 동작하는지 확인