# Windows 8이하 에서 USB Serial 연결 및 TeraTerm을 통한 라즈베리파이 접속
  > Windows 8 이하에서 테스트 진행하지 않아서 정상 동작이 안될 수도 있음

1. USB Serial COM 포트 확인
   1. USB Serial Device를 Windows USB 포트에 삽입
   2. '시작'(윈도 심볼)을 우마우스 클릭 &gt; '장치 관리자' 선택
      1. '포트(COM && LPT)' 클릭하여 확장
	  2. COM Por 확인
	     * 포트명 앞에 경고 아이콘이 있을 경우 드라이버 재설치 필요하며 단계 2.로 갈 것.

2. USB Serial 드라이버 이상이 있을 경우 드라이버 다운로드후 재설치
   1. USB Serial Device를 USB 포트에서 제거
   2. '장치 관리자'에서 '기타 장치' &gt; 'USB-Serial Controller' 확인
      1. 'USB-Serial Controller'에서 우마우스 클릭 &gt; '드라이버 업데이트' &gt; '업데이트된 드라이버 소프트웨어 자동 검색' 선택
	  2. '닫기' 버튼 클릭
   2. USB Serial에 맞는 드라이버 선택하여 드라이버 설치
      1. PL2303HX USB Serial Driver: https://plugable.com/drivers/prolific/
	  2. 'PL2303-Prolific_DriverInstaller_v&lt;<i>nnnn</i>&gt;.exe' 실행하여 설치

3. TeraTerm의 시리얼로 라즈베리파이에 연결하여 할당된 IP 주소 확인
   <pre><code>$ <b><u><i>ifconfig</i></u></b>&lt;Enter&gt;
   eth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
           ether b8:27:eb:0a:0d:86  txqueuelen 1000  (Ethernet)
           RX packets 0  bytes 0 (0.0 B)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 0  bytes 0 (0.0 B)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

   lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
           inet 127.0.0.1  netmask 255.0.0.0
           inet6 ::1  prefixlen 128  scopeid 0x10<host>
           loop  txqueuelen 1000  (Local Loopback)
           RX packets 0  bytes 0 (0.0 B)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 0  bytes 0 (0.0 B)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

   <b><u>wlan0</u></b>: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
           inet <b><u>192.168.100.80</u></b>  netmask 255.255.255.0  broadcast 192.168.100.255
           inet6 fe80::3bc1:51af:9874:e532  prefixlen 64  scopeid 0x20<link>
           ether b8:27:eb:5f:58:d3  txqueuelen 1000  (Ethernet)
           RX packets 10  bytes 1171 (1.1 KiB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 32  bytes 4983 (4.8 KiB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
   $ ■</code></pre>
   
5. TeraTerm의 SSH로 라즈베리파이에 연결하기
   * 앞서 '4'에서의 WiFi IP 주소(여기서는 192.168.100.80으로 가정함) 확인
