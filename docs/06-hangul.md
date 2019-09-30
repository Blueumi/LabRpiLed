# 라즈베리파이 한글 폰트 설치


# 전광판을 위한 한글 폰트 생성

<pre><code>
cd ~/rpi-rgb-led-matrix/fonts
otf2bdf ~/WinFornts/NanumGothicBold.ttf -o NanumGothicBoldx12.bdf -p 12
otf2bdf ~/WinFornts/NanumGothicBold.ttf -o NanumGothicBoldx16.bdf -p 16
otf2bdf ~/WinFornts/NanumGothicBold.ttf -o NanumGothicBoldx20.bdf -p 20
</code></pre>