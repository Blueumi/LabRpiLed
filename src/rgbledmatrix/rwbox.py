#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 위 주석은 한글을 위해 반드시 추가해 주어야 한다.

# Image-draw.py 와 runtext.py 의 결합

# Display a runtext with double-buffering.
from samplebase import SampleBase
from PIL import Image
from PIL import ImageDraw
#import graphics
from rgbmatrix import graphics, RGBMatrix, RGBMatrixOptions
import time

class RwBox(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RwBox, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="이미지와 글자의 결합")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        offscreen_canvas.Clear()

        # 1. 기본값
        canvas_cols = offscreen_canvas.width
        canvas_rows = offscreen_canvas.height

        # 2. Box 준비

        # RGB example w/graphics prims.
        # Note, only "RGB" mode is supported currently.
        image = Image.new("RGB", (canvas_cols, canvas_rows))  # Can be larger than matrix if wanted!!
        draw = ImageDraw.Draw(image)  # Declare Draw instance before prims

        # Draw some shapes into image (no immediate effect on matrix)...
        draw.rectangle((0, 0, canvas_cols - 1, canvas_rows - 1), fill=(0, 0, 0), outline=(255, 0, 0))
        #draw.line((0, 0, 31, 31), fill=(255, 0, 0))
        #draw.line((0, 31, 31, 0), fill=(0, 255, 0))

        # 3. 글자 만들기
        font = graphics.Font()
        # font.LoadFont("../../../fonts/NanumGothicBoldx20.bdf")     # Font Height 29 Baseline 23
        font.LoadFont("../../../fonts/NanumGothicBoldx22.bdf")     # Font Height 31 Baseline 25
        text_color = graphics.Color(255, 255, 255)

        # 4. 위치 준비
        text_pos = offscreen_canvas.width
        text_len = 0
        my_text = self.args.text

        font_row_pos = font.baseline + 1

        # 5. 표시
        while True:
            text_pos -= 1
            if text_pos + text_len < 0:
                text_pos = offscreen_canvas.width

            # offscreen_canvas.Clear()
            offscreen_canvas.SetImage(image, 0, 0)
            text_len = graphics.DrawText(offscreen_canvas, font, text_pos, font_row_pos, text_color, my_text)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            time.sleep(0.1)

# Main function
if __name__ == "__main__":

    # 실행
    run_text = RwBox()
    if (not run_text.process()):
        run_text.print_help()
