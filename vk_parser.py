import csv

import requests
import time

token = " " # put in your API-token here

def ParsePosts():

    version = 5.126
    domain = "nrmusicru"
    count = 100
    offset = 0
    all_posts = []

    while offset < 13000:

        response = requests.get('http://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                })
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
        time.sleep(0.5)
    return all_posts
all_posts = ParsePosts()


def csv_writer(data):
    with open('nrmusicru_df.csv', 'w', encoding='utf-8') as file:
         a_pen = csv.writer(file)
         a_pen.writerow(("date","body","artist","likes"))
         for post in all_posts:
             try:
                 a_pen.writerow((post['date'],
                                 post['text'],
                                 post['attachments'][1]['audio']['artist'],
                                 post['likes']['count']
                                 ))
             except:
                pass
all_posts = ParsePosts()
csv_writer(all_posts)
