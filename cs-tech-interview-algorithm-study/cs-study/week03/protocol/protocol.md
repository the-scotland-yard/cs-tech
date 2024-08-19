# 프로토콜
컴퓨터 내부에서, 또는 컴퓨터 사이에서 데이터의 교환 방식을 정의하는 규칙 체계

## 프로토콜 정의 기관
- ISO(International Organization for Standardization)
- EIA(Electronic Industries Organization)
- IEEE(Institute of Electrical and Electronic Engineers)
- CCITT(Consultative Committee for International Telegraph and Telephone)
- IAB(Internet Activities Board)

## 유명한 프로토콜들
### HTTP - Hyper Text Transfer Protocol

### HTTPS - Hyper Text Transfer Protocol Secure

### Telnet - TErminaL NETwork

### SSH - Secure Shell

### SSL - Secure Socket Layer

## Bluetooth Low Energy Protocol
![BLE Stack](../protocol/BLE%20Stack.png)

- Physical: 2.4 GHz ISM 대역에서 1 Mbps의 속도로 패킷 송수신 역할 (실제 Bluetooth Analog Signal과 통신할 수 있는 회로가 구성되어 있음)

- LL (Link Layer): 5가지의 RF 상태 제어 (standby, advertising, scanning, initiating, connected) 및 디바이스의 Role 정의

- HCI (Host Controller Interface): Host 영역과 Controller 영역의 Interface 역할

- L2CAP (Logical Link Control and Adaptation Protocol): 데이터 encapulation service 제공

- SM (Security Manager): paring and key distributuiion 방법 정의 및 인증과 보안에 사용

- ATT (Attribute Protocol): 다른 기기로 'attribute'라는 데이터 노출 및 데이터 교환을 위한 클라이언트, 서버 프로토콜 정의

- GAP (Generic Access Protocl): 장치 간의 paring과 bonding 사용을 통해 장치 간 인터페이스 역할

- GATT (Generic Attribute Profile): ATT를 이용하는 sub-procedure를 정의하는 프레임워크, ATT 영역에서 읽어 들인 서비스의 기능 수행

### GATT - General Attribute Profile
GATT는 디바이스들이 데이터를 발견하고 읽고, 쓰는 것을 가능하게 하는 기조적인 데이터 모델과 절차를 정의
**디바이스 간의 Low-level에서의 모든 인터렉션을 정의하는 GAP와는 달리 GATT는 오직 데이터의 포맷 및 전달에 대해서만 처리한다.**

#### GATT Role
- Client (Master): Central 역할을 했던 장치에서 Client역할을 하며, 연결 과정에서 연결 간격을 조정하고 Service 항목을 통해 데이터 요청의 기능을 수행
- Server (Slave): Peripheral 역할을 했던 장치에서 Server역할을 하며, 연결 과정에서 초기 연결 간격을 명시하며 Client에서 보낸 연결 간격 조정 값의 적용 여부를 판단하고 Client의 데이터 요청에 대한 응답 기능을 수행

==> GATT는 BLE의 대표적인 프로토콜이다.


참고

https://igotit.tistory.com/entry/BLE-Protocol-Stack-Bluetooth-Low-Energy
