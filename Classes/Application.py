#!/usr/bin/env python
from Parser import Parser


class Application:
    def __init__(self):
        self.parser = Parser()

    def run(self):
        """Функция запуска приложенич"""
        self.parser.parse_cards_info()

    def stop(self):
        """Функия остановки всех процессов и функция приложения"""
