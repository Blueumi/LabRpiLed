# rpirgbled-01.py
# 1초마다 R, G, B 를 순차적으로 On 시킨다.
import RPi.GPIO as GPIO
import time

# RGB 핀 번호
PIN_R = 10  # pin seq:10, no:19
PIN_G = 9   # pin seq:11, no:21
PIN_B = 11  # pin seq:12, no:23

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED 공통 핀이 GND인 경우에는 ON이 HIGH, OFF가 LOW
# LED 공통 핀이 +인 경우에는 ON이 LOW, OFF가 HIGH

# LED는 공통핀이 + 인 경우
LED_ON = GPIO.LOW
LED_OFF = GPIO.HIGH

# LED는 공통핀이 GND 인 경우
#LED_ON = GPIO.HIGH
#LED_OFF = GPIO.LOW

# LED 핀 속성 정의
GPIO.setup(PIN_R, GPIO.OUT)
GPIO.setup(PIN_G, GPIO.OUT)
GPIO.setup(PIN_B, GPIO.OUT)

# LED 핀 초기 신호 설정
GPIO.output(PIN_R, LED_OFF)
GPIO.output(PIN_G, LED_OFF)
GPIO.output(PIN_B, LED_OFF)

# 타이틀 메시지 출력
print('> Red, Green, Blue led를 1초마다 번갈아 가면서 On 시킨다.')

try:
    led_index = -1;        # 처음에는 On된 LED가 없다.

    while True:
        # LED 위치를 지정한다.
        # led_index: 0-Red, 1-Green, 2-Blue
        led_index += 1     # python에서는 ++ 미지원
        if led_index > 2:
            led_index = 0

        # 지정된 위치의 LED만 On 시킨다.
        if led_index = 0:
            # RED Led만 On, 나머지는 Off
            GPIO.output(PIN_R, LED_ON)
            GPIO.output(PIN_G, LED_OFF)
            GPIO.output(PIN_B, LED_OFF)
            print('red on')
        elif led_index = 1:
            # GREEN Led만 On, 나머지는 Off
            GPIO.output(PIN_R, LED_OFF)
            GPIO.output(PIN_G, LED_ON)
            GPIO.output(PIN_B, LED_OFF)
            print('green on')
        elif led_index = 2:
            # BLUE Led만 On, 나머지는 Off
            GPIO.output(PIN_R, LED_OFF)
            GPIO.output(PIN_G, LED_OFF)
            GPIO.output(PIN_B, LED_ON)
            print('blue on')
        else:
            # 여기에 오면 오류인 셈이지만 예시용으로.
            GPIO.output(PIN_R, LED_OFF)
            GPIO.output(PIN_G, LED_OFF)
            GPIO.output(PIN_B, LED_OFF)
            print('all led off')

        time.sleep(1.0)   # 1초 대기

except KeyboardInterrupt:       # !중요! CTRL+C 로 종료
    GPIO.cleanup()
