from urllib.request import urlopen
import os
from ScannerTcpPort import scan_tcp_port
from ScannerUdpPort import scan_udp_port
from Tracer import tracer
from sntpServerClient.sntp import sntp


def get_list_ip(host):
    return os.popen("host " + host + " | awk '{ print $4 }'").read().split('\n')[:-3]


def check_internet_conn():
    try:
        urlopen('https://google.com/', timeout=5)
        return True
    except:
        return False


def print_start_menu():
    while True:
        print("\n\n--------------------------------------")
        print("---------->  PORT SCANNER  <----------")
        print("--------------------------------------")
        print("   MENU\n")
        print("1. Port scanner TCP")
        print("2. Port scanner UDP")
        print("3. Tracer")
        print("4. SNTP server for wrong time")
        print("h. Help")
        print("0. Exit")
        print("-------------------------------------\n")
        reader = input("> ")

        if reader == "1":
            scan_tcp_port()
            input("\nPress Enter to continue...")
            print_start_menu()

        if reader == "2":
            scan_udp_port()
            input("\nPress Enter to continue...")
            print_start_menu()

        if reader == "3":
            tracer()
            input("\nPress Enter to continue...")
            print_start_menu()

        if reader == '4':
            sntp()
            input("\nPress Enter to continue...")
            print_start_menu()

        if reader == "h":
            messageraw = open("help.txt", "r")
            print(messageraw.read())
            input("\nPress Enter to continue...")
            print_start_menu()

        if reader == "0":
            exit()


def main():
    if not check_internet_conn():
        print('please, connect internet')
        return
    try:
        print_start_menu()
    except KeyboardInterrupt as e:
        print('You enter ctrl + C')
    except:
        pass


if __name__ == '__main__':
    main()
