import socket
import threading
import time


def __scanner_tcp_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect((ip, port))
        # sock.send(bytes(b'GET /other-19 HTTP/1.1\n\n'))
        # data, addr = sock.recv(1024)
        print("port=", port, "\\tcp is OPEN")
    except socket.timeout:
        pass
    except Exception as e:
        print('непонятная ошибка с портом', port)
    finally:
        sock.close()


def scan_tcp_port():
    url = input("Enter url: ")
    port_range = input("Enter range ports: ").split()
    for i in range(len(port_range)):
        port_range[i] = int(port_range[i])
    ip = socket.gethostbyname(url)

    port_range[1] += 1
    if port_range[1] - port_range[0] < 0:
        print('второе число должно быть больше предыдущего')
        return

    print('scan tcp port')

    threads = []

    for port in range(port_range[0], port_range[1]):
        threads.append(threading.Thread(target=__scanner_tcp_port, args=(ip, port)))

    for thread in threads:
        time.sleep(0.01)
        thread.start()

    for thread in threads:
        time.sleep(0.01)
        thread.join()


if __name__=="__main__":
    scan_tcp_port()
