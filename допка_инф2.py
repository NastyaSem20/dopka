import threading
from urllib.request import urlopen
import json
import requests


def upload_cat():
    global count
    while count < 50:
        count += 1
        cat = urlopen(f'https://aws.random.cat/meow').read()
        cat_img_link = json.loads(cat)['file']
        cat_img = requests.get(cat_img_link)
        # print(cat_img, threading.current_thread())
        with open(f'cat_photo{count}.jpg', 'wb') as f:
            f.write(cat_img.content)


count = 0
th_list = []
for i in range(1, 5):
    th = threading.Thread(target=upload_cat, name=f'th-{i}')
    th_list.append(th)
    th.start()
