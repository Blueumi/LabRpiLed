# 라즈베리파이 한글 폰트 설치

1. 라즈베리파이에서 한글 보기용 폰트 설치
   <pre><code>sudo apt-get install fonts-unfonts-core fonts-nanum fonts-nanum-extra</code></pre>

# 전광판(RGB LED Matrix)용 폰트
  > LED Matrix에서는 파일 확장자가 'bdf'인 폰트를 사용
    ** BDF(Glyph Bitmap Distribution Format, Adobe): 비트맵 글꼴 저장 파일 형식

1. 폰트 추출 프로그램 설치
   <pre><code>sudo apt-get install otf2bdf</code></pre>

2. Windows 폰트를 라즈베리파이로 복사
   > 예시 폰트: 나눔고딕(Bold)
   1. 탐색기에서 C:\Windows\Fonts 폴더로 이동
   2. '나눔고딕'을 우마우스 클릭하여 '열기' 선택
   3. '나눔고딕 굵게'를 우마우스 클릭하여 '속성' 선택하여 영문파일명 확인
     ** 'NanumGothicBold.ttf'
   4. FileZilla Client 실행하여 라즈베리파이 연결
      > 수정 필요
   
3. 폰트 추출
   <pre><code>
   cd ~/rpi-rgb-led-matrix/fonts
   otf2bdf ~/WinFonts/NanumGothicBold.ttf -o NanumGothicBoldx12.bdf -p 12
   otf2bdf ~/WinFonts/NanumGothicBold.ttf -o NanumGothicBoldx16.bdf -p 16
   otf2bdf ~/WinFonts/NanumGothicBold.ttf -o NanumGothicBoldx20.bdf -p 20
   otf2bdf ~/WinFonts/NanumGothicBold.ttf -o NanumGothicBoldx28.bdf -p 28
   </code></pre>
