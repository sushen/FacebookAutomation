#  Copyright (c) 2020.
#  Version : 3.0.2
#  Script Author : Sushen Biswas
#  Somehow we don't know this is highly edited by Fahim Al Islam (https://github.com/dev-fahim) (https://dev-fahim.github.io/me)
#  Sushen Biswas Github Link : https://github.com/sushen
#
#  !/usr/bin/env python
#  coding: utf-8

import os
import sys
import dotenv

from selenium import webdriver
import time
import random

# TODO: We have to wait for page
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import emoji

waiting_for_page = 2

# TODO: Put Your massage here
messages = [
    "You are welcome",
    "Thank you very much",
    "Thanks for your comment"
]

closeNow = False

class Data:
    username = None
    password = None

    facebook_login_page = "https://business.facebook.com/login/"
    facebook_business_page = "https://business.facebook.com/Sushen.Biswas.Creative.Director/"
    facebook_business_post_url = "https://www.facebook.com/watch/?v=1464445743765490&extid=01rZBI8pW3zsVEdD"
    facebook_business_page_post = "https://business.facebook.com/Sushen.Biswas.Creative.Director/posts/"

    def __init__(self,
                 facebook_username,
                 facebook_password,
                 facebook_login_page=None,
                 facebook_business_page=None,
                 facebook_business_post_url=None,
                 facebook_business_page_post=None):

        self.username = facebook_username
        self.password = facebook_password
        if facebook_login_page is not None:
            self.facebook_login_page = facebook_login_page
        if facebook_business_page is not None:
            self.facebook_business_page = facebook_business_page
        if facebook_business_post_url is not None:
            self.facebook_business_post_url = facebook_business_post_url
        if facebook_business_page_post is not None:
            self.facebook_business_page_post = facebook_business_page_post


class FacebookBot:
    driver: webdriver.Chrome = None
    data: Data = None
    wait_time = 2

    def __init__(self, data: Data = None, default_wait_time_in_sec=1):
        self.wait_time = default_wait_time_in_sec

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument('--incognito')

        try:
            if sys.platform.startswith('win32'):
                self.driver = webdriver.Chrome("./chromedriver.exe", options=options)
            else:
                options.add_argument('--user-data-dir="/home/fahim/.config/google-chrome"')
                options.add_argument('--profile-directory=Profile 1')
                self.driver = webdriver.Chrome('./chromedriver', options=options)
        except Exception as e:
            print(e)
            exit(1)

        self.data = data

    def wait(self, in_sec=None):
        time.sleep(in_sec) if in_sec is not None else time.sleep(self.wait_time)

    def login(self, asked=False):
        self.driver.get(self.data.facebook_login_page)
        if asked:
            input("#### Accepted cookies??? Then hit enter :")
        self.driver.find_element_by_name("email").send_keys(self.data.username)
        self.wait()
        self.driver.find_element_by_name("pass").send_keys(self.data.password)
        self.wait()
        self.driver.find_element_by_name("login").click()
        self.wait()

    def goto_facebook_page(self):
        self.driver.implicitly_wait(waiting_for_page)
        self.driver.get(self.data.facebook_business_page)
        self.wait()

    def goto_facebook_page_post(self, url=None):
        self.driver.implicitly_wait(waiting_for_page)
        if url is None:
            self.driver.get(self.data.facebook_business_post_url)
        else:
            self.driver.get(url)
        self.wait()

    def react_like(self, is_wait=True):
        self.driver.implicitly_wait(waiting_for_page)
        if is_wait:
            self.wait()

    def execute_script(self, script):
        self.driver.execute_script(script)

    def hover_element_xpath(self, xpath):
        centre = self.driver.find_element_by_xpath(xpath)
        hover = ActionChains(self.driver).move_to_element(centre)
        hover.perform()
        self.wait(1)

    def hover_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        self.wait(1)

    def hover_element_class(self, class_):
        centre = self.driver.find_element_by_class_name(class_)
        hover = ActionChains(self.driver).move_to_element(centre)
        hover.perform()

    def hover_element_id(self, id_):
        centre = self.driver.find_element_by_id(id_)
        hover = ActionChains(self.driver).move_to_element(centre)
        hover.perform()

    def mouse_click(self, xpath, wait=None, until=None):
        self.driver.find_element_by_xpath(xpath).click()
        if until is None:
            self.wait(wait) if wait is not None else self.wait(self.wait_time)
        else:
            until()

    def mouse_click_element(self, element, wait=None, until=None):
        element.click()
        if until is None:
            self.wait(wait) if wait is not None else self.wait(self.wait_time)
        else:
            until()

    def check_it_exists_by_class(self, class_):
        try:
            self.driver.find_element_by_class_name(class_)
        except NoSuchElementException:
            return False
        return True

    def check_it_exists(self, class_=None, id_=None, xpath_=None):
        try:
            if class_:
                self.driver.find_element_by_class_name(class_)
            elif id_:
                self.driver.find_element_by_id(id_)
            else:
                self.driver.find_element_by_xpath(xpath_)
        except NoSuchElementException:
            return False
        return True

    def fill_text_input_by_xpath(self, xpath, text):
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    def run_driver(self):
        pass


def run(febu_bot_: FacebookBot, feed_box_aria_):

    comments = feed_box_aria_.find_elements_by_xpath('//div[contains(@aria-label, "Comment by")]')

    i = 1
    for li in comments:
        print()
        print(f"========> Now in number {i} thread {emoji.emojize(':smirking_face:')} <========")
        message = random.choice(messages)
        if isYourPage:
            message_link = None
            try:
                message_link = li.find_element_by_xpath('//div[1]/div/div[2]/ul/li[3]/div[@role="button"]')
                febu_bot_.driver.execute_script("arguments[0].scrollIntoView();", message_link)
                print("====> Scrolled to the commenter")
                time.sleep(0.5)
            except Exception as e:
                print(f"====> Messagings are not available {emoji.emojize(':expressionless_face:')}")
                closeNow = True
                break

            time.sleep(1.3)
            febu_bot_.driver.execute_script("arguments[0].click();", message_link)
            print("====> Message button clicked")
            time.sleep(2)
            commenter = febu_bot_.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div['
                                                              '4]/div/div/div[1]/div/div[2]/div/div/div/div['
                                                              '1]/div/h2/span/span').text
            print(f"====> {emoji.emojize(':face_savoring_food:')} Sending Message to {commenter}")
            time.sleep(1)
            message_box = febu_bot_.driver.find_element_by_xpath('//div[contains(@aria-label, "Message")]')
            message_box_form = message_box.find_element_by_xpath(
                '//div/div[3]/div[2]/div[2]/span/div/div/div[2]/div/div/div/div')
            message_box_form.send_keys(message)
            print("====> Inputed the message with: " + message)
            time.sleep(1)
            febu_bot_.mouse_click(xpath='//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div['
                                       '2]/div/div/div/div[4]/div[2]/div')
            print("====> Send message button clicked")
            time.sleep(5)
            print(f"====> {emoji.emojize(':face_savoring_food:')} Message is sent ")
        else:
            febu_bot_.hover_element(li.find_element_by_class_name('oajrlxb2'))
            time.sleep(0.5)
        print(f"========> {emoji.emojize(':watermelon:')} Thread {i} is completed <========")
        i += 1
        time.sleep(5)
        print()


if __name__ == '__main__':
    print()
    print()
    print(f"************ Facebook page post auto message bot {emoji.emojize(':robot:')} ************")
    dotenv.load_dotenv()
    messages = []
    with open("./messages.txt") as f:
        for line in f:
            messages.append(line.split('\n')[0])

    print(">>>>>>>> All messages are loaded!!!")

    time.sleep(2)
    print(">>>>>>>> STARTED!!! " + emoji.emojize(':winking_face_with_tongue:'))

    is2FA = bool(int(input('#### Do you need 2FA? type 1 for yes and 0 for no: ')))
    isYourPage = bool(int(input('#### Is this your page? type 1 for yes and 0 for no: ')))
    isCookieAsked = bool(int(input('#### Is this your cookie is been asked? type 1 for yes and 0 for no: ')))
    isSilent = bool(int(input('#### Do you want to run this silently? type 1 for yes and 0 for no: ')))

    username = os.environ.get('my_facebook_username')
    password = os.environ.get('my_facebook_password')

    data = Data(username, password)
    post_url = input("#### Your post URL: ")
    data.facebook_business_post_url = post_url

    febu_bot = FacebookBot(data)

    febu_bot.login(asked=isCookieAsked)

    if is2FA:
        input("#### Enter after your work is done: ")
    print(f"==> Logged in {emoji.emojize(':smiling_face_with_sunglasses:')}")

    febu_bot.goto_facebook_page_post()
    print("==> Now in page post")

    time.sleep(2)

    feed_box_aria = febu_bot.driver.find_element_by_xpath("//div[@data-testid='Keycommand_wrapper_feed_story']")

    comments_button = "//div[@aria-label='Leave a comment']"

    febu_bot.mouse_click(comments_button)
    print("==> Clicked the comments button")

    time.sleep(3)

    i = 1
    while closeNow:
        print(f"==========> Executing {1} <============")

        if i > 1 and isSilent is False:
            febu_bot.driver.execute_script('window.alert("Click ok then in command ans. question to load more comments '
                                           'and run again");')
            load_more = bool(int(input("#### Load more comments? type 1 for yes and 0 for no: ")))
        else:
            load_more = True

        if load_more is False:
            break
        else:
            try:
                view_comments = febu_bot.driver.find_element_by_xpath(
                    '//span/span[contains(text(), "View") and contains(text(), "comments")]')
                febu_bot.driver.execute_script("arguments[0].scrollIntoView();", view_comments)
                time.sleep(1)
                febu_bot.driver.execute_script("arguments[0].click();", view_comments)
                print("==> Loading more comments")
                time.sleep(10)
                print("==> More comments are loaded")
            except Exception as e:
                print(e)
                print("==> No More comments")

            run(febu_bot, feed_box_aria)

            i += 1


"""
    for profile in febu_bot_.driver.find_elements_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div['
                                                          '1]/div[1]/div[4]/div['
                                                          '1]/div/div/div/div/div/div/div/div/div[1]/div/div['
                                                          '2]/div/div[4]/div/div/div[2]/ul/li'):
        febu_bot_.hover_element(profile.find_element_by_class_name('oajrlxb2'))

        time.sleep(3)

        if len(febu_bot_.driver.find_elements_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div['
                                                      '2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div')) \
                == 2:
            canMessage = febu_bot_.check_it_exists_by_class('k4urcfbm')

            if canMessage:
                # message = febu_bot_.driver.find_element_by_class_name('k4urcfbm')
                febu_bot_.mouse_click('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div['
                                     '1]/div/div/div[2]/div/div/div/div[1]/div/div')  # rq0escxv
                time.sleep(3)
                try:
                    febu_bot_.fill_text_input_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div['
                                                      '1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div['
                                                      '3]/div[ '
                                                      '2]/div[1]/div/div/div/div/div[2]/div/div/div/div', 'Thanks')
                except NoSuchElementException as no_element_error:
                    print("Already messaged")
                    continue

    exit(0)
"""