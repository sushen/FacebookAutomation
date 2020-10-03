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

dotenv.load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# chrome_options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

# driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
# time.sleep(4)


# driver.get("https://www.facebook.com")
# I use environment variable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
username = os.environ.get('my_facebook_username')
password = os.environ.get('my_facebook_password')

# driver.find_element_by_name("email").send_keys(username)
# driver.find_element_by_name("pass").send_keys(password)
# driver.find_element_by_name("login").click()

# time.sleep(2)

# TODO: We have to wait for page
waiting_for_page = 2

# TODO: Put Your massage here
messages = [
    "You are welcome",
    "Thank you very much",
    "Thanks for your comment"
]

# TODO: Go to the Post link
facebook_login_page = "https://business.facebook.com/login/"
facebook_business_page = "https://business.facebook.com/Sushen.Biswas.Creative.Director/"
facebook_business_post_url = "https://www.facebook.com/watch/?v=1464445743765490&extid=01rZBI8pW3zsVEdD"
facebook_business_page_post = "https://business.facebook.com/Sushen.Biswas.Creative.Director/posts/"


class FacebookBot:
    def __init__(self):
        if sys.platform.startswith('win32'):
            self.driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
        else:
            self.driver = webdriver.Chrome(options=options)
        # self.profile_reference = ''

    def login(self):
        self.driver.get(facebook_login_page)
        self.driver.find_element_by_name("email").send_keys(username)
        time.sleep(2)
        self.driver.find_element_by_name("pass").send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_name("login").click()

    def facebook_page(self):
        self.driver.implicitly_wait(waiting_for_page)
        self.driver.get(facebook_business_page)

    def facebook_page_post(self):
        self.driver.implicitly_wait(waiting_for_page)
        self.driver.get(facebook_business_page_post)

    def like(self):
        self.driver.execute_script('window.console.log("Hello vaia");')
        self.driver.implicitly_wait(waiting_for_page)
        # self.driver.find_element_by_xpath("//span[contains(text())='Like']").is_displayed()
        # self.driver.find_element_by_xpath("//span[contains(text())='Like']").is_enabled()

    def auto_scroll(self):
        while True:
            self.driver.implicitly_wait(waiting_for_page)


fb = FacebookBot()
time.sleep(waiting_for_page)
fb.login()
input("After your 2 step authentication enter 0 : ")
# fb.facebook_page()
# input("After your facebook_page enter o : ")
fb.facebook_page_post()
input("After your facebook_page_post enter 0 : ")
fb.like()
input("After like facebook page post enter 0 : ")
