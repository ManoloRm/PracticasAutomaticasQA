import selenium
from selenium import webdriver
from selenium.webdriver.common import by
import time

from selenium.webdriver.common.by import By

import pages
import data

class Test_demo_qa():
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_username(self):
        self.driver.get(data.URLBank)
        test_pass = data.pasword
        test_username = data.username
        pages.loginpage.loging_user_name_box(self, test_username)
        pages.loginpage.loging_user_password_box(self, test_pass)
        pages.loginpage.logiong_button(self)
        assert test_username == data.pasword