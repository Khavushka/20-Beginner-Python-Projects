# Python automation 
# Importing packages 
# pip install schedule
# https://textbelt.com/
# pip install requests

import schedule
import time
import requests

def send_message():
    resp = requests.post('https://textbelt.com/text', {
    'phone': 'mobilenumber her',
    'message': 'Hej, smukke. I love you!!! Mom',
    'key': 'textbelt',
    })
    print(resp.json())

# schedule.every(10).minutes.do()
# schedule.every().hour.do()
# schedule.every().day.at("10:30").do()
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

# schedule.every().day.at("21:13").do(send_message)
schedule.every(5).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)