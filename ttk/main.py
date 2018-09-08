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
        raise AttributeError('It is neither Host nor URL...')
    return ip

def menu():
    print('''
    {1} host2ip : Find IP from Host or URL
    ''')
    
    select_num = input('>>> ')

    if select_num is '1':
        host = input('>>> Host or URL : ')
        ip = host2ip(host)
        print(ip)
    else:
        exit()

if __name__ == '__main__':
    menu()