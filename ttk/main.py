import os
from lib import *

MENUS = {
    '1' : wrap_host2ip, '2' : wrap_wifi_scan,
    '3' : wrap_connect_wifi, '4' : wrap_all_repo_clone,
    '5' : wrap_all_repo_pull, '99' : exit,
    'exit' : exit
}

def clear_screen():
    os.system('clear')

def menu():
    while True:
        clear_screen()
        print('''
        {1} host2ip : Find IP from Host or URL
        {2} wifi_scan : WiFi spot scan
        {3} connect_wifi : Conect WiFi
        {4} all_repo_clone : Github account repository clone
        {5} all_repo_pull : Github account repository pull
        {99} Exit
        ''')
        select_num = input('>>> ')
        try:
            MENUS[select_num]()
        except KeyError:
            continue

if __name__ == '__main__':
    menu()
