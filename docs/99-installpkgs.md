1. GPIO 라이브러리 설치
   <pre><code>sudo apt-get install rpi.gpio rpi.gpio-common</code></pre>
   
2. 라즈베리파이 GUI에서 한글 보기용 폰트 설치
   <pre><code>sudo apt-get install fonts-unfonts-core fonts-nanum fonts-nanum-extra</code></pre>

3. 폰트 추출 프로그램 설치
   <pre><code>sudo apt-get install otf2bdf</code></pre>

4. 개발용 Python 설치
   <pre><code>sudo apt-get install python3-dev python3-pillow -y</code></pre>

5. Python Web Server Flask 설치
   <pre><code>sudo apt-get install python3-flask</code></pre>

6. update
   <pre><code>sudo apt-get update</code></pre>

7. upgrade
   > Upgrade는 소요시간이 많이 걸리므로 되도록이면 맨 마지막에 진행함을 권장한다.
   <pre><code>sudo apt-get upgrade</code></pre>
   * Upgrade 종료시 'E:Unable to fetch some archives, maybe run apt-get update or try with --fix-missing?'와 같은 메시지가 나오면 추가 작업을 진행한다.
     <pre><code>sudo apt-get update
     sudo apt-get upgrade --fix-missing</code></pre>
