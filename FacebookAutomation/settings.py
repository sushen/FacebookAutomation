import os
import message_post_commenter
import page_post
import page_post_test
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BOTS = [
    message_post_commenter.Bot,
    page_post.Bot,
    page_post_test.Bot,
    
]

DEFAULT_BOT = 1

LOG_LEVEL = logging.DEBUG
