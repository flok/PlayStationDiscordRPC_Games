import base64, requests, os, sys

API_ENDPOINT = 'https://discord.com/api/v9'
TOKEN = sys.argv[1]
CLIENT_ID = '906197927968526358'

def get_assets():
    url = '%s/oauth2/applications/%s/assets' % (API_ENDPOINT, CLIENT_ID)
    headers={'Authorization': '%s' % TOKEN}
    r = requests.get(url=url, headers=headers)
#    r = requests.get('%s/oauth2/applications/%s/assets' % (API_ENDPOINT, CLIENT_ID), headers={'Authorization': '%s' % TOKEN})
    r.raise_for_status()
    return r.json()

def add_asset(name, image_data):
    data = {
        'name': name,
        'image': image_data,
        'type': 1
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': '%s' % TOKEN
    }
    r = requests.post('%s/oauth2/applications/%s/assets' % (API_ENDPOINT, CLIENT_ID), headers=headers, json=data)
    
    r.raise_for_status()
    return r.json()

def delete_asset(id):
    r = requests.delete('%s/oauth2/applications/%s/assets/%s' % (API_ENDPOINT, CLIENT_ID, id), headers={'Authorization': '%s' % TOKEN})
    r.raise_for_status()