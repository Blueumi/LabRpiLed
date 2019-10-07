#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 위 주석은 한글을 위해 반드시 추가해 주어야 한다.

# 파이썬 Samples/runtext.py 수정

# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class RunText2(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText2, self).__init__(*args, **kwargs)     # class: RunText2
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        # font.LoadFont("../../../fonts/7x13.bdf")              # default
        font.LoadFont("../../../fonts/NanumGothicBoldx22.bdf")  # Font Height 31 Baseline 25
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        vpos = font.baseline + 1

        my_text = self.args.text

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, vpos, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText2()
    if (not run_text.process()):
        run_text.print_help()
