import logging
from selenium.webdriver import FirefoxOptions

PATH = 'https://youla.ru'

ADDITIONAL_URL = '/moskva/nedvijimost'

HUB_HOST = 'selenium-hub'
MONGO_HOST = 'localhost'

headers = {
    'user-agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47',
    'Referer': 'https://youla.ru/'
}

db_link = f"mongodb://{MONGO_HOST}:27017/"

db_collection_name = "Parser_Data"

logging.basicConfig(filename="logs.log", level=logging.INFO)

firefox_options = FirefoxOptions()
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('window-size=1200x600')
firefox_options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"')

attribute_dict = {
            "tip_sdelki": "task",
            "name": "name",
            "description": "text",
            "price": "cost",
            "realty_obshaya_ploshad": "totalarea",
            "realty_ploshad_kuhni": "kitchenarea",
            "komnat_v_kvartire": "roomquantity",
            "realty_etaj": "floor",
            "realty_etajnost_doma": "floors",
            "sobstvennik_ili_agent": "is_agent",
            "realty_building_type": "housing",
            "realty_hidden_location": "street",
            "posudomoechnaya_mashina": "dishWasher",
            "holodilnik": "refr",
            "remont": "repair",
            "lift": "cargoLift",
            "realty_god_postroyki": "buildYear",
        }