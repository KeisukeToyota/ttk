import socket
from urllib.parse import urlparse
import subprocess

def host2ip(host):
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        host = urlparse(host).netloc
        ip = socket.gethostbyname(host)
    if ip == '0.0.0.0':
        return 'Error : It is neither Host nor URL...'
    return ip

def wifi_scan():
    try:
        output = subprocess.getoutput('/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -s')
    except Exception as e:
        output = 'Error : No connecton...'
    return output

def sniffer():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    while True:
        print(s.recvfrom(65565))
