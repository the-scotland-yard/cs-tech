## **window.requestAnimationFrame()**

이 메서드는 브라우저에게 수행하기 원하는 애니메이션을 알리고 다음 리페인트 바로 전에 브라우저가 애니메이션을 업데이트할 지정된 함수를 호출하도록 요청합니다.

해당 함수는 하나의 프레임일 뿐이므로, 재귀함수를 사용해 한 프레임이 호출된 후에 다음 프레임을 호출하게 적용해야합니다.

## setInterval을 사용하면 안될까?

자바스크립트의 타이머 함수인 setInterval을 사용해서 간격도 조정하면 더 좋지 않냐는 의문이 들 수 있습니다.

우선 이 함수는 시스템이 프레임을 그릴 준비가 되면 애니메이션 프레임을 호출합니다. 실제 화면이 갱신되어 표시되는 주기에 따라 함수를 호출하기 때문에, 자바스크립트가 프레임 시작 시 실행되도록 보장해주어 delay가 발생하지 않습니다.

웹 브라우저의 디스플레이의 주사율에 따라 주사율 만큼 호출합니다.

또한, setInterval은 브라우저의 다른 탭을 보거나, 브라우저가 최소화되어있을 때 계속 타이머가 돌아 리소스 낭비 및 전력 소모를 초래하지만, raf는 페이지가 비활성화되면 화면 그리는 작업도 일시 중지되기 때문에 리소스나 배터리 수명을 낭비하지 않게 됩니다.

## Animation frames queue라니???

![stack-queue](<stack queue.png>)

기본적으로 자바스크립트의 실행 순서나 이벤트 루프 등에 대해 학습할 때 task queue에 대해서는 들어본 경험이 있을 것입니다.

requestAnimationFrame 또한 콜백 함수를 등록하고 비동기 task로 분류하여 처리됩니다. 하지만 task queue가 아닌, animation frame이라는 별도의 queue에서 처리된다는 특징이 있습니다.

requestAnimationFrame 콜백 함수는 Animation frames에 들어가 별도로 처리되어 밀리지 않습니다.

```jsx
const rocket = document.querySelector(".rocket");
const value = document.querySelector(".value");

let yPos = 0;
let rafId;

// 콜백 함수
const render = () => {
  yPos += 2;
  // y 좌표 증가
  rocket.style.transform = `translateY(${-yPos}px)`;
  // 로켓을 위로 올리기
  value.innerHTML = yPos;

  // requestAnimationFrame 종료
  if (yPos >= 500) {
    cancelAnimationFrame(rafId);
    return;
  }

  rafId = requestAnimationFrame(render);
};

requestAnimationFrame(render);
```

```jsx
function animate() {
  requestAnimationFrame(animate);
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;
  renderer.render(scene, camera);
}
animate();
```

위의 코드처럼 재귀형식으로 사용합니다.

requestAnimationFrame은 브라우저 환경에서 제공하는 `Window 객체의 메서드`입니다. 따라서 순수한 JavaScript 내장 함수가 아니라 브라우저 API의 일부입니다.

또한 위에서 설명한 렌더링 루프는 자바스크립트에서의 동작이 아닌, 런타임 환경에서의 동작입니다.

런타임 환경이라고 하면, 크롬의 v8엔진보다 더 큰 범주의, 브라우저 상의 환경을 말합니다.