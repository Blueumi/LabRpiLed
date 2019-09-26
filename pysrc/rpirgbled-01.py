# Simple Python RGB Raspberry Pi Tutorial
# https://www.hackster.io/masteruan/simple-python-rgb-raspberry-pi-tutorial-298aa9

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# rgb 핀 번호
pin_r = 10  # pin seq:10, no:19
pin_g = 9   # pin seq:11, no:21
pin_b = 11  # pin seq:12, no:23

# Red 핀 정의
GPIO.setup(pin_r, GPIO.OUT)
GPIO.output(pin_r, 0)

# Green 핀 정의
GPIO.setup(pin_g, GPIO.OUT)
GPIO.output(pin_g, 0)

# Blue 핀 정의
GPIO.setup(pin_b, GPIO.OUT)
GPIO.output(pin_b, 0)

try:
    while True:
        req = input('rgb: ')    # raw_input
        if (len(req)==1):
            GPIO.output(pin_r, 1 if req=='r' else 0)
            GPIO.output(pin_g, 1 if req=='g' else 0)
            GPIO.output(pin_b, 1 if req=='b' else 0)
except KeyboardInterrupt:
    GPIO.cleanup()
