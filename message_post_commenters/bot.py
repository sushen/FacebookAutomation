import logging

from febu_bot import VERSION
from .driver import driver
import sys


def drive_bot():
    argv = sys.argv
    if len(argv) > 1 and (argv[1] == '-v' or argv[1] == '--version'):
        print(VERSION)
        quit()
    logging.basicConfig(filename='./errors.log', level=logging.ERROR,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger = logging.getLogger(__name__)

    try:
        driver()
    except Exception as e:
        logger.error(e)
        print()
        print("============> Error occurred. See errors.log <============")
        exit(129)

    print()
    print("============> Task completed!!! <============")
