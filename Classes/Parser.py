#!/usr/bin/env python
import json
import time
from cfg import *
from typing import List
from Storage import Storage

class Parser:
    def __init__(self):
        self.__how_many_attempts = 2
        self.__driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe")
        self.headers = headers
        self.url = PATH + ADDITIONAL_URL
        self.storage = Storage()
        logging.info('Class parser has been inited')

    def get_html_page(self, url_to_parse) -> str:
        """Функция, которая возвращает html раметку страницы сайта: https://youla.ru/moskva/nedvijimost"""
        while self.__how_many_attempts > 0:
            self.__driver.get(url=url_to_parse)
            self.__how_many_attempts -= 1

        html_page = self.__driver.page_source
        logging.info('got an html of page')
        return html_page

    def get_urls_of_cards(self) -> List:
        """Функция, которая парсит ссылки на карточки объектов недвижимости и возвращает их список"""
        links_list = list()

        page = self.get_html_page(url_to_parse=self.url)
        link_parser_soup = BeautifulSoup(page, 'html.parser')
        elements = link_parser_soup.find_all('li', class_='product_item')
        while len(links_list) <= 67:

            for e in elements:
                links_list.append(PATH + e.find_next('a')['href'])
        _links = {
            'urls': f'{links_list}'
        }
        logging.info('Got links of cards')
        self.storage.write_data_urls(_links)
        return links_list

    def parse_cards_info(self) -> None:
        global phone_num
        parsed_info = list()
        full_info = {}
        """Функция, которая парсит ирмаию с каждой карточки по полученной ссылке"""
        links_of_cards = self.get_urls_of_cards()

        for l in links_of_cards:
            try:
                self.__driver.get(url=l)
            except WebDriverException:
                links_of_cards.remove(l)
                logging.info('Redirecting to promo-url, deleting this url from list of urls')  # logger
                continue
            time.sleep(2)
            page = self.__driver.page_source
            soup = BeautifulSoup(page, 'html.parser')
            try:
                get_square_and_rooms = soup.find('h2', class_='sc-fznZeY').text.split(',')
            except AttributeError:
                logging.info("the elements haven't loaded yet, trying again")  # logger
                continue
            values_of_headers = soup.find_all("li", class_='sc-pcYTN')[2].find_all('dd', class_='sc-AxjAm')
            button = self.__driver.find_elements_by_class_name('sc-fzokvW')
            if len(button) == 5:
                button[4].click()
            elif len(button) == 7:
                button[5].click()
            phone = self.__driver.find_elements_by_tag_name('p')

            try:

                if len(phone) == 8:
                    phone_num = phone[7]
                else:
                    phone_num = phone[7]
            except IndexError:
                phone_num = None
                logging.info('phone number not found or it was hidden')  # logger
                print("No phone number")
                info = {
                    'square': f'{get_square_and_rooms[2].strip(" ")}',
                    'rooms': f'{get_square_and_rooms[1].strip(" ")}',
                    'kitchen_square': f'{values_of_headers[1].text}',
                    'floor': f'{values_of_headers[2].text}',
                    'phone': f'{phone_num}'
                }
                parsed_info.append(info)
                full_info = {
                    'info': f'{parsed_info}'
                }
                continue

            if phone_num is None:
                info = {
                    'square': f'{get_square_and_rooms[2].strip(" ")}',
                    'rooms': f'{get_square_and_rooms[1].strip(" ")}',
                    'kitchen_square': f'{values_of_headers[1].text}',
                    'floor': f'{values_of_headers[2].text}',
                    'phone': f'{phone_num}'

                }
                parsed_info.append(info)
                full_info = {
                    'info': f'{parsed_info}'
                }

            elif phone_num is not None:
                info = {
                    'square': f'{get_square_and_rooms[2].strip(" ")}',
                    'rooms': f'{get_square_and_rooms[1].strip(" ")}',
                    'kitchen_square': f'{values_of_headers[1].text}',
                    'floor': f'{values_of_headers[2].text}',
                    'phone': f'{phone_num.text}',

                }
                parsed_info.append(info)
                full_info = {
                    'info': f'{parsed_info}'
                }
        logging.info('Got an info from site')
        self.storage.write_data_info(full_info)

