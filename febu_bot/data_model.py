class DataModel:
    username: str = None
    password: str = None

    facebook_login_url: str = None
    facebook_post_url: str = None

    def __init__(self,
                 facebook_username,
                 facebook_password,
                 facebook_login_url=None,
                 facebook_post_url=None):

        self.username = facebook_username
        self.password = facebook_password
        if facebook_login_url is not None:
            self.facebook_login_url = facebook_login_url
        else:
            self.facebook_login_url = "https://business.facebook.com/login/"
        if facebook_post_url is not None:
            self.facebook_post_url = facebook_post_url
