#  Copyright (c) 2020.
#  Version : 1.0.2
#  Script Author : Sushen Biswas
#
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

waiting_for_page = 2

# TODO: Put Your massage here
messages = [
    "You are welcome",
    "Thank you very much",
    "Thanks for your comment"
]


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
        options.add_argument('--user-data-dir="/home/fahim/.config/google-chrome"')
        options.add_argument('--profile-directory=Profile 1')
        options.add_argument('--incognito')

        try:
            if sys.platform.startswith('win32'):
                self.driver = webdriver.Chrome("./chromedriver.exe", options=options)
            else:
                self.driver = webdriver.Chrome('./chromedriver', options=options)
        except Exception as e:
            print(e)
            exit(1)

        self.data = data

    def wait(self, in_sec=None):
        time.sleep(in_sec) if in_sec is not None else time.sleep(self.wait_time)

    def login(self):
        self.driver.get(self.data.facebook_login_page)
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

    def check_it_exists_by_class(self, class_):
        try:
            self.driver.find_element_by_class_name(class_)
        except NoSuchElementException:
            return False
        return True

    def fill_text_input_by_xpath(self, xpath, text):
        self.driver.find_element_by_xpath(xpath).send_keys(text)

    def run_driver(self):
        pass


if __name__ == '__main__':
    dotenv.load_dotenv()

    username = os.environ.get('my_facebook_username')
    password = os.environ.get('my_facebook_password')

    febu_bot = FacebookBot(Data(username, password))

    febu_bot.login()

    febu_bot.goto_facebook_page_post()

    febu_bot.mouse_click('//*[@id="watch_feed"]/div/div[1]/div[1]/div/div[2]/div[3]/div[1]/div/div[1]/div/span[2]/div')
    # febu_bot.mouse_click('//*[@id="watch_feed"]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/span', 4)
    # febu_bot.mouse_click('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div['
    #                      '1]/div/div/div[1]/div/div[1]/div/div[1]')
    febu_bot.mouse_click('//*[@id="watch_feed"]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]')
    time.sleep(5)
    for profile in febu_bot.driver.find_elements_by_xpath('//*[@id="watch_feed"]/div/div[1]/div[1]/div/div[2]/div['
                                                          '3]/div[2]/div[2]/ul/li'):
        febu_bot.hover_element(profile.find_element_by_class_name('oajrlxb2'))
        time.sleep(3)
        card = febu_bot.driver.find_element_by_class_name('j34wkznp')
        time.sleep(1)

        if len(febu_bot.driver.find_elements_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div['
                                                      '2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div')) \
                == 2:
            time.sleep(2)
            canMessage = febu_bot.check_it_exists_by_class('k4urcfbm')
            time.sleep(1)
            if canMessage:
                # message = febu_bot.driver.find_element_by_class_name('k4urcfbm')
                febu_bot.mouse_click('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div['
                                     '1]/div/div/div[2]/div/div/div/div[1]/div/div')  # rq0escxv
                time.sleep(3)
                febu_bot.fill_text_input_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div['
                                                  '1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div['
                                                  '2]/div[1]/div/div/div/div/div[2]/div/div/div/div', 'Thanks')

    exit(0)
