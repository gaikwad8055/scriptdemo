from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver



#         print("Launching chrome browser.")
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#         print("Launching Firefox browser.")
#     else:
#         # making a default browser
#         driver = webdriver.Edge()
#         print("Launching Ie browser.")
#     return driver
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")