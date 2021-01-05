#!/usr/bin/env python3

import requests
from credentials import API_KEY

def main():
    org_id = '549236'
    
    url = f'https://api.meraki.com/api/v0/organizations/{org_id}/networks'
    print(url)
    headers = {'X-Cisco-Meraki-API-Key': API_KEY}

    result = requests.get(url, headers=headers)
    if result.status_code == 200:
        for network in result.json():
            print(10*'*')
            print(f'ID: {network["id"]}')
            print(f'Name: {network["name"]}')
            print(f'TimeZone: {network["timeZone"]}')

            
if __name__ == '__main__':
    main()
