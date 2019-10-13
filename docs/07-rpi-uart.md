https://www.raspberrypi.org/documentation/configuration/uart.md

Raspberry Pi에 사용된 SoC에는 PL011과 미니 UART의 두 가지 내장 UART가 있다.
두 가지 UART는 다른 하드웨어 블록을 사용하여 구현되므로 약간 다른 특성을 가진다.
그러나 둘 다 3.3V 장치이므로 전압 레벨 주의가 필요하다.

무선/블루투스 모듈이 장착된 라즈베리파이에서 PL011 UART는 블루투스 모듈에 연결되어 있다.
미니 UART는 기본 UART로 Linux 콘솔로 사용된다.
(그 이전 모델은 PL011이 기본 UART)

/dev/ttyS0는 미니 UART
/dev/AMA0는 PL011

* 심볼릭 링크
/dev/serial0 : 항상 1차 UART 참조
/dev/serial1 : 2차 UART 가능

미니 UART 전송속도는 VC4 GPU상의 VPU 핵심 주파수와 연결된다.

기본으로 미니 UART를 Primary UART를 사용하도록 선택하면 비활성화된다.
이를 활성화시키기 위해서는 'config.txt'에 'enable_uart=1'을 추가해야 한다.
이렇게 하면 Core 주파수를 250MHz로 고정시킨다.

미니 UART를 블루투스 컨트롤러에 연결한 것과 같이 기본 UART로 사용하지 않을 때는 'config.txt'에 'core_freq=250'을 추가해야 한다.
그렇지 않으면 미니 UART는 동작하지 않는다.

앞서와 같이 기본 UART(serial0)는 리눅스 콘솔에 할당된다.
이를 다를 용도로 사용하려면 기본 동작을 변경해야 한다.

* 수동 변경
'/boot/cmdline.txt'에서 콘솔 항목을 나타내는 'serial0' 장치를 찾아 속도 설정을 포함하여 장치를 주석처리한다.
<-- Console로 사용시 필요하지 않음

