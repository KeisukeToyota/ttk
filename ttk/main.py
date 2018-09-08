import socket
from urllib.parse import urlparse
import os
import http.cookiejar
import threading

def clear_screen():
    os.system('clear')

def host2ip(host):
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        host = urlparse(host).netloc
        ip = socket.gethostbyname(host)
    if ip == '0.0.0.0':
        raise AttributeError('It is neither IP nor URL...')
    return ip
