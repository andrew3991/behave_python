import unittest
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = '33006ea4cf559399'
desired_caps['app'] = "ru.appkode.friendsclub.internal"
desired_caps['appActivity'] = 'ru.appkode.friendsclub.MainActivity'



def before_all(context):
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def after_all(context):
    context.driver.quit()



