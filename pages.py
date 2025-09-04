from selenium import webdriver
import selenium
import time
import selenium.common.exceptions
from selenium.webdriver.common.by import By

class loginpage():
    def __init__(self, driver):
        self.driver = driver

    def loging_user_name_box(self, set_user):
        return self.driver.find_element(By.CSS_SELECTOR, "#userName").send_keys(set_user)

    def loging_user_password_box(self, set_password):
        return self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(set_password)

    def logiong_button(self):
        return self.driver.find_element(By.CLASS_NAME, "#login.btn-primary ").click()

class Books ():
    def __init__(self, driver):
        self.driver = driver

    def search(self):
        return self.driver.find_element(By.ID, "searchbox")
