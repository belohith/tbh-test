from bs4 import BeautifulSoup
import requests
import time
import tweepy
from PIL import Image, ImageDraw, ImageFont
from image_utils import ImageText
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

def api():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Tweeted successfully!')

img = ImageText('img/blob.png')

def adding_text(img, text, position, size, colour):
    font = ImageFont.truetype("fonts/hkgrotesk.ttf", size, encoding="unic")
    draw = ImageDraw.Draw(img)
    draw.text(position, text, font=font, fill=colour)
    return img


url = 'https://www.nytimes.com/section/'
topic = ['technology', 'science', 'politics', 'sports', 'business', 'style']
i = 0

hkgrotesk = 'fonts/hkgrotesk.ttf'
cooperhewitt = 'fonts/cooperhewitt.ttf'
bluunext = 'fonts/bluunext.ttf' 
color = (50, 50, 50)
def scrape_news():
    html_text_0 = requests.get(f'{url}{topic[0]}').text
    soup_0 = BeautifulSoup(html_text_0, 'lxml')
    news_t_0 = soup_0.find('h2', class_='css-1kv6qi e15t083i0').text
    news_b_0 = soup_0.find('p', class_='css-1pga48a e15t083i1').text
    news_post_0 = f'Booook NEWS: {news_t_0}\n{news_b_0}\n'
    print(news_post_0)
    
    html_text_1 = requests.get(f'{url}{topic[1]}').text
    soup_1 = BeautifulSoup(html_text_1, 'lxml')
    news_t_1 = soup_1.find('h2', class_='css-1kv6qi e15t083i0').text
    news_b_1 = soup_1.find('p', class_='css-1pga48a e15t083i1').text
    news_post_1 = f'Booook NEWS: {news_t_1}\n{news_b_1}\n'
    print(news_post_1)
    
    html_text_2 = requests.get(f'{url}{topic[2]}').text
    soup_2 = BeautifulSoup(html_text_2, 'lxml')
    news_t_2 = soup_2.find('h2', class_='css-1kv6qi e15t083i0').text
    news_b_2 = soup_2.find('p', class_='css-1pga48a e15t083i1').text
    news_post_2 = f'Booook NEWS: {news_t_2}\n{news_b_2}\n'
    print(news_post_2)

    html_text_3 = requests.get(f'{url}{topic[3]}').text
    soup_3 = BeautifulSoup(html_text_3, 'lxml')
    news_t_3 = soup_3.find('h2', class_='css-1kv6qi e15t083i0').text
    news_b_3 = soup_3.find('p', class_='css-1pga48a e15t083i1').text
    news_post_3 = f'Booook NEWS: {news_t_3}\n{news_b_3}\n'
    print(news_post_3)
    
    html_text_4 = requests.get(f'{url}{topic[4]}').text
    soup_4 = BeautifulSoup(html_text_4, 'lxml')
    news_t_4 = soup_4.find('h2', class_='css-1kv6qi e15t083i0').text
    news_b_4 = soup_4.find('p', class_='css-1pga48a e15t083i1').text
    news_post_4 = f'Booook NEWS: {news_t_4}\n{news_b_4}\n'
    print(news_post_4)
    
    html_text_5 = requests.get(f'{url}{topic[5]}').text
    soup_5 = BeautifulSoup(html_text_5, 'lxml')
    news_t_5 = soup_5.find('h2', class_='css-1kv6qi e15t083i0').text
    news_b_5 = soup_5.find('p', class_='css-1pga48a e15t083i1').text
    news_post_5 = f'Booook NEWS: {news_t_5}\n{news_b_5}\n'
    print(news_post_5)

    # with Image.open('img/yellow.png') as img:
    #         img = adding_text(img, news_t, (10, 50), 50, (0, 0, 0,200))
    #         img = adding_text(img, news_b, (10, 150), 50, (0, 0, 0,200))
    #         img.save('img/whitetext.png')
    img.write_text_box((75, 150), news_t_0, box_width=400, font_filename=bluunext, font_size=25, color=color, place='center')
    img.write_text_box((75, 250), news_b_0, box_width=400, font_filename=hkgrotesk, font_size=25, color=color, place='center')
    img.write_text_box((575, 150), news_t_1, box_width=400, font_filename=bluunext, font_size=25, color=color, place='center')
    img.write_text_box((575, 250), news_b_1, box_width=400, font_filename=hkgrotesk, font_size=25, color=color, place='center')
    img.write_text_box((75, 650), news_t_2, box_width=400, font_filename=bluunext, font_size=25, color=color, place='center')
    img.write_text_box((75, 750), news_b_2, box_width=400, font_filename=hkgrotesk, font_size=25, color=color, place='center')
    img.write_text_box((575, 650), news_t_3, box_width=400, font_filename=bluunext, font_size=25, color=color, place='center')
    img.write_text_box((575, 750), news_b_3, box_width=400, font_filename=hkgrotesk, font_size=25, color=color, place='center')
    img.write_text_box((75, 1150), news_t_4, box_width=400, font_filename=bluunext, font_size=25, color=color, place='center')
    img.write_text_box((75, 1250), news_b_4, box_width=400, font_filename=hkgrotesk, font_size=25, color=color, place='center')
    img.write_text_box((575, 1150), news_t_5, box_width=400, font_filename=bluunext, font_size=25, color=color, place='center')
    img.write_text_box((575, 1250), news_b_5, box_width=400, font_filename=hkgrotesk, font_size=25, color=color, place='center')
    img.save('img/whitetext.png')
    time.sleep(10)
    tweet(api, '', 'img/whitetext.png')

if __name__ == '__main__':
    api = api()
    while True:
        scrape_news()
