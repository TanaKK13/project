from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

chromeoption = Options()
chromeoption.add_argument('--headless')

urls = [
    'https://www.youtube.com/channel/UCPA4lU-VlLO4-hU38JgItQw/videos'
]

video_url = []


def new():
    driver = webdriver.Chrome(options=chromeoption)
    for url in urls:
        driver.get('{}//videos?view=0&sort=dd&flow=grid'.format(url))
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'html.parser')
        titles = soup.findAll('a', id='video-title')
        video_urls = soup.findAll('a', id='video-title')

        j = 0
        for title in titles:
            if 'shorts' not in video_urls[j].get('href'):
                title = title.text
                url_video = 'https://www.youtube.com' + video_urls[j].get('href')
                itog = (title + ' ' + url_video)
                video_url.append(itog)

            j += 1

    return video_url
