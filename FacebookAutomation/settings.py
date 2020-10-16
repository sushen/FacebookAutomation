import os
import message_post_commenter
import page_post
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BOTS = [
    message_post_commenter.Bot,
    message_post_commenter
]

DEFAULT_BOT = 1

LOG_LEVEL = logging.DEBUG
