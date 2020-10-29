import os
import random
import time

import emoji
from selenium.common.exceptions import NoSuchElementException

from febu_bot.febu_bot import FacebookBot


def run(febu_bot_: FacebookBot, feed_box_aria_, isYourPage, messages):
    comments = feed_box_aria_.find_elements_by_xpath('//div[contains(@aria-label, "Comment by")]')
    print(len(comments))
    # i = 1
    # for li in comments:
    #     print()
    #     message = random.choice(messages)
    #     if isYourPage:
    #         try:
    #             message_link = li.find_element_by_xpath('//div[1]/div/div[2]/ul/li[3]/div[@role="button"]')
    #             print(f"========> Now in number {i} thread {emoji.emojize(':smirking_face:')} <========")
    #             febu_bot_.driver.execute_script("arguments[0].scrollIntoView();", message_link)
    #             print("====> Scrolled to the commenter")
    #             time.sleep(0.5)
    #         except NoSuchElementException:
    #             print(f"====> Messaging are not available anymore {emoji.emojize(':expressionless_face:')}")
    #             print()
    #             print()
    #             break
    #
    #         time.sleep(1.3)
    #         febu_bot_.driver.execute_script("arguments[0].click();", message_link)
    #         print("====> Message button clicked")
    #         time.sleep(2)
    #         commenter = febu_bot_.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div['
    #                                                            '4]/div/div/div[1]/div/div[2]/div/div/div/div['
    #                                                            '1]/div/h2/span/span').text
    #         print(f"====> {emoji.emojize(':face_savoring_food:')} Sending Message to {commenter}")
    #         time.sleep(1)
    #         message_box = febu_bot_.driver.find_element_by_xpath('//div[contains(@aria-label, "Message")]')
    #         message_box_form = message_box.find_element_by_xpath(
    #             '//div/div[3]/div[2]/div[2]/span/div/div/div[2]/div/div/div/div')
    #         message_box_form.send_keys(message)
    #         print("====> Filled with message: " + message)
    #         time.sleep(1)
    #         febu_bot_.mouse_click(xpath='//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div['
    #                                     '2]/div/div/div/div[4]/div[2]/div')
    #         print("====> Send message button clicked")
    #         time.sleep(5)
    #         print(f"====> {emoji.emojize(':face_savoring_food:')} Message is sent ")
    #     else:
    #         febu_bot_.hover_element(li.find_element_by_class_name('oajrlxb2'))
    #         time.sleep(0.5)
    #     print(f"========> {emoji.emojize(':smirking_face:')} Thread {i} is completed <========")
    #     i += 1
    #     time.sleep(5)
    #     print()


def driver():

    messages = []
    with open("./messages.txt") as f:
        for line in f:
            messages.append(line.split('\n')[0])

    print(">>>>>>>> All messages are loaded!!!")

    is2_fa = bool(int(input('#### Do you need 2FA? type 1 for yes and 0 for no: ')))
    is_your_page = bool(int(input('#### Is this your page? type 1 for yes and 0 for no: ')))
    is_cookie_asked = bool(int(input('#### Is this your cookie is been asked? type 1 for yes and 0 for no: ')))
    is_silent = bool(int(input('#### Do you want to run this silently? type 1 for yes and 0 for no: ')))

    username = os.environ.get('my_facebook_username')
    password = os.environ.get('my_facebook_password')

    post_url = input("#### Your post URL: ")

    febu_bot = FacebookBot()

    febu_bot.login(
        username=username,
        password=password,
        asked=is_cookie_asked,
        is2Fa=is2_fa,
        url='https://business.facebook.com/login'
    )

    febu_bot.goto_facebook_page_post(url=post_url)

    time.sleep(2)

    # data-testid='newsFeedStream' ==== Bangladesh
    feed_box_aria = febu_bot.driver.find_element_by_xpath("//div[@data-testid='newsFeedStream']")
    
    # feed_box_aria = febu_bot.driver.find_element_by_xpath("//div[@data-testid='Keycommand_wrapper_feed_story']")

    comments_button = "//a[@title='Leave a comment']" # This is for Bangladesh
    
    # comments_button = "//div[@aria-label='Leave a comment']"
    
    # //body/div[@id='u_0_2k']/div[@id='globalContainer']/div[@id='content']/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[2]/div[2]/span[2]/a[1]
    
    
     

    febu_bot.mouse_click(comments_button)
    print("==> Clicked the comments button")

    time.sleep(3)

    i = 1
    while True:
        print(f"==========> Executing {i} <============")

        if i > 1 and is_silent is False:
            febu_bot.driver.execute_script('window.alert("Click ok then in command ans. question to load more comments '
                                           'and run again");')
            load_more = bool(int(input("#### Load more comments? type 1 for yes and 0 for no: ")))
        else:
            load_more = True

        if load_more is False:
            break
        else:
            try:
                
                view_comments = feed_box_aria.find_element_by_xpath('//span[contains(text(), "View") and contains(text(), "comments")]') # For Bangladesh
                # view_comments = feed_box_aria.find_element_by_xpath('//span/span[contains(text(), "View") and contains(text(), "comments")]')
                febu_bot.driver.execute_script("arguments[0].scrollIntoView();", view_comments)
                time.sleep(1)
                febu_bot.driver.execute_script("arguments[0].click();", view_comments)
                print("==> Loading more comments")
                time.sleep(10)
                print("==> More comments are loaded")
            except NoSuchElementException:
                print("==> No More comments")
                break

            run(febu_bot, feed_box_aria, is_your_page, messages)

            i += 1
