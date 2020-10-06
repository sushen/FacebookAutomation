class DataModel:
    username: str = None
    password: str = None

    facebook_login_page: str = None
    facebook_business_page: str = None
    facebook_business_post_url: str = None
    facebook_business_page_post: str = None

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
