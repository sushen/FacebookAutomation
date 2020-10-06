import logging

from .driver import driver


def drive_bot():
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
