import unittest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utilities.env import *

import time

capabilities = {
    "platformName": 'Android',
    "appium:platformVersion": "13",
    "appium:deviceName": "Samsung",
    "appium:appPackage": "com.chess",
    "appium:appActivity": "com.chess.home.HomeActivity",
    "appium:language": "en",
    "appium:locale": "US",
    "appium:automationName": "uiautomator2",
    "appium:autoGrantPermissions": True,
    "appium:forceAppLaunch": True,
    "uiautomator2ServerInstallTimeout": 60000
}

appium_server_url = 'http://127.0.0.1:4723'
options = AppiumOptions().load_capabilities(capabilities)


class TestForum(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=options)
        time.sleep(2)
        el8 = self.driver.find_element(
            by=AppiumBy.ID, value="com.chess:id/navigation_more")
        el8.click()
        time.sleep(2)
        self.driver.swipe(500, 1500, 500, 300)
        el9 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/titleTxt" and @text="Forums"]')
        el9.click()
        time.sleep(2)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_post_not_log_in(self) -> None:
        el1 = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Add")
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.ID, value="com.chess:id/forumTopicNameEdt")
        el2.send_keys("tes")
        time.sleep(2)
        el3 = self.driver.find_element(
            by=AppiumBy.ID, value="com.chess:id/forumTopicBodyEdt")
        el3.send_keys("tes")
        time.sleep(2)
        el4 = self.driver.find_element(
            by=AppiumBy.ID, value="com.chess:id/text")
        el4.click()
        assert WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="Please login to continue."]')))

    def test_topic_search_success(self) -> None:
        el1 = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Search")
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.ID, value="com.chess:id/keywordsEditText")
        el2.send_keys(FORUM_SEARCH_KEYWORD)
        time.sleep(2)
        el3 = self.driver.find_element(
            by=AppiumBy.ID, value="android:id/text1")
        el3.click()
        time.sleep(2)
        el4 = self.driver.find_element(
            by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"All\")")
        el4.click()
        time.sleep(2)
        el5 = self.driver.find_element(
            by=AppiumBy.ID, value="com.chess:id/searchBtn")
        el5.click()
        assert WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="com.chess:id/subjectTxt"])[1]')))

    def test_topic_search_no_result(self) -> None:
        el1 = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Search")
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.ID, value="com.chess:id/keywordsEditText")
        el2.send_keys(FORUM_SEARCH_KEYWORD_NO_RESULT)
        time.sleep(2)
        el3 = self.driver.find_element(
            by=AppiumBy.ID, value="com.chess:id/searchBtn")
        el3.click()
        assert WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.chess:id/noForumTopicsTxt"]')))
    #


if __name__ == '__main__':
    unittest.main(verbosity=2)
