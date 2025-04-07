from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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
        try:
            save_login_prompt = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div')
            if save_login_prompt:
                save_login_prompt.click()
        except NoSuchElementException:
            print("Save login prompt not found or already dismissed.")

        time.sleep(4)

        # Click not now for notifications
        notifications_prompt = self.driver.find_elements(By.XPATH, value="//button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt[0].click()


    def find_followers(self):
        time.sleep(5)
        # Show people following the selected account
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(5.5)

        # The Xpath can change in the future, so make sure to update if needed.
        modal_xpath = '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a'
        modal = self.driver.find_element(By.XPATH, value=modal_xpath)
        modal.click()

        for i in range(10):
            # This script will use Javascript to scroll the
            # top of the modal element by the height of the modal
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
    def follow(self):
        pass

