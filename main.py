import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pages
import data

class Test_demo_qa():
    driver=webdriver.Chrome()
    driver.get(data.URLBank_login)
    accions = ActionChains(driver)
    accions.move_to_element(driver.find_element(By.CSS_SELECTOR, "#login"))
    driver = None
    
    @classmethod
    def test_setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_username(self):
        self.driver.get(data.URLBank_login)
        test_pass = data.password
        test_username = data.username
        pages.loginpage.loging_user_name_box(self, test_username)
        pages.loginpage.loging_user_password_box(self, test_pass)

    def test_search_books(self):
        self.driver.get(data.URLBank_books)
        test_searchBook = data.searchBook
        time.sleep(2)
        pages.Books.search(self, test_searchBook)

    def test_Scroll_To_Item(self):
        pages.scroll(self)