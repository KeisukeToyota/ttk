import socket
from urllib.parse import urlparse
import os

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
    while True:
      clear_screen()
      print('''
      {1} host2ip : Find IP from Host or URL
      {99} Exit
      ''')

      select_num = input('>>> ')

      if select_num == '1':
          host = input('>>> Host or URL : ')
          ip = host2ip(host)
          print('\n' + ip + '\n')
          input('Enter continue...')
      elif select_num == '99':
          print('bye!')
          break

if __name__ == '__main__':
    menu()
