api ='https://api.github.com/repos/channelcat/sanic'
web_page='https://github.com/huge-success/sanic'

import requests
import webbrowser
import time

api ='https://api.github.com/repos/channelcat/sanic'

last_update =None # mannully change last update to test if the code works :2018-12-16T13:01:10Z

all_info = requests.get(api).json()

cur_update =all_info['updated_at']
print(cur_update)

while True:

    if not last_update:
        last_update = cur_update



    if last_update< cur_update:
        webbrowser.open(web_page)
    time.sleep(600)