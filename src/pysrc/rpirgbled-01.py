# rpirgbled-01.py
# 1초마다 R, G, B 를 순차적으로 On 시킨다.
import RPi.GPIO as GPIO
import time

# RGB 핀 번호
#PIN_R = 10  # pin seq:10, no:19
#PIN_G = 9   # pin seq:11, no:21
#PIN_B = 11  # pin seq:12, no:23
LED_PINS = [ 10, 9, 11 ]    # RGB 핀 번호
PIN_R = LED_PINS[0]         # RED
PIN_G = LED_PINS[1]         # GREEN
PIN_B = LED_PINS[2]         # BLUE

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED 공통 핀이 GND인 경우에는 ON이 HIGH, OFF가 LOW
# LED 공통 핀이 +인 경우에는 ON이 HIGH, OFF가 LOW
# 풀업(Pull-up)인 경우에는 반대

# 현재 테스트용 RGB LED는 공통핀이 +라서 LED가 ON되려면 할당 핀에 LOW 신호를 주어야 한다.
LED_ON = GPIO.LOW
LED_OFF = GPIO.HIGH

# LED 핀 속성 정의 및 초기화
for i in range(0, 3):
    GPIO.setup(LED_PINS[i], GPIO.OUT)
    GPIO.output(LED_PINS[i], LED_OFF)

# leds on
print('> Red, Green, Blue led를 1초마다 On 시킨다.')

try:
    pos_on_led = -1;        # 처음에는 On된 LED가 없다.

    while True:
        # LED 위치를 지정한다.
        pos_on_led += 1     # python에서는 ++ 미지원
        if pos_on_led > 2:
            pos_on_led = 0

        # 지정된 위치의 LED만 On 시킨다.
        for i in range(0, 3):
            if pos_on_led == i:
                GPIO.output(LED_PINS[i], LED_ON)
                if pos_on_led == 0: print('red on')
                elif pos_on_led == 1: print('green on')
                elif pos_on_led == 2: print('blue on')
            else:
                GPIO.output(LED_PINS[i], LED_OFF)

        '''
        #----------------------------------------------------------
        # 다른 방식 #1
        GPIO.output(PIN_R, LED_ON if pos_on_led == 0 else LED_OFF)
        GPIO.output(PIN_G, LED_ON if pos_on_led == 1 else LED_OFF)
        GPIO.output(PIN_B, LED_ON if pos_on_led == 2 else LED_OFF)

        if pos_on_led == 0: print('red on')
        elif pos_on_led == 1: print('green on')
        elif pos_on_led == 2: print('blue on')

        # 다른 방식 #2
        if pos_on_led == 0:
            GPIO.output(PIN_R, LED_ON)
            print('red on')
        else:
            GPIO.output(PIN_R, LED_OFF)

        if pos_on_led == 1:
            GPIO.output(PIN_G, LED_ON)
            print('green on')
        else:
            GPIO.output(PIN_G, LED_OFF)

        if pos_on_led == 2:
            GPIO.output(PIN_B, LED_ON)
            print('blue on')
        else:
            GPIO.output(PIN_B, LED_OFF)
        '''
        time.sleep(1.0)   # 1초 대기

except KeyboardInterrupt:       # !중요! CTRL+C 로 종료
    GPIO.cleanup()
