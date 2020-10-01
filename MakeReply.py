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

#TODO: We have to wait for page
waiting_for_page = 4

#TODO: Put Your massage here
messages = [
    "You are welcome",
    "Thank you very much",
    "Thanks for your comment"
]

#TODO: Go to the Post link
post_url = "https://www.facebook.com/watch/?v=1464445743765490&extid=01rZBI8pW3zsVEdD"


class FacebookBot():
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
        self.profile_reference = ''
    def login(self):
        self.driver.get("https://www.facebook.com")
        self.driver.find_element_by_name("email").send_keys("eyyidxf633@lefaqr5.com")
        time.sleep(2)
        self.driver.find_element_by_name("pass").send_keys("#3#3#3")
        time.sleep(2)
        self.driver.find_element_by_name("login").click()
        
        try:   
            notnowBtn = self.driver.find_element_by_xpath('//*[@id="notNowBox"]/label/input')
            notnowBtn.click()   
        except Exception:
            pass  
            
        
            
        # self.driver.get("https://www.facebook.com/profile.php?id=100052136962146")
        # self.driver.close(self)

    def setProfileUrl(self):
        time.sleep(5)
        try:   
            pro = self.driver.find_element_by_xpath('//*[@id="u_0_a"]/div[1]/div[1]/div/a')
            self.profile_reference = pro.get_attribute('href')
            
            print(self.profile_reference)
        except Exception:
            print(Exception)
            pass

    def comment_watchVideoLink(self,videoLink):
        

        self.driver.get(videoLink)
        while True:
            time.sleep(2)
            try:
                cmnt_btn = self.driver.find_element_by_xpath('//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div/div/div[2]/div/div[3]/div/span')
                cmnt_btn.click()
                break;
            except Exception:
                pass
        
        # time.sleep(10)
        while True:
            time.sleep(waiting_for_page)
            try:
                show_cmnt = self.driver.find_element_by_xpath('//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[1]/div[2]/div/span/div/div/i')  
                show_cmnt.click()
                time.sleep(waiting_for_page)
                all_cmnt = self.driver.find_element_by_xpath('//*[@id="watch_feed"]/div/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/div[1]/div/div[1]/span')
                all_cmnt.click()
                break;
            except Exception:
                pass
        
    
    def botComment(self,comment):
        index = 1
        while True:
            time.sleep(waiting_for_page)
            try:
                reply_x_path = '//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/ul/li[{}]/div[1]/div/div[2]/ul/li[2]/div'.format(index)
                reply_btn = self.driver.find_element_by_xpath(reply_x_path)
                reply_btn.click()
                comment_List_count = 1
                profile_found = False
                author_found = 0;
                while True:
                    time.sleep(5)
                    ch_list = '//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/ul/li[{}]/div[2]/div/ul/li[{}]/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/a'.format(index,comment_List_count)
                    try:
                        
                        ha = self.driver.find_element_by_xpath(ch_list)
                        profile_link = ha.get_attribute('href')
                        # print(profile_link)
                        # print(self.profile_reference)
                        pr = profile_link.split("&")
                        profile_ref = pr[0].strip()
                        if self.profile_reference == profile_ref:
                            profile_found = True
                            break;    
                        comment_List_count += 1
                    except Exception:
                        try:
                            more_reply_xpath = '//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/ul/li[{}]/div[2]/div/div/div/div[2]/span[2]/span'.format(index)
                            more_reply_btn = self.driver.find_element_by_xpath(more_reply_xpath)
                            more_reply_btn.click()
                          
                        except Exception:
                            author_path = '//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/ul/li[{}]/div[2]/div/ul/li/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/a'.format(index)
                            
                            if author_found == 1:
                                break;
                            
                            try:
                                author = self.driver.find_element_by_xpath(author_path)
                                comment_List_count += 1
                                author_found += 1
                            except Exception:
                                break; 
                    
                    
                if not profile_found:
                    while True:
                        time.sleep(1)
                        try:  
                            msg_x_path = '//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/ul/li[{}]/div[2]/div/div[2]/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div'.format(index)
                            msg_box = self.driver.find_element_by_xpath(msg_x_path)
                            msg = random.choice(comment)
                            msg_box.send_keys(msg+"\n")
                            break;

                        except Exception:
                            pass
                index += 1
            except Exception:
                more_btn = vc = self.driver.find_element_by_xpath('//*[@id="watch_feed"]/div/div[1]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/div/div[1]/div[2]/span/span')
                more_btn.click()
        


fb = FacebookBot()
time.sleep(waiting_for_page)
fb.login()
time.sleep(2)
fb.setProfileUrl()
#TODO: Make a yes no gate

input("You have to login and Put your 2 step auth and write 0 and enter  : \n")

time.sleep(waiting_for_page)
# post_url = "https://www.facebook.com/watch/?v=1464445743765490&extid=01rZBI8pW3zsVEdD"
fb.comment_watchVideoLink(post_url)

#TODO: Check option two
input("Do you want to start commenting then write 0 and enter  : \n")
# time.sleep(10)
fb.botComment(messages)
    


#time.sleep(4)

#TODO: 1.Start Replying and Scape if alrady reply

#TODO: 2.Delet

#TODO: Like

#TODO: Close After Work

# messages = ["You are welcome","Thank you very much","Thanks for your comment"]
