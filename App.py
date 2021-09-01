# from cfg import PATH, ADDITIONAL_URL, fake_user_agent, webdriver, BeautifulSoup, UserAgent
import sqlite3
import time

from cfg import *


class Application:
    def __init__(self):
        pass

    def run(self):
        pass

    def stop(self):
        pass


class Parser:
    def __init__(self):
        self.how_many_attempts = 2
        self.driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")
        self.headers = {
            'user-agent': f'{fake_user_agent.ff}',
            'Referer': 'https://youla.ru/'
        }
        self.url = PATH + ADDITIONAL_URL
        self.storage = Storage()

    def get_html_page(self):
        """Функция, которая возвращает html раметку страницы сайта: https://youla.ru/moskva/nedvijimost"""
        while self.how_many_attempts > 0:
            self.driver.get(url=self.url)
            self.how_many_attempts -= 1
        html_page = self.driver.page_source
        return html_page

    def get_urls_of_cards(self):
        """Функция, которая парсит ссылки на карточки объектов недвижимости и возвращает их список"""
        links_list = []
        page = self.get_html_page()
        soup = BeautifulSoup(page, 'html.parser')
        elements = soup.find_all('li', class_='product_item')
        for e in elements:
            links_list.append(PATH + e.find_next('a')['href'])
        for link in links_list:
            links_ = {
                'url': f'{link}'
            }
            id = self.storage.urls.insert_one(links_).inserted_id
            print(id)


        return links_list

    def parse_cards_info(self):
        pass


class Storage:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://Wyzledev:Miler776775@cluster0.fszrm.mongodb.net/test")
        self.database = self.client['Parser_Data']
        self.urls = self.database.urls


a = Parser()
c = a.get_urls_of_cards()
