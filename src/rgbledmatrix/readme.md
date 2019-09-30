# 전광판(RGB LED Matrix) 보드 준비

# Install RGB LED Matrix Modules

1. rpi-rgb-led-matrix 디렉토리가 있는지 확인한다. 디렉토리가 없으면 설치를 진행한다.
   <pre><code>ls</code></pre>

2. rpi-rgb-led-matrix를 github에서 받아온다.
   <pre><code>git clone https://github.com/hzeller/rpi-rgb-led-matrix</code></pre>

3. 샘플 API를 Make한 뒤에 데모를 실행한다.
   <pre><code>cd ~/rpi-rgb-led-matrix/examples-api-use
   sudo ./demo --led-rows=32 --led-cols=64 --led-chain=1 --led-parallel=1 --led-no-hardware-pulse -D 9</code></pre>
   
   * 전광판 그림이 깨어진다면 아래와 같이 '--led-slowdown-gpio' 값을 증가시켜 본다.
   <pre><code>sudo ./demo --led-rows=32 --led-cols=64 --led-chain=1 --led-parallel=1 --led-no-hardware-pulse --led-slowdown-gpio=2 -D 9</code></pre>

# Python 모듈 설치

1. 개발용 Python3를 설치한다.
   <pre><code>cd ~/rpi-rgb-led-matrix/bindings/python
   sudo apt-get update
   sudo apt-get install python3-dev python3-pillow -y</code></pre>

2. 빌더를 진행한다.
   <pre><code>make build-python PYTHON=$(which python3)
   sudo make install-python PYTHON=$(which python3)</code></pre>

# Python 기본 샘플

* 작업 디렉토리: ~/rpi-rgb-led-matrix/bindings/python/samples
* 전광판 그림이 깨어지는 경우에는 옵션에 '--led-slowdown-gpio 2'를 추가한다.
    1. 사각형
         <pre><code>sudo python3 ./simple-square.py --led-no-hardware-pulse 1 --led-chain 1 --led-parallel 1 --led-rows 32 --led-cols 64</code></pre>

    2. 문자열
         <pre><code>sudo python3 ./runtext.py --led-no-hardware-pulse 1 --led-chain 1 --led-parallel 1 --led-rows 32 --led-cols 64 -t Hello</code></pre>

# Python 변형 샘플
  * runtext2.py : 한글 폰트 적용 예제
  * rwbox.py : 그래픽과 문자 혼합 예제

# Python 기준 모듈

  1. ~/rpi-rgb-led-matrix/bindings/python/rgbmatrix
     * core.pyx
     * graphics.pyx

  2. ~/rpi-rgb-led-matrix/bindings/python/samples
     * graphics.py
     * samplebase.py
