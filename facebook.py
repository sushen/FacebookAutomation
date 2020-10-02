from selenium import webdriver
import time

#we will create our driver
test_driver = webdriver.Firefox()

test_driver.get("https://www.facebook.com/messages/t/")

email_input = test_driver.find_element_by_id("email")
password_input = test_driver.find_element_by_id("pass")
login_button = test_driver.find_element_by_id("loginbutton")

email = "enter your fb email"
password = "enter fb password"

email_input.send_keys(email)
password_input.send_keys(password)
login_button.click()

#writing in the search area

time.sleep(10)
contacts = ["enter your contact name"]
search_input = test_driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/label/input")
search_input.send_keys(contacts[0])

##click on the first account##

time.sleep(4)
first_account = test_driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/div/div/div[2]/ul/li/a/div/div[2]/div/div')
first_account.click()

## writing a message

time.sleep(4)
message = "hello user!"
message_text_box = test_driver.find_element_by_css_selector('.notranslate')
message_text_box.send_keys(message)

# finally send message
time.sleep(2)
send_button = test_driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div/a')
send_button.click()
