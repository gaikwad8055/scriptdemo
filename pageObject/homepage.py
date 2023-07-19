from selenium import webdriver
from selenium.webdriver.common.by import By

class home:

    prof_xpath = "//div[text()='Rohit Anand Gaikwad']"




    def __init__(self,driver):
        self.driver=driver

    def link(self):
        self.driver.find_element(By.XPATH, "prof_xpath").click()
