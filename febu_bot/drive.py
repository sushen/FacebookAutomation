import logging

from febu_bot.bot import FebuBotConfig
from febu_bot.start import start
from .conf.settings import *


def drive_bot(index=None):

    logging.basicConfig(filename='./errors.log', level=mod.LOG_LEVEL,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger = logging.getLogger(__name__)

    try:
        if index is None:
            index = mod.DEFAULT_BOT
        bot: FebuBotConfig = mod.BOTS[index - 1]
        start(bot.name)
        bot.driver()
    except Exception as e:
        logger.error(e)
        print()
        print("============> Error occurred. See errors.log <============")
        exit(129)

    print()
    print("============> Task completed!!! <============")
