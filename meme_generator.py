import requests
import urllib
import random
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv('MEME_USERNAME')
password = os.getenv('MEME_PASSWORD')
water_messages = ['8 cups water a day, keep doctor away',
                  'water is good for your skin!',
                  'get up, drink water!!!',
                  'Water Time']


def generate_meme():
    images = get_img()
    img = random.choice(images)
    img_id = img['id']
    text0 = img['name']
    text1 = random.choice(water_messages)
    img_url = 'https://api.imgflip.com/caption_image'
    params = {
        'username': username,
        'password': password,
        'template_id': img_id,
        'text0': text0,
        'text1': text1
    }
    response = requests.request('POST', img_url, params=params).json()
    url = response['data']['url']
    return url


def get_img():
    data = requests.get('https://api.imgflip.com/get_memes').json()['data']['memes']
    images = [{'name': image['name'], 'url': image['url'], 'id': image['id']} for image in data]
    return images
