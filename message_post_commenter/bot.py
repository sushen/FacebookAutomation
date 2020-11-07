from febu_bot.bot import FebuBotConfig
from .driver import driver


class Bot(FebuBotConfig):
    name = 'message_post_commenter'

    driver = driver
