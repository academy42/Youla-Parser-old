#!/usr/bin/env python
import logging
from cfg import *

from Application import Application


def main():
    app = Application()
    app.run()
    logging.info("The program has started")


if __name__ == "__main__":
    main()
