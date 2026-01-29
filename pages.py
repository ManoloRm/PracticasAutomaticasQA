from selenium import webdriver
import selenium
import time
import selenium.common.exceptions
from selenium.webdriver.common.by import By
import data

class loginpage():
    def __init__(self, driver):
        self.driver = driver

    def loging_user_name_box(self, set_user):
        return self.driver.find_element(By.CSS_SELECTOR, "#userName").send_keys(set_user)

    def loging_user_password_box(self, set_password):
        return self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(set_password)

    def logiong_button(self):
        return self.driver.find_element(By.CLASS_NAME, "#login.btn-primary ").click()

class Books():
    def __init__(self, driver):
        self.driver = driver

    def search(self, set_book):
         return self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/input').send_keys(data.searchBook)

class scroll():
    def __init__(self, driver):
        self.driver = driver
    def scroll_To_Search_Box(self):
        return self.driver.find_element(By.XPATH, '//*[@id="login"]').is_displayed()
    assert (scroll_To_Search_Box()).is_displayed()


