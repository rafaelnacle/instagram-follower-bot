from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os


load_dotenv()
IG_USER = os.getenv("IG_USER")
IG_PWD = os.getenv("IG_PWD")
SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(4.5)

        decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            cookie_warning[0].click()

        username = self.driver.find_element(By.NAME, value="username")
        password = self.driver.find_element(By.NAME, value="password")

        username.send_keys(IG_USER)
        password.send_keys(IG_PWD)

        time.sleep(2.5)
        password.send_keys(Keys.ENTER)

        time.sleep(4.5)
        # Click not now and ignore save-login info
        save_login_prompt = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(4)

        # Click not now for notifications
        notifications_prompt = self.driver.find_element(By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        pass

    def follow(self):
        pass

