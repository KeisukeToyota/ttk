import os
from lib import *

def clear_screen():
    os.system('clear')

def menu():
    while True:
        clear_screen()
        print('''
        {1} host2ip : Find IP from Host or URL
        {2} wifi_scan : WiFi spot scan
        {99} Exit
        ''')

        select_num = input('>>> ')

        if select_num == '1':
            host = input('>>> Host or URL : ')
            ip = host2ip(host)
            print('\n' + ip + '\n')
            input('Enter continue...')
        elif select_num == '2':
            print('\n' + wifi_scan() + '\n')
            input('Enter continue...')
        elif select_num in ['99', 'exit']:
            print('bye!')
            break

if __name__ == '__main__':
    menu()
