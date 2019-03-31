import socket
from datetime import datetime, timedelta


def __get_time(count_seconds) -> str:
    current_time = datetime.now()
    delta = timedelta(seconds=count_seconds)
    return str(current_time + delta)


def sntp_server(count_seconds):
    # count_seconds = int(input('Seconds count\n'))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(('127.0.0.1', 123))
        s.listen(1)
        conn, addr = s.accept()
        response = bytes(__get_time(count_seconds), "utf8")
        conn.sendall(response)
        conn.close()
    except:
        return
    finally:
        s.close()


if __name__=='__main__':
    sntp_server(3600)
