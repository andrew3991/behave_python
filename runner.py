import unittest
from appium import webdriver
from behaver.steps.scenario import *

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = '33006ea4cf559399'
desired_caps['app'] = "ru.appkode.friendsclub.internal"
desired_caps['appActivity'] = 'ru.appkode.friendsclub.MainActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



def before_all(context):
    context.browser = webdriver.Firefox()
    # context.browser = webdriver.Chrome() if you have set chromedriver in your PATH
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()



driver.quit()