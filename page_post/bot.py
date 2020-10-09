from febu_bot.bot import FebuBotConfig
from .driver import driver


class Bot(FebuBotConfig):
    name = 'page_post'

    driver = driver
