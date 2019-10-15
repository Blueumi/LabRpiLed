#rpirgbled-02.py
# 키 입력으로 RGB 선택적 On
import RPi.GPIO as GPIO

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
print('> 입력한 Red, Green, Blue led를 On 시킨다.')

try:
    while True:
        req = input('> rgb: ')    # 입력 대기

        # 먼저 모든 등을 Off 시킨다.
        GPIO.output(PIN_R, LED_OFF)
        GPIO.output(PIN_G, LED_OFF)
        GPIO.output(PIN_B, LED_OFF)

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
