## JS Array에 대한 고찰
 

자바스크립트에서 Object, 객체는 유일한 변경 가능한 값이고,  key, value 속성으로 구성되어 있습니다. 또한 key 값은 string, symbol 타입이 될 수 있습니다.

사실 자바스크립트에서 Function , 함수 또한 객체로 구성되어 있고, Array, 배열 또한 객체 형식입니다.

배열은 이름과 인덱스를 사용하여 참조하는 값들의 순서가 있는 목록입니다.

하지만, 자바스크립트는 명시적인 배열 데이터 형식을 가지고 있지 않고, 객체 형식으로 정의되어 있어, 사용할 수 있습니다.

```jsx
const list = [2, 4, 6, 7]
list[0] = 2
```

기본적으로 위 코드로 많이 보셨을 겁니다.  

0번째 인덱스에 2가 할당되어 있다고 알고 있겠지만, 사실 아래의 코드와 같다고 볼 수 있습니다.

```jsx
// Object
const list = {
  0: 2,
  1: 4,
  2: 6,
  3: 7,
};
```

배열이 사실 객체로 제작되어 있기 때문에, index로 접근해 값을 삭제하게 되면 value값만 삭제되어 undefined가 저장됩니다.

슬롯에 undefined가 저장된 빈 슬롯이 존재하는 배열은 `희소 배열` 이라고 합니다.

```jsx

// 배열에 숫자 하나를 할당하면 생성자로 실행됩니다.
const arr = Array(5) // [undefined, undefined, undefined, undefined, undefined]

// length를 직접 설정하면 배열을 늘릴 수 있습니다.
const arr1 = [1,2]
arr1.length = 5 // [1, 2, undefined, undefined, undefined]

const arr2 = [1, 2, 3, 4, 5]
delete arr2[2] // [1, 2, undefined , 4, 5]
```

배열의 값을 삭제한 뒤, 

```jsx
let lst = Array(1, 2, 3, 4, 5);
delete lst[2];
console.log(lst);

for (let i = 0; i < lst.length; i++) {
  console.log(lst[i]);
}

// [ 1, 2, <1 empty item>, 4, 5 ]
// 1
// 2
// undefined
// 4
// 5

```

## 요약!

JS에서의 Array는 list형태를 한, index값을 key값으로 가지고 value를 가지는 Object, 객체라는 것이다.