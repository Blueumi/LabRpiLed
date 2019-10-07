#-*- coding: utf-8 -*-
# 파이썬 Samples/runtext2.py 수정
from flask import Flask, render_template, request

# RGB LED Matrix
# Display a runtext with double-buffering.
from samplebase2 import SampleBase2
from rgbmatrix import graphics
import threading
import time
from time import sleep


# StaticVals 이외에서는 사용하지 말 것!!!
_isThread1Alive = False
_ledStr = '안녕하세요!'
t1 = ''


# class: StaticVals()
# 프로그램 전체에서 사용할 변수들
class StaticVals(object):
    # Thread가 살아 있는지 여부
    def isThread1Alive(self):
        global _isThread1Alive
        return _isThread1Alive

    # Thread 생존 여부 설정
    def setThread1Alive(self, isAlive):
        global _isThread1Alive
        _isThread1Alive = isAlive

    # Led 문자 얻기
    def getLedStr(self):
        global _ledStr
        return _ledStr

    # Led 문자열 설정
    def setLedStr(self, ledStr):
        global _ledStr
        _ledStr = ledStr
        print('* StaticVals.setLedStr() - _ledStr', _ledStr)


# class: RunText2()
# LED 로 문자열 출력
class RunText2(SampleBase2):
    def __init__(self, *args, **kwargs):
        super(RunText2, self).__init__(*args, **kwargs)     # class: RunText2

        static_vals = StaticVals()
        print('* LED Text:', static_vals.getLedStr())   # LED 에 출력할 문자열을 가져온다.

        # self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default=static_vals.getLedStr())

    def run(self):
        print('RunText2', 'run()')

        offscreen_canvas = self.matrix.CreateFrameCanvas()

        # Font 할당
        font = graphics.Font()
        font.LoadFont("../../../fonts/NanumGothicBoldx22.bdf")

        textColor = graphics.Color(255, 255, 0)                 # 문자열 색상 정의
        pos = offscreen_canvas.width                            # 문자열 표시할 최초 위치
        vpos = font.baseline + 1

        static_vals = StaticVals()
        my_text = static_vals.getLedStr()                       # LED 에 출력할 문자열

        # while True:
        while static_vals.isThread1Alive():
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, vpos, textColor, my_text)
            pos -= 1

            if (len + pos < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

        print('- Finished RunText2.run()')


# ------------------------------------------------------------------------
# main
# ------------------------------------------------------------------------

# Thread1Proc()
# RunText2() 호출
def Thread1Proc():
    print('* main.ThreadProc()')

    static_vals = StaticVals()
    static_vals.setThread1Alive(True)

    run_text = RunText2()
    if (not run_text.process()):
        static_vals.setThread1Alive(False)

    print('- Finished main.ThreadProc()')

# runThread1()
# 쓰레드를 생성하여 Thread1Proc()를 호출하여 실행시킨다.
def runThread1():
    print('* main.runThread1()')

    global t1
    static_vals = StaticVals()
    static_vals.setThread1Alive(False)
    sleep(1)

    t1 = threading.Thread(target=Thread1Proc)
    t1.start()

    print('- Finished main.runThread1()')


# Flask
app = Flask(__name__)


# index() / index.html
# LED 로 출력할 문자열을 받아서 /send_cont 로 보낸다.
@app.route('/')
def index():
    static_vals = StaticVals()
    return render_template('index.html', led_str=static_vals.getLedStr())


# send_content() / send_cont / send_ok.html
# index.html 에서 보내어 온 문자열을 받아서 전광판으로 출력한다.
@app.route('/send_cont', methods=['post'])
def send_content():
    cont = request.values.get('cont')

    # 전역에 보관
    static_vals = StaticVals()
    static_vals.setLedStr(cont)

    # 전광판 표시 진행
    runThread1()        # 쓰레드 호출

    return render_template('send_ok.html', cont=cont)


# Start WWW
app.run(host='0.0.0.0', port=3000, debug=True)
