import subprocess
import requests
import json


def tracer():
    url = input("Enter url: ")
    if 'http' in url:
        print('Введите без http')
        return
    list_ip = subprocess.getoutput("traceroute " + url + " | awk '{ print $3 }'").replace('(', '').replace(')', '').split()[1:]
    for ip in list_ip:
        if ip != '*':
            req = requests.get("https://ipinfo.io/{0}/json".format(ip))
            if req.status_code == 200:
                data = req.json()
                if 'bogon' in data:
                    print('ip:', data['ip'], 'зарезервированный ip, который не закреплен за провайдером')
                    continue

                if 'org' in data:
                    print('ip:', data['ip'], 'org:', data['org'], 'country:', data['country'], end=' ')
                    if 'hostname' in data:
                        print('hostname:', data['hostname'])
                    else:
                        print()
                    continue
        else:
            print('ip:', ip, 'secret ip')


if __name__ == '__main__':
    tracer()
