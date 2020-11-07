# this is for post feed box xpath list
feed_box_path_list = [
    "//div[@role='article']",
    "//div[@data-testid='newsFeedStream']"
    "//div[@data-testid='Keycommand_wrapper_feed_story']"
    ]

# this is for comment button xpath list
comments_button_xpath_list = [
    "//div[@aria-label='Leave a comment']",
    "//a[@title='Leave a comment']",
]

# this is for meesage box xpath list which is appear after hover in commnet profile
page_commenter_hover_message_box_xpath_list = [
    '//div[@aria-label="Message" and @tabindex="-1"]'
]

person_message_xpath = [
    '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[5]/*//form/div/div[3]/div[2]/div[1]/div/div/div/div/*//div/div/div/div'
]

class CustomXpath():
    def __init__(self, *args, **kwargs):
        self.feed_box_path_list = feed_box_path_list
        self.comments_button_xpath_list = comments_button_xpath_list
        self.page_commenter_hover_message_box_xpath_list = page_commenter_hover_message_box_xpath_list
        self.person_message_xpath = person_message_xpath
        
    
    def get_feed_box_path_list(self):
        return self.feed_box_path_list
    
    def get_comments_button_xpath_list(self):
        return self.comments_button_xpath_list
    
    def get_page_commenter_hover_message_box_xpath_list(self):
        return self.page_commenter_hover_message_box_xpath_list
    
    def get_person_message_xpath_list(self):
        return self.person_message_xpath
    def set_person_message_xpath_list(self,xpath):
        return self.person_message_xpath.append(xpath)
    
    
        



    