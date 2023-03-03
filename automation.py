# Python automation 
# Importing packages 
# pip install schedule
# https://textbelt.com/
# pip install requests

import requests

def send_message():
    resp = requests.post('https://textbelt.com/text', {
    'phone': '60833306',
    'message': 'Hej, smukke',
    'key': 'textbelt',
    })
    print(resp.json())