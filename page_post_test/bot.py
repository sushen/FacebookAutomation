from febu_bot.bot import FebuBotConfig
from .driver import driver


class Bot(FebuBotConfig):
    name = 'Test Page Post Comment'
    driver = driver
