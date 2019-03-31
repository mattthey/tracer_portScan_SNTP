import socket


def sntp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(('127.0.0.1', 123))
        data = s.recv(1024)
    except:
        print("Попробуйте позже")
        return
    finally:
        s.close()
    print("Получил: {}".format(repr(data)))


if __name__=='__main__':
    sntp_client()
