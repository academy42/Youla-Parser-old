#!/usr/bin/env python
import datetime
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException
from cfg import headers, PATH, ADDITIONAL_URL, logging
from typing import List
from storage_core import Storage
import re


class Parser:
    def __init__(self):
        self.__how_many_attempts = 2
        self.driver = webdriver.Firefox(executable_path="geckodriver.exe")
        self.headers = headers
        self.url = PATH + ADDITIONAL_URL
        self.storage = Storage()
        logging.info('Class parser has been inited')

    def get_html_page(self, url_to_parse) -> str:
        """Функция, которая возвращает html раметку страницы сайта: https://youla.ru/moskva/nedvijimost"""
        while self.__how_many_attempts > 0:
            self.driver.get(url=url_to_parse)
            self.__how_many_attempts -= 1

        html_page = self.driver.page_source
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
        logging.info('Got links of cards ' + f'{datetime.datetime.now()}')
        self.storage.write_data_urls(_links)
        return links_list

    def parse_cards_info(self) -> None:
        # global phone_num
        phone_num = None
        parsed_info = list()
        full_info = {}
        """Функция, которая парсит информацию с каждой карточки по полученной ссылке"""
        links_of_cards = self.get_urls_of_cards()

        for link in links_of_cards:
            try:
                self.driver.get(url=link)
            except WebDriverException:
                links_of_cards.remove(link)
                logging.info('Redirecting to promo-url, deleting this url from list of urls')  # logger
                continue
            splited_link_to_get_id = link.split('-')
            link_id = splited_link_to_get_id[-1]
            time.sleep(2)
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser')
            try:
                get_square_and_rooms = soup.find('h2', class_='sc-fznZeY').text.split(',')
            except AttributeError:
                logging.info("the elements haven't loaded yet, trying again")  # logger
                continue
            values_of_headers = soup.find_all("li", class_='sc-pcYTN')[2].find_all('dd', class_='sc-AxjAm')
            button = self.driver.find_elements_by_class_name('sc-fzokvW')
            if len(button) == 5:
                button[4].click()
            elif len(button) == 7:
                button[5].click()
            phone = self.driver.find_elements_by_tag_name('p')

            for p in phone:
                if re.match("(\W\d{1}) (\W\d{3}\W) (\d{3})-(\d{2})-(\d{2})", f'{p.text}'):
                    phone_num = p.text

                    logging.info('Writing parsed phone number to the list of a number')

            info = {
                'id': f'{link_id}',
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

        logging.info('Got an info from site')
        logging.info("Writing information to the MongoDB")
        self.storage.write_data_info(full_info)
