import pymongo
import logging
from cfg import db_link, db_collection_name
import datetime


class Storage:

    def __init__(self):
        self.client = pymongo.MongoClient(db_link)
        self.database = self.client[db_collection_name]
        self.urls = self.database.urls
        self.card_info = self.database.card_info

    def write_data_urls(self, data_to_write):
        if type(data_to_write) == dict:
            self.urls.insert_one(data_to_write)
        else:
            logging.info('[-] Exiting! Type of the data is not a dict!' + f'{datetime.datetime.now()}')
            exit(1)

    def write_data_info(self, info_to_write):
        if type(info_to_write) == dict:
            self.card_info.insert_one(info_to_write)
        else:
            logging.info('[-] Exiting! Type of the data is not a dict!' + f'{datetime.datetime.now()}')
            exit(1)

    def get_data(self):
        """"Func to get data from database"""
