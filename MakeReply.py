#  Copyright (c) 2020.
#  Version : 1.0.2
#  Script Author : Sushen Biswas
#
#  Sushen Biswas Github Link : https://github.com/sushen
#
#  !/usr/bin/env python
#  coding: utf-8

import os
from selenium import webdriver
import time
import random


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# chrome_options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

# driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
#time.sleep(4)


# driver.get("https://www.facebook.com")
# I use environment veriable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
username = os.environ.get('my_facebook_username')
password = os.environ.get('my_facebook_password')

# driver.find_element_by_name("email").send_keys(username)
# driver.find_element_by_name("pass").send_keys(password)
# driver.find_element_by_name("login").click()
# time.sleep(2)

messages = [
    "You are welcome",
    "Thank you very much",
    "Thanks for your comment"
]

#TODO: Go to the Post link


class FacebookBot():
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)

        
    def login(self):
        self.driver.get("https://www.facebook.com")
        self.driver.find_element_by_name("email").send_keys(username)
        self.driver.find_element_by_name("pass").send_keys(password)
        self.driver.find_element_by_name("login").click()

        # self.driver.get("https://www.facebook.com/profile.php?id=100052136962146")
        # self.driver.close(self)


    def comment_watchVideoLink(self,videoLink):
        self.driver.get(videoLink)
        while True:
            time.sleep(0.5)
            try:
                cmnt_btn = self.driver.find_element_by_xpath('//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div/div/div[2]/div/div[3]/div/span')
                cmnt_btn.click()
                break;
            except Exception:
                pass
        
      
        time.sleep(1)
        while True:
            time.sleep(1)
            try:
                show_cmnt = self.driver.find_element_by_xpath('//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[1]/div[2]/div/span/div/div/i')  
                show_cmnt.click()
                all_cmnt = self.driver.find_element_by_xpath('//*[@id="watch_feed"]/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/div[1]/div/div[1]/span')
                all_cmnt.click()
                break;
            except Exception:
                pass
        
    
    def botComment(self,comment):
        index = 1
        while True:
            time.sleep(15)
            try:
                reply_x_path = '//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/ul/li[{}]/div[1]/div/div[2]/ul/li[2]/div'.format(index)
                reply_btn = self.driver.find_element_by_xpath(reply_x_path)
                reply_btn.click()
                
                while True:
                    time.sleep(15)
                    try:  
                        msg_x_path = '//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/ul/li[{}]/div[2]/div/div[2]/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div'.format(index)
                        msg_box = self.driver.find_element_by_xpath(msg_x_path)
                        msg_box.send_keys(comment+"\n")
                        break;
                        
                    except Exception:
                        pass
                index += 1
            except Exception:
                more_btn = vc = self.driver.find_element_by_xpath('//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/span/span')
                more_btn.click()
            
        


fb = FacebookBot()
fb.login()
input("You have to login and Put your 2 step auth and write 0 and enter  : \n")
fb.comment_watchVideoLink("https://www.facebook.com/watch/?v=1464445743765490&extid=01rZBI8pW3zsVEdD")

#TODO: Check option two
#fb.botComment("Thats is awesome")
fb.botComment(random.choice(messages))

    
    


#time.sleep(4)

#TODO: 1.Start Replying and Scape if alrady reply

#TODO: 2.Delet

#TODO: Like



#TODO: Close

