import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time

user_minutes = int(input('After how many minutes would you like this to run again?: '))

min_to_secs = user_minutes * 60


def cb_scraper():

    notifier = ToastNotifier()

    URL = 'https://comicbook.com/'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('div', {'class': "headline-box"})
    print(title)

    if 'Star Wars' in title.text:
        notifier.show_toast('Comicbook.com', 'A New Star Wars article is available', duration=10, icon_path='CB_logo.ico')
    if 'Mandalorian' in title.text:
        notifier.show_toast('Comicbook.com', 'A New Star Wars article is available', duration=10, icon_path='CB_logo.ico')
    if 'Yoda' in title.text:
        notifier.show_toast('Comicbook.com', 'A New Star Wars article is available', duration=10, icon_path='CB_logo.ico')        


if __name__ == '__main__':
    while True:
        cb_scraper()
        time.sleep(min_to_secs)
