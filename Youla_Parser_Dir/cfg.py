#!/usr/bin/env python
from fake_useragent import UserAgent
import logging

PATH = 'https://youla.ru'

ADDITIONAL_URL = '/moskva/nedvijimost/prodaja-kvartiri'

fake_user_agent = UserAgent()

DB_PASSW = 'Miler776775'

headers = {
    'user-agent': f'{fake_user_agent.ff}',
    'Referer': 'https://youla.ru/'
}

db_link = f"mongodb+srv://Wyzledev:{DB_PASSW}@cluster0.fszrm.mongodb.net/test?connectTimeoutMS=60000"

db_collection_name = "Parser_Data"

logging.basicConfig(filename="sample.log", level=logging.INFO)
