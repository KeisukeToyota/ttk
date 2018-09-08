from main import *

def test_host2ip():
    hosts = [
        'http://www.sojo-u.ac.jp/top.html',
        'www.sojo-u.ac.jp',
        'www.sojo-u.ac.jp/top.html',
        'hgoehgoehogheo',
        'www.sojo-u.ac.jp/top.html',
        'https://www.sojo-u.ac.jp/top.html',
    ]

    for host in hosts:
        print(host2ip(host))


if __name__ == '__main__':
    test_host2ip()