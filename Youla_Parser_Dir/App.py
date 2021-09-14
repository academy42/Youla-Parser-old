#!/usr/bin/env python
from parser_core import Parser
import logging, datetime


class Application:
    def __init__(self):
        self.parser = Parser()
        logging.info('Application has been started ' + f'{datetime.datetime.now()}')

    def run(self):
        """Функция запуска приложенич"""

        self.parser.parse_cards_info()

    def stop(self):
        """Функия остановки всех процессов и функция приложения"""
        self.parser.driver.close()

