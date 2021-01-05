#!/usr/bin/env python3

import requests
from credentials import API_KEY

def main():
    network_id = 'L_646829496481105433'
    
    url = f'https://api.meraki.com/api/v0/networks/{network_id}/devices'
    print(url)
    headers = {'X-Cisco-Meraki-API-Key': API_KEY}

    result = requests.get(url, headers=headers)
    if result.status_code == 200:
        for device in result.json():
            print(10*'*')
            print(f'Model: {device["model"]}')
            print(f'MAC: {device["mac"]}')
            print(f'SerialNumber: {device["serial"]}')
            print(f'LAN IP: {device["lanIp"]}')
            
if __name__ == '__main__':
    main()
