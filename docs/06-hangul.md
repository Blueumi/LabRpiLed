# 라즈베리파이 한글 폰트 설치

1. 라즈베리파이에서 한글 보기용 폰트 설치
   <pre><code>sudo apt-get install fonts-unfonts-core fonts-nanum fonts-nanum-extra</code></pre>

# Windows용 폰트를 라즈베리파이로 복사해 넣기

1. Windows 폰트 확인
   1. 탐색기를 실행한 후 'C:\Windows\Fonts' 폴더로 이동한다.
   2. 라즈베리파이로 복사해 넣을 폰트를 찾는다. 여기서는 '나눔고딕 굵게' 폰트로 정한다.
   3. '나눔고딕' 폰트에서 우마우스 클릭하여 '열기'를 선택한다.
   4. '나눔고딕 굵게'를 우마우스 클릭하여 '속성'을 클릭한다.
   5. 텍스트 상자에 있는 영문 폰트명(NanumGothicBold.ttf)을 기억한다.
   6. '취소' 버튼을 클릭하고 탐색기를 닫느다.

2. Windows 폰트를 라즈베리파이로 복사하기
   1. FileZilla Client를 실행한다.
   2. 라즈베리파이에 연결한다.
      1. 상단 '호스트'에 라즈베리파이 IP 주소를 입력한다.
      2. 사용자명에 'pi'를 입력한다.
      3. 비밀번호에 'pi'의 비밀번호를 입력한다.
      4. 포트에 '22'를 입력한 후 엔터 키를 누른다.
   3. '알 수 없는 호스트키' 창에서 '확인' 버튼을 클릭한다.
   4. '/home/pi/WinFonts' 디렉토리를 선택한다.
      * 'WinFonts' 디렉토리가 없다면 '/home/pi' 디렉토리를 선택한 후에 새로운 디렉토리(WinFonts)를 생성한다.
   5. 왼쪽의 Windows 'C:\Windows\Fonts' 폴더에서 'NanumGothicBold.ttf'를 선택하여 우측 디렉토리로 파일을 옮겨서 복사해 넣는다.

# 전광판(RGB LED Matrix)용 폰트
  * LED Matrix에서는 파일 확장자가 'bdf'인 폰트를 사용
    > BDF(Glyph Bitmap Distribution Format, Adobe): 비트맵 글꼴 저장 파일 형식

1. 폰트 추출 프로그램 설치
   <pre><code>sudo apt-get install otf2bdf</code></pre>
   
2. 폰트 추출
   <pre>
   <code>cd ~/rpi-rgb-led-matrix/fonts
   otf2bdf ~/WinFonts/NanumGothicBold.ttf -o NanumGothicBoldx12.bdf -p 12
   otf2bdf ~/WinFonts/NanumGothicBold.ttf -o NanumGothicBoldx16.bdf -p 16
   otf2bdf ~/WinFonts/NanumGothicBold.ttf -o NanumGothicBoldx20.bdf -p 20
   otf2bdf ~/WinFonts/NanumGothicBold.ttf -o NanumGothicBoldx22.bdf -p 22
   </code></pre>
