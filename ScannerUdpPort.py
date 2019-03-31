import socket
import time
import threading


def __scanner_udp_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)
    try:
        sock.sendto(bytes(b'GET /other-19 HTTP/1.1'), (ip, port))
        data, addr = sock.recv(1024)
    except socket.timeout as e:
        print('port:', port, 'is OPEN')
    except:
        pass
    finally:
        sock.close()


def scan_udp_port():
    url = input("Enter url: ")
    port_range = input("Enter range ports: ").split()
    for i in range(len(port_range)):
        port_range[i] = int(port_range[i])
    ip = socket.gethostbyname(url)

    port_range[1] += 1
    if port_range[1] - port_range[0] < 0:
        print('второе число должно быть больше предыдущего')
        return

    print('scan udp port')

    threads = []

    for port in range(port_range[0], port_range[1]):
        threads.append(threading.Thread(target=__scanner_udp_port, args=(ip, port)))

    for thread in threads:
        time.sleep(0.01)
        thread.start()

    for thread in threads:
        time.sleep(0.01)
        thread.join()


def main():
    scan_udp_port()


if __name__=="__main__":
    scan_udp_port()

'''
def _build_packet(url='google.com'):
    randint = random.randint(0, 65535)
    packet = struct.pack(">H", randint)  # Query Ids (Just 1 for now)
    packet += struct.pack(">H", 0x0100)  # Flags
    packet += struct.pack(">H", 1)  # Questions
    packet += struct.pack(">H", 0)  # Answers
    packet += struct.pack(">H", 0)  # Authorities
    packet += struct.pack(">H", 0)  # Additional
    split_url = url.split(".")
    for part in split_url:
        packet += struct.pack("B", len(part))
        for s in part:
            packet += struct.pack('c',s.encode())
    packet += struct.pack("B", 0)  # End of String
    packet += struct.pack(">H", 1)  # Query Type
    packet += struct.pack(">H", 1)  # Query Class
    return packet


def scan_udp(host, port):
    result = os.popen("sudo nmap -sU -p " + str(port) + " " + host + " | grep open | awk '{ print $1 }'").read()
    if result is not None:
        print('port=', result[:-1], 'is OPEN')
'''