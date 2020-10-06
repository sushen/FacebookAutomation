import os
import time

import dotenv

from febu_bot.data_model import DataModel
from febu_bot.febu_bot import FacebookBot


def page_post_message():
    dotenv.load_dotenv()

    is2FA = bool(int(input('Do you need 2FA? type 1 for yes and 0 for no: ')))
    isYourPage = bool(int(input('Is this your page? type 1 for yes and 0 for no: ')))
    post_url = input("Your post URL: ")

    username = os.environ.get('my_facebook_username')
    password = os.environ.get('my_facebook_password')

    data = DataModel(username, password)
    data.facebook_business_post_url = post_url

    febu_bot = FacebookBot(data)

    febu_bot.login()

    if is2FA:
        input("Enter after your work is done:")

    febu_bot.goto_facebook_page_post()

    feed_box_aria = febu_bot.driver.find_element_by_xpath("//div[@data-testid='Keycommand_wrapper_feed_story']")

    comments_button = "//div[@aria-label='Leave a comment']"

    febu_bot.mouse_click(comments_button)

    time.sleep(3)

    comments = feed_box_aria.find_elements_by_xpath('//div[contains(@aria-label, "Comment by")]')

    for li in comments:
        if isYourPage:
            try:
                message_link = li.find_element_by_xpath('//div[1]/div/div[2]/ul/li[3]/div[@role="button"]')
            except Exception as e:
                print(e)
                print("Not found")
                continue

            print("Found")
            message_link.click()
            time.sleep(0.8)
            message_box = febu_bot.driver.find_element_by_xpath('//div[contains(@aria-label, "Message")]')
            message_box_form = message_box.find_element_by_xpath(
                '//div/div[3]/div[2]/div[2]/span/div/div/div[2]/div/div/div/div')
            message_box_form.send_keys('It worked')
            time.sleep(1)
            febu_bot.mouse_click(xpath='//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div['
                                       '2]/div/div/div/div[4]/div[2]/div')
            time.sleep(5)
        else:
            febu_bot.hover_element(li.find_element_by_class_name('oajrlxb2'))
            time.sleep(0.5)
    exit(0)
