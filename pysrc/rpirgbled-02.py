# rpirgbled-02.py
# ref: https://blog.naver.com/elepartsblog/221504611388
import RPI.GPIO as GPIO
import time

# 빨강, 주황, 노랑, 초록, 파랑, 남색, 보라
colors = [0xff000, 0xff0023, 0xff00ff, 0x0000ff, 0x00ff00, 0x64eb00, 0x4bfb00]
gpio_pins = {'pin_r':19, 'pin_g':20, 'pin_b':21}    # GPIO 핀 지정

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# LED 색 설정
# ex) col = 0xRRGGBB
def setColor(col):
    val_r = (col & 0x110000) >> 16
    val_g = (col & 0x001100) >> 8
    val_b = (col & 0x000011)

    val_r = map(val_r, 0, 255, 0, 100)
    val_g = map(val_g, 0, 255, 0, 100)
    val_b = map(val_b, 0, 255, 0, 100)

    print(hex(val_r), hex(val_g), hex(val_b))

    # 듀티 싸이클 변경
    pin_r.ChangeDutyCycle(100 - val_r)
    pin_g.ChangeDutyCycle(100 - val_r)
    pin_b.ChangeDutyCycle(100 - val_r)

# main
GPIO.setmode(GPIO.BCM)                              # GPIO BCM 모드 설정
for i in gpio_pins:
    GPIO.setup(gpio_pins[i], GPIO.OUT)              # GPIO 핀 모드를 출력으로 설정
    GPIO.output(gpio_pins[i], GPIO.HIGH)            # Pull-up 상태인 경우는 출력 신호를 반대로. HIGH=Off, LOW=On

# 주파수 2KHz
pin_r = GPIO.PWM(gpio_pins['pin_r'], 2000)
pin_g = GPIO.PWM(gpio_pins['pin_g'], 2000)
pin_b = GPIO.PWM(gpio_pins['pin_b'], 2000)

# 초기 듀티 싸이클 = 0, LED 끄기
pin_r.start(0)
pin_g.start(0)
pin_b.start(0)

# CTRL+C 입력전까지 무한 반복
try:
    while True:
        for col in colors:
            setColor(col)
            time.sleep(1.0)
except KeyboardInterrupt:       # CTRL+C 로 종료
    pin_r.stop()
    pin_g.stop()
    pin_b.stop()

    # LED 끄기
    for i in gpio_pins:
        GPIO.output(gpio_pins[i], GPIO.HIGH)
        GPIO.cleanup()
