1. USB Serial 드라이버 다운로드후 설치
   > USB Serial에 맞는 드라이버 선택. 아래는 'PL2303HX' 칩을 사용한 드라이버 사이트임.
   * https://plugable.com/drivers/prolific/

2. USB Serial Controller 정상 확인
   1. 'Apple' 심볼 > '이 Mac에 관하여' > '시스템 리포트' 버튼 클릭
   2. '하드웨어' > 'USB' > 'USB 기기 트리'에서 'USB 버스' > 'USB-Serial Controller D' 선택후 '제조업체' 확인
      * 'PL2303HX'인 경우 'Prolific Technology Inc.'로 나옴
   3. '유틸리티' > '터미널' 실행후 tty 확인 
      <pre><code>$ ls /dev/tty.*&lt;Enter&gt;
      /dev/tty.Bluetooth-Incoming-Port	/dev/tty.usbserial</code></pre>
      * '/dev/tty.usbserial'이 나오지 않을 경우
        1. '시스템 환경설정' > '보안 및 개인 정보 보호' 선택
           * Lock이 걸려 있으면 Lock 해제
        2. '"Prolific" was blocked from loading.'에 있는 '승인' 버튼 클릭
           * Lock이 해제되어 있으며 Lock 처리

3. '터미널'에서 시리얼 프로그램으로 연결
   <pre><code>$ screen /dev/tty.usbserial 115200&lt;Enter&gt;
   <Enter>
   raspberrypi login: <b><u><i>pi</i></u></b>&lt;Enter&gt;
   Password: &lt;<b><u><i>pi password</i></u></b>&gt;&lt;Enter&gt;
   ...
   $</code></pre>

4. 할당된 IP 주소 확인
   <pre><code>$ ifconfig&lt;Enter&gt;
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

   <b><u><i>wlan0</i></u></b>: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
           inet <b><u><i>192.168.100.80</i></u></b>  netmask 255.255.255.0  broadcast 192.168.100.255
           inet6 fe80::3bc1:51af:9874:e532  prefixlen 64  scopeid 0x20<link>
           ether b8:27:eb:5f:58:d3  txqueuelen 1000  (Ethernet)
           RX packets 10  bytes 1171 (1.1 KiB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 32  bytes 4983 (4.8 KiB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
  $</code></pre>
  
