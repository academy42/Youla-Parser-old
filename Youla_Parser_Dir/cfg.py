import logging
import os

PATH = 'https://youla.ru'

ADDITIONAL_URL = '/moskva/nedvijimost/prodaja-kvartiri'

HUB_HOST = '0.0.0.0'
MONGO_HOST = os.environ['MONGO_HOST']

headers = {
    'user-agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47',
    'Referer': 'https://youla.ru/'
}

db_link = f"mongodb://{MONGO_HOST}:27017/"

db_collection_name = "Parser_Data"

logging.basicConfig(filename="logs.log", level=logging.INFO)
