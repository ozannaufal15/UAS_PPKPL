import unittest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from utilities.login_helper import *

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
    "appium:noReset": True,
    "appium:autoGrantPermissions": True,
    "appium:forceAppLaunch": True
}

appium_server_url = 'http://127.0.0.1:4723'
options = AppiumOptions().load_capabilities(capabilities)
login = LoginHelper()
login.login(appium_server_url, options)
# if driver:
#     driver.quit()


class TestMessage(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_message_no_text(self) -> None:
        el1 = self.driver.find_element(
            by=AppiumBy.ID, value="com.chess:id/navigation_more")
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/titleTxt" and @text="Messages"]')
        el2.click()
        time.sleep(2)
        el3 = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="New Message")
        el3.click()
        time.sleep(2)
        el4 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText[2]')
        el4.send_keys("test1")
        time.sleep(2)
        el5 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.EditText[@text="test1"]/android.view.View/android.widget.Button')
        el5.click()
        time.sleep(2)
        el6 = self.driver.find_elements(
            by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Error"]')
        assert len(el6) > 0

    def test_message_no_receiver(self) -> None:
        el1 = self.driver.find_element(
            by=AppiumBy.ID, value="com.chess:id/navigation_more")
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/titleTxt" and @text="Messages"]')
        el2.click()
        time.sleep(2)
        el3 = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="New Message")
        el3.click()
        time.sleep(2)
        el4 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText[2]')
        el4.send_keys("test1")
        time.sleep(2)
        el5 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.EditText[@text="test1"]/android.view.View/android.widget.Button')
        el5.click()
        time.sleep(2)
        el6 = self.driver.find_elements(
            by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Error"]')
        assert len(el6) > 0
        # //android.widget.TextView[@text="Cannot Be Empty"]

    def test_message_valid(self) -> None:
        el1 = self.driver.find_element(
            by=AppiumBy.ID, value="com.chess:id/navigation_more")
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/titleTxt" and @text="Messages"]')
        el2.click()
        time.sleep(2)
        el3 = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="New Message")
        el3.click()
        time.sleep(2)
        el4 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.EditText[2]')
        el4.send_keys("test1")
        time.sleep(2)
        el5 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.EditText[@text="test1"]/android.view.View/android.widget.Button')
        el5.click()
        time.sleep(2)
        el6 = self.driver.find_elements(
            by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Error"]')
        assert len(el6) > 0


if __name__ == '__main__':
    unittest.main(verbosity=2)
