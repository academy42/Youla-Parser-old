from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
import requests
import selenium
import pymongo

PATH = 'https://youla.ru'

ADDITIONAL_URL = '/moskva/nedvijimost'

# request parameters
(deal_type, engine_version, offer_type, region, pg) = 'sale', 2, 'flat', -1, 1

params = {
        'deal_type': deal_type,
        'engine_version': engine_version,
        'offer_type': offer_type,
        'region': region,
        'p': pg
}

fake_user_agent = UserAgent()
DB_PASSW = 'Miler776775'



