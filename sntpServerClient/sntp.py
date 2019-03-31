from multiprocessing import Process
from sntpServerClient.server import sntp_server
from sntpServerClient.client import sntp_client
import time
import socket


def check_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect(('127.0.0.1', 123))
        return True
    except:
        return False
    finally:
        sock.close()


def sntp():
    if check_port():
        print('Port already in use')
        return
    time.sleep(0.1)
    count_seconds = int(input('Write seconds: '))
    proc = []
    proc.append(Process(target=sntp_server, args=(count_seconds,)))
    proc.append(Process(target=sntp_client))

    for p in proc:
        time.sleep(0.1)
        p.start()

    for p in proc:
        time.sleep(0.01)
        p.join()

if __name__=='__main__':
    sntp()
