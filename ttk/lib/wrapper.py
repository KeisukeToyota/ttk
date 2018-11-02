from .network import host2ip, wifi_scan, connect_wifi
from .github import all_repo_clone, all_repo_pull

def wrap_host2ip():
    host = input('>>> Host or URL : ')
    ip = host2ip(host)
    print('\n' + ip + '\n')
    input('Enter continue...')

def wrap_wifi_scan():
    print('\n' + wifi_scan() + '\n')
    input('Enter continue...')

def wrap_connect_wifi():
    ssid = input('>>> SSID : ')
    password = input('>>> Password : ')
    result = connect_wifi(ssid, password)
    print('\n' + result + '\n')
    input('Enter continue...')

def wrap_all_repo_clone():
    target = input('users or orgs : ')
    org = input(f"{target} name : ")
    pages = int(input('get page count : '))
    for page in range(1, pages + 1):
        all_repo_clone(target, org, page)
    input('\nEnter continue...\n')

def wrap_all_repo_pull():
    dir_path = input('Directory path : ')
    all_repo_pull(dir_path)
    input('\nEnter continue...\n')
