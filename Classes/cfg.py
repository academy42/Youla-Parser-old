#!/usr/bin/env python
from fake_useragent import UserAgent
from selenium import webdriver
from bs4 import BeautifulSoup
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
PATH = 'https://youla.ru'

ADDITIONAL_URL = '/moskva/nedvijimost/prodaja-kvartiri'

fake_user_agent = UserAgent()

DB_PASSW = 'Miler776775'

headers = {
    'user-agent': f'{fake_user_agent.ff}',
    'Referer': 'https://youla.ru/'
}

db_link = f"mongodb+srv://Wyzledev:{DB_PASSW}@cluster0.fszrm.mongodb.net/test"

db_collection_name = "Parser_Data"

logging.basicConfig(filename="sample.log", level=logging.INFO)