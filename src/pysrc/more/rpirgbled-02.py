#rpirgbled-02.py
# 키 입력으로 RGB 선택적 On
import RPi.GPIO as GPIO

# RGB 핀 번호
LED_PINS = [ 10, 9, 11 ]    # RGB 핀 번호
PIN_R = LED_PINS[0]         # RED
PIN_G = LED_PINS[1]         # GREEN
PIN_B = LED_PINS[2]         # BLUE

# LED 공통 핀이 GND인 경우에는 ON이 HIGH, OFF가 LOW
# LED 공통 핀이 +인 경우에는 ON이 LOW, OFF가 HIGH
IS_LED_COMMON_PIN_GND = False
LED_ON = GPIO.HIGH if IS_LED_COMMON_PIN_GND == True else GPIO.LOW
LED_OFF = GPIO.LOW if IS_LED_COMMON_PIN_GND == True else GPIO.HIGH

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED 핀 속성 정의 및 초기화
for i in range(0, 3):
    GPIO.setup(LED_PINS[i], GPIO.OUT)
    GPIO.output(LED_PINS[i], LED_OFF)

# 타이틀 메시지 출력
print('> 입력한 Red, Green, Blue led를 On 시킨다.')

try:
    while True:
        req = input('> rgb: ')    # raw_input

        # 모든 등을 Off 시킨다.
        for i in range(0, 3):
            GPIO.output(LED_PINS[i], LED_OFF)

        if (len(req)>0):

            # 필요한 등만 On 시킨다.
            for c in req:
                if c == 'r':
                    GPIO.output(PIN_R, LED_ON)
                    print('red on')
                elif c == 'g':
                    GPIO.output(PIN_G, LED_ON)
                    print('green on')
                elif c == 'b':
                    GPIO.output(PIN_B, LED_ON)
                    print('blue on')
        else:
            print('all led off')

except KeyboardInterrupt:       # !중요! CTRL+C 로 종료
    GPIO.cleanup()
