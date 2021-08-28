import json
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent

PATH = 'https://youla.ru'
additional_url = '/moskva/nedvijimost'


def get_urls():
    driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")

    (deal_type, engine_version, offer_type, region, page) = 'sale', 2, 'flat', -1, 1
    params = {
        'deal_type': deal_type,
        'engine_version': engine_version,
        'offer_type': offer_type,
        'region': region,
        'p': page
    }
    ua = UserAgent()

    headers = {
        'user-agent': f'{ua.ie}',
        'Referer': 'https://youla.ru/'
    }
    url = requests.get(PATH + additional_url, params=params, headers=headers).url
    if f'p={params["p"]}' in url:
        driver.get(url)
        sleep(0.5)
    while page != 2:
        driver.get(url)
        page += 1
        sleep(0.5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    a = [article.find('a')['href'] for article in soup.find_all('li', class_='product_item')]
    a1 = [PATH + i for i in a]
    return a1


def convert_to_json(list_of_urls):
    list_of_urls.pop(5)  # костыль, который потом уберу(им я удаляю промо-ссылку, которая стабильно стоит на 4 индексе)
    json.dump(list_of_urls, open('cards_urls.json', "w+"), ensure_ascii=False, indent=6)


if __name__ == "__main__":
    list_of_url = get_urls()
    convert_to_json(list_of_url)
