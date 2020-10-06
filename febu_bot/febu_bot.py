# Copyright (c) 2020.
# Version : 5.0.0
# Script Author : Sushen Biswas, Fahim Al Islam
# Sushen Biswas Github Link : https://github.com/sushen
# Fahim Al Islam Github and Profile link (https://github.com/dev-fahim) (https://dev-fahim.github.io/me)
#
#  !/usr/bin python3
#  coding: utf-8


import sys
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from febu_bot.data_model import DataModel


class FacebookBot:
    driver: webdriver.Chrome = None
    data: DataModel = None
    wait_time = 2

    def __init__(self, data: DataModel = None, default_wait_time_in_sec=1):
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
        self.driver.get(self.data.facebook_login_url)
        if asked:
            input("#### Accepted cookies??? Then hit enter: ")
        self.driver.find_element_by_name("email").send_keys(self.data.username)
        self.wait()
        self.driver.find_element_by_name("pass").send_keys(self.data.password)
        self.wait()
        self.driver.find_element_by_name("login").click()
        self.wait()

    def goto_facebook_page(self):
        self.driver.implicitly_wait(self.wait_time)
        self.driver.get(self.data.facebook_business_page)
        self.wait()

    def goto_facebook_page_post(self, url=None):
        self.driver.implicitly_wait(self.wait_time)
        if url is None:
            self.driver.get(self.data.facebook_post_url)
        else:
            self.driver.get(url)
        self.wait()

    def react_like(self, is_wait=True):
        self.driver.implicitly_wait(self.wait_time)
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
