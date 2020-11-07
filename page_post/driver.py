#  for trigger button roles in every comments of a page post

import os
import time

from febu_bot.febu_bot import FacebookBot, FebuCommenter, TRIGGER


def driver():

    febu_bot = FacebookBot()
    
    febu_bot.login(
        url='https://business.facebook.com/login',
        username=os.environ.get('my_facebook_username'),
        password=os.environ.get('my_facebook_password'),
        asked=False,
        is2Fa=False
    )

    febu_bot.goto_facebook_page_post(os.environ.get('post_link'))

    time.sleep(5)

    bot = FebuCommenter(febu_bot)

    commenter_list = bot.get_commenter_actions_list()
    print(commenter_list.__len__())
    i = 1
    for li in commenter_list:
        like_element = bot.commenter_action_element(TRIGGER.LIKE, li)
        time.sleep(1)
        bot.like(like_element)
        time.sleep(1)
        i += 1
    print(i)
