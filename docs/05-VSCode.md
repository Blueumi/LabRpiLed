# Visual Studio Code 개발툴 한글화

1. 좌측 'Extensions' 아이콘 클릭한다.
2. 검색 박스에 'korean' 입력한다.
3. 목록에서 'Korean Language Pack for Visual Studio Code' 선택한다.
4. 'Install' 버튼 클릭한다.
5. 하단의 'Restart Now' 버튼 클릭한다.

[Youtube - Visual Studio Code 개발툴 한글화](https://youtu.be/kx7kpDC5llg)

# Visual Studio Code 원격 개발툴 설치

1. 좌측 'Extensions' 아이콘 클릭한다.
2. 검색 박스에 'Remote Development' 입력, 목록 선택후 'Install' 버튼 클릭한다.

# Visual Studio Code 원격 개발 환경 설정

1. &lt;F1&gt; 키를 누른다.
2. 'remotessh' 입력해서 나온 목록에서 'Remote-SSH:Connect to Host...' 선택한다.
3. 박스 하단의 'Add New SSH Hosts...'를 선택한다.
4. 'ssh pi@&lt;원격접속할 곳의 IP 주소&gt; -A'를 입력후 &lt;Enter&gt; 키를 누른다.
5. 'C:\Users\&lt;User Account&gt;\.ssh\config'를 선택한다.
6. 하단에 'Host added!' 팝업을 확인후 'Open Config' 버튼을 클릭한다.
   * 다음과 같이 정의되었음을 확인한다.
   <pre>
     <code>
     Host 192.168.137.227
       User pi
       ForwardAgent yes
     </code>
   </pre>



3. 박스 하단의 'Configure SSH Hosts...'를 선택한다.
4. 'C:\Users\&lt;User Account&gt;\.ssh\config'를 선택한다.

3. 'pi@&lt;원격접속할 곳의 IP 주소&gt;' 주소를 입력한다. (ex: pi@192.168.137.227)
4. 'Windows 보안 경고' 창이 뜨면 '액세스 허용' 버튼을 클릭한다.
5. 'Could not establish to "&lt;IP 주소&gt;". Connecting was canceled.' 오류창에서 'More Actions...' 버튼을 클릭한다.


