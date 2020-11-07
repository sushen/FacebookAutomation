import os
import random
import time

import dotenv
import emoji
from selenium.common.exceptions import NoSuchElementException

from febu_bot import VERSION
from febu_bot.data_model import DataModel
from febu_bot.febu_bot import FacebookBot 
from febu_bot.custom_xpath import CustomXpath






def run(febu_bot_: FacebookBot, feed_box_aria_, isYourPage, messages,custom_xpath_:CustomXpath):
    
    # comments = feed_box_aria_.find_elements_by_xpath('//div[contains(@aria-label, "Comment")]') # for Bangladesh page
    comments = feed_box_aria_.find_elements_by_xpath('//div[contains(@aria-label, "Comment by")]')

    i = 1
    
    for li in comments:
        print()
        message = random.choice(messages)
        if isYourPage:
            try:
                # person_link = li.find_element_by_xpath('//div/a[contains(@data-hovercard,"/ajax/hovercard/user.php")]')
                
                # febu_bot_.hover_element(person_link)
                # for Bangladesh
                # message_link = li.find_element_by_xpath('//a[@role="button" and starts-with(@href, "/messages/") and @rel="dialog" and starts-with(text(), "Message")]') 
                message_link = li.find_element_by_xpath('//div[1]/div/div[2]/ul/li[3]/div[@role="button"]')
                # message_link = li.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/ul/li[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/a')
                
                print(f"========> Now in number {i} thread {emoji.emojize(':smirking_face:')} <========")
                febu_bot_.driver.execute_script("arguments[0].scrollIntoView();", message_link)
                print("====> Scrolled to the commenter")
                time.sleep(0.5)
            except NoSuchElementException:
                print(f"====> Messaging are not available anymore {emoji.emojize(':expressionless_face:')}")
                print()
              

            time.sleep(1)
            febu_bot_.driver.execute_script("arguments[0].click();", message_link)
            print("====> Message button clicked")
            time.sleep(2)
            
            # commenter = febu_bot_.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div/h2/span/span').text
            
            # print(f"====> {emoji.emojize(':face_savoring_food:')} Sending Message to {commenter}")
            time.sleep(1)
            message_box = febu_bot_.driver.find_element_by_xpath('//div[contains(@aria-label, "Message")]')
            message_box_form = message_box.find_element_by_xpath('//div/div[3]/div[2]/div[2]/span/div/div/div[2]/div/div/div/div')
            
            message_box_form.send_keys(message)
            print("====> Filled with message: " + message)
            time.sleep(1)
            febu_bot_.mouse_click(xpath='//*[@id="mount_0_0"]/div/div[1]/div[1]/div[5]/*//form/div/div[3]/div[2]/div[1]/div/div/div/div/*//div/div/div/div')
            # febu_bot_.mouse_click(xpath='//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[4]/div[2]/div') # 0ld
            
            print("====> Send message button clicked")
            time.sleep(1)
            print(f"====> {emoji.emojize(':face_savoring_food:')} Message is sent ")
        else:
            
            personLink = febu_bot_.hover_element(li.find_element_by_class_name('oajrlxb2'))

            time.sleep(5)
            try:
                message_box = febu_bot_.driver.find_element_by_xpath('//div[@aria-label="Message" and @tabindex="-1"]') 
                time.sleep(5)
                try:
                    febu_bot_.driver.execute_script("arguments[0].click();", message_box)
                except NoSuchElementException:
                    pass
            except NoSuchElementException:
                print("Hover message box not found")
        
            try:
                time.sleep(5)
                # custom_xpath_.set_person_message_xpath_list('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[5]/*//form/div/div[3]/div[2]/div[1]/div/div/div/div/*//div/div/div/div')
                xpath_list = custom_xpath_.get_person_message_xpath_list()
                message_box_form =  febu_bot_.driver.find_element_by_xpath(xpath_list[0])   
                try:                
                    time.sleep(5)  
                    message_box_form.send_keys(message)
                
                    time.sleep(2)
                    message_box_form.send_keys(u'\ue007')
                    
                    print("====> Filled with message: " + message)
                    print(f"====> {emoji.emojize(':face_savoring_food:')} Message Sent Succesful ")
                    time.sleep(2)
                    febu_bot_.mouse_click(xpath='//div[@aria-label="Close chat"]')
                    print("Chat closed")
                
                except NoSuchElementException:
                    print('message box form not found') 
                                     
            except NoSuchElementException:
               pass       
                             
        print(f"========> {emoji.emojize(':smirking_face:')} Thread {i} is completed <========")
        i += 1
        time.sleep(5)
        print()


def driver():
    print()
    print()

    print(f"******** Facebook page post auto message bot \U0001F600 {VERSION} **********")

    print(f"********* Facebook page message bot \U0001F600 {VERSION} *********")
    
    dotenv.load_dotenv()
    messages = []
    
    with open("./messages.txt", encoding="utf-8") as f:
        for line in f:
            messages.append(line.split('\n')[0])

    print(">>>>>>>> All messages are loaded!!!")

    time.sleep(2)
    
    print(">>>>>>>> STARTED!!! " + emoji.emojize(':winking_face_with_tongue:'))

    is2_fa = bool(int(input('#### Do you need 2FA? type 1 for yes and 0 for no: ')))
    
    is_your_page = bool(int(input('#### Is this your page? type 1 for yes and 0 for no: ')))
    
    is_cookie_asked = bool(int(input('#### Is this your cookie is been asked? type 1 for yes and 0 for no: ')))
    
    is_silent = bool(int(input('#### Do you want to run this silently? type 1 for yes and 0 for no: ')))

    
    
    username = os.environ.get('my_facebook_username')
    password = os.environ.get('my_facebook_password')

    # data = DataModel(username, password)
    post_url = input("#### Your post URL: ")
    # data.facebook_post_url = post_url
   
    febu_bot = FacebookBot()
    custom_xpath = CustomXpath()
   
    febu_bot.login(
        username=username,
        password=password,
        asked=is_cookie_asked,
        is2Fa=is2_fa,
        url='https://business.facebook.com/login'
    )


    if is2_fa:
        input("#### Enter after your work is done: ")
    print(f"==> Logged in {emoji.emojize(':smiling_face_with_sunglasses:')}")

    febu_bot.goto_facebook_page_post(url=post_url)

    
    print("==> Now in page post")

    time.sleep(5)
    
    # data-testid='newsFeedStream' ==== Bangladesh
    feed_box_aria = febu_bot.driver.find_element_by_xpath("//div[@role='article']")
   
    # feed_box_aria = febu_bot.driver.find_element_by_xpath("//div[@data-testid='newsFeedStream']")
    
    print(feed_box_aria)
    
    # feed_box_aria = febu_bot.driver.find_element_by_xpath("//div[@data-testid='Keycommand_wrapper_feed_story']")
    
    # comments_button_xpath = "//a[@title='Leave a comment']" 
    # comments_button_xpath = "//div[@aria-label='Leave a comment']"

    # febu_bot.mouse_click(comments_button_xpath)
    # print("==> Clicked the comments button")

    time.sleep(3)

    i = 1
    while True:
        print(f"==========> Executing {i} <============")

        if i > 1 and is_silent is False:
            febu_bot.driver.execute_script('window.alert("Click ok then in command ans. question to load more comments and run again");')
            load_more = bool(int(input("#### Load more comments? type 1 for yes and 0 for no: ")))
        else:
            load_more = True

        if load_more is False:
            break
        else:
            try:
                view_comments = feed_box_aria.find_element_by_xpath(
                    '//span/span[contains(text(), "View") and contains(text(), "comments")]')
                febu_bot.driver.execute_script("arguments[0].scrollIntoView();", view_comments)
                time.sleep(1)
                febu_bot.driver.execute_script("arguments[0].click();", view_comments)
                print("==> Loading more comments")
                time.sleep(10)
                print("==> More comments are loaded")
            except NoSuchElementException:
                print("==> No More comments")
                break

            run(febu_bot, feed_box_aria, is_your_page, messages,custom_xpath)

            i += 1