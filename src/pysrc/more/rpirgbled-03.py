# rpirgbled-03.py
# RGB Led를 이용하여 무지개색을 표현한다.
import RPi.GPIO as GPIO
import time

# RGB 핀 번호
LED_PINS = [ 10, 9, 11 ]    # RGB 핀 번호

# 기본 상수 정의
# LED 공통핀이 GND인지 여부
IS_LED_COMMON_PIN_GND = False

# LED 공통핀이 GND인 경우에는 ON이 HIGH, OFF가 LOW
# LED 공통핀이 +인 경우에는 ON이 LOW, OFF가 HIGH
LED_ON = GPIO.HIGH if IS_LED_COMMON_PIN_GND == True else GPIO.LOW
LED_OFF = GPIO.LOW if IS_LED_COMMON_PIN_GND == True else GPIO.HIGH

# LED 공통핀이 GND인 경우 Duty 최대값은 100(On), 최소값은 0(Off)이다.
# LED 공통핀이 +인 경우 Duty 최대값은 0(On), 최소값은 100(Off)이다.
DUTY_ON = 100 if IS_LED_COMMON_PIN_GND == True else 0
DUTY_OFF = 0 if IS_LED_COMMON_PIN_GND == True else 100

# 빨강, 주황, 노랑, 초록, 파랑, 남색, 보라
colors = [
            {'name': '빨강', 'color':0xff0000 }
        ,   {'name': '주황', 'color':0xff7f00 }
        ,   {'name': '노랑', 'color':0xffd400 }
        ,   {'name': '초록', 'color':0x008000 }
        ,   {'name': '파랑', 'color':0x0067a3 }
        ,   {'name': '남색', 'color':0x000080 }
        ,   {'name': '보라', 'color':0x8b00ff }
        ]

#-----------------------------------------------------------------[ functions ]
# (함수) remap(x, in_max, out_max)
# 입력값을 0에서 out_max 사이의 값으로 바꾼다.
# - x : 색상 16진수
# - in_max : 0x00 ~ 0xFF
# - out_max : 0 ~ 100
def remap(x, in_max, out_max):
    return (out_max / in_max) * x

# (함수) setColor(col)
# LED 색 설정
# ex) col = 0xRRGGBB
def setColor(col):
    val_r = (col & 0xFF0000) >> 16      # Red 16진수
    val_g = (col & 0x00FF00) >> 8       # Green 16진수
    val_b = (col & 0x0000FF)            # Blue 16진수

    # 색상을 PWM에 맞게 변환 (0x00 ~ 0xFF 사이의 값을 0 ~ 100까지로 변환)
    val_r = int( remap(val_r, 0xFF, 100) )
    val_g = int( remap(val_g, 0xFF, 100) )
    val_b = int( remap(val_b, 0xFF, 100) )

    #print(hex(val_r), hex(val_g), hex(val_b))

    # 듀티 싸이클 변경
    new_r = val_r
    new_g = val_g
    new_b = val_b

    if IS_LED_COMMON_PIN_GND == False:
        new_r = 100 - val_r
        new_g = 100 - val_g
        new_b = 100 - val_b

    #print(val_r, val_g, val_b, new_r, new_g, new_b)

    PWM_R.ChangeDutyCycle(new_r)
    PWM_G.ChangeDutyCycle(new_g)
    PWM_B.ChangeDutyCycle(new_b)

#----------------------------------------------------------------------[ main ]
GPIO.setmode(GPIO.BCM)              # GPIO BCM 모드 설정
GPIO.setwarnings(False)

for pin_no in LED_PINS:
    GPIO.setup(pin_no, GPIO.OUT)    # GPIO 핀 모드를 출력으로 설정
    GPIO.output(pin_no, LED_OFF)    # Pull-up 상태인 경우는 출력 신호를 반대로

# 주파수 2KHz
PWM_R = GPIO.PWM(LED_PINS[0], 2000)
PWM_G = GPIO.PWM(LED_PINS[1], 2000)
PWM_B = GPIO.PWM(LED_PINS[2], 2000)

# 초기 듀티 싸이클, LED 끄기
PWM_R.start(DUTY_OFF)
PWM_G.start(DUTY_OFF)
PWM_B.start(DUTY_OFF)

# 무지개색 표현
print('> 무지개색 7가지 색상들을 1초마다 하나씩 보여준다.')

try:
    while True:
        for col in colors:
            print('* ' + col['name'])
            setColor(col['color'])
            time.sleep(1.0)

except KeyboardInterrupt:       # CTRL+C 로 종료
    PWM_R.stop()
    PWM_G.stop()
    PWM_B.stop()

    # LED 끄기
    for pin_no in LED_PINS:
        GPIO.output(pin_no, LED_OFF)
    
    GPIO.cleanup()
