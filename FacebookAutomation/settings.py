import os
import message_post_commenter
import page_post
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BOTS = [
    message_post_commenter.Bot,
    page_post.Bot
]

DEFAULT_BOT = 2

LOG_LEVEL = logging.DEBUG
