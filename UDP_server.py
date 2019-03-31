import socket


def udp_server(host='127.0.0.1', port=1234):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    while True:
        (data, addr) = s.recvfrom(128*1024)
        # print(addr)
        s.sendto(bytes(b'i up this udp server for test'), addr)

def main():
    udp_server()


if __name__ == '__main__':
    main()
