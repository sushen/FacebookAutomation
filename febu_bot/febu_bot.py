# Copyright (c) 2020.
# Version : 5.1.0
# Script Author : Sushen Biswas, Fahim Al Islam
# Sushen Biswas Github Link : https://github.com/sushen
# Fahim Al Islam Github and Profile link (https://github.com/dev-fahim) (https://dev-fahim.github.io/me)
#
#  !/usr/bin python3
#  coding: utf-8
import enum
import sys
import time

import emoji
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement


class FacebookBot:
    driver: webdriver.Chrome = None
    wait_time = 2

    def __init__(self, default_wait_time_in_sec=1):
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

    def wait(self, in_sec=None):
        time.sleep(in_sec) if in_sec is not None else time.sleep(self.wait_time)

    def login(self, url, username, password, asked=False, is2Fa=False):
        print("==> Now in login page")
        self.driver.get(url)
        if asked:
            input("#### Accepted cookies??? Then hit enter: ")
        self.driver.find_element_by_name("email").send_keys(username)
        self.wait()
        self.driver.find_element_by_name("pass").send_keys(password)
        self.wait()
        self.driver.find_element_by_name("login").click()
        self.wait()
        if is2Fa:
            input("#### Hit enter after your work is done: ")
        print(f"==> Logged in {emoji.emojize(':smiling_face_with_sunglasses:')}")

    def goto_facebook_page_post(self, url):
        self.driver.implicitly_wait(self.wait_time)
        self.driver.get(url)
        self.wait()
        print("==> Now in page post")

    def execute_script(self, script):
        self.driver.execute_script(script)

    def hover_element_xpath(self, xpath):
        centre = self.driver.find_element_by_xpath(xpath)
        hover = ActionChains(self.driver).move_to_element(centre)
        hover.perform()
        self.wait(3)

    def hover_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()
        self.wait(3)


    def hover_element_class(self, class_):
        centre = self.driver.find_element_by_class_name(class_)
        hover = ActionChains(self.driver).move_to_element(centre)
        hover.perform()
        self.wait(3)

    def hover_element_id(self, id_):
        centre = self.driver.find_element_by_id(id_)
        hover = ActionChains(self.driver).move_to_element(centre)
        hover.perform()
        self.wait(3)

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


class TRIGGER(enum.Enum):
    LIKE = 1
    REPLY = 2
    MESSAGE = 3
    DATE = 4
    EDIT = 5


class FebuCommenter:
    feed_box_area = None
    browser = None

    def __init__(self, febu_bot: FacebookBot):
        self.browser = febu_bot
        # role='main' ===== Bangladesh Page Post 
        self.feed_box_area = self.browser.driver.find_element_by_xpath("//div[@role='main']")
        
        #role='article' =====  
        # self.feed_box_area = self.browser.driver.find_element_by_xpath("//div[@role='article']")
        # self.feed_box_area = self.browser.driver.find_element_by_xpath("//div[@data-testid""='Keycommand_wrapper_feed_story']")

    def get_feed_box_area(self):
        return self.feed_box_area

    def set_feed_box_area(self, feed_box_area_xpath):
        self.feed_box_area = self.browser.driver.find_element_by_xpath(feed_box_area_xpath)

    def get_commenter_actions_list(self):
        return self.feed_box_area.find_elements_by_xpath('//div[contains(@aria-label, "Comment by") and @role="article"]')
        # return self.feed_box_area.find_elements_by_xpath('//div[contains(@aria-label, "Comment by") and ''@role="article"]')

    @staticmethod
    def commenter_action_element(trigger_type: TRIGGER, commenter: WebElement):
        trigger_link = None
        try:
            if trigger_type == TRIGGER.LIKE:
                trigger_link = commenter.find_element_by_xpath('//div[text()="Like"]')
        except NoSuchElementException as e:
            print("Like button not found by the FebuBot")

        return trigger_link

    def like(self, trigger_link):
        print()
        self.scroll(trigger_link)
        time.sleep(2)
        self.click(trigger_link)
        time.sleep(1)
        print(f"==> Liked")
        print()

    def scroll(self, element):
        self.browser.driver.execute_script("arguments[0].scrollIntoView();", element)
        print(f"==> Scrolled")

    def click(self, element):
        self.browser.driver.execute_script("arguments[0].click();", element)
        print(f"==> Clicked")
