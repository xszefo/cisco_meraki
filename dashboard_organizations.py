#!/usr/bin/env python3

import requests
from credentials import API_KEY

def main():
    url = 'https://api.meraki.com/api/v0/organizations'
    headers = {'X-Cisco-Meraki-API-Key': API_KEY}

    print(url)

    result = requests.get(url, headers=headers)
    if result.status_code == 200:
        for org in result.json():
            print(10*'*')
            print(f'Name: {org["name"]}')
            print(f'ID: {org["id"]}')
            print(f'URL: {org["url"]}')

if __name__ == '__main__':
    main()
