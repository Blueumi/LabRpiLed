# 전광판(RGB LED Matrix) 준비

# Install RGB LED Matrix Modules

1. rpi-rgb-led-matrix 디렉토리가 있는지 확인한다. 디렉토리가 없으면 설치를 진행한다.
   <pre><code>ls</code></pre>

2. rpi-rgb-led-matrix를 github에서 받아온다.
   <pre><code>git clone https://github.com/hzeller/rpi-rgb-led-matrix</code></pre>

3. 샘플 API를 Make한다.
   <pre><code>cd ~/rpi-rgb-led-matrix/examples-api-use
   sudo python3 ./simple-square.py --led-no-hardware-pulse LED_NO_HARDWARE_PULSE --led-chain 1 --led-parallel 1 --led-rows 32 --led-cols 64</code></pre>
   
   * 전광판 그림이 깨어진다면 아래와 같이 해 본다.
   <pre><code>cd ~/rpi-rgb-led-matrix/examples-api-use
   sudo python3 ./simple-square.py --led-no-hardware-pulse LED_NO_HARDWARE_PULSE --led-chain 1 --led-parallel 1 --led-rows 32 --led-cols 64 --led-slowdown-gpio=2</code></pre>
