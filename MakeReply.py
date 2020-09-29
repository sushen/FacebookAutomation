# https://www.facebook.com/watch/?v=298300894651113&extid=VX1anIwOK2v1V7mL

import os
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
#time.sleep(4)


driver.get("https://www.facebook.com")
# I use environment veriable base on this tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
username = os.environ.get('fake_facebook_email')
password = os.environ.get('fake_facebook_pass')

driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_name("pass").send_keys(password)
driver.find_element_by_name("login").click()
#time.sleep(4)

#TODO: Go to the Post link
driver.get("https://www.facebook.com/watch/?v=1464445743765490&extid=01rZBI8pW3zsVEdD")
#time.sleep(4)

#TODO: Start Replying


#TODO: Close

