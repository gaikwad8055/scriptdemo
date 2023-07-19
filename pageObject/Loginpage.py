from selenium import webdriver
from selenium.webdriver.common.by import By
class Login:
    user_email_xpath = "//input[@type='text']session_key"
    user_pass_xpath = "//input[@type='password']"
    user_click = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver


    def enter_email(self,username):
        self.driver.find_element(By.XPATH,"user_email_xpath").send_keys(username)

    def enter_pass(self,password):
        self.driver.find_element(By.XPATH," user_pass_xpath").send_keys(password)


    def submit(self):
        self.driver.find_element(By.XPATH,"user_click").click()


