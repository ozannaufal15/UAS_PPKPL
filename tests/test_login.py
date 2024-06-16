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
    "uiautomator2ServerInstallTimeout": 60000
}

appium_server_url = 'http://127.0.0.1:4723'
options = AppiumOptions().load_capabilities(capabilities)


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=options)
        el1 = self.driver.find_elements(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/sign_up"]')
        if (len(el1) <= 0):
            self.fail(f'{el1} element not found')
        el1[0].click()
        time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Log In"]')
        el2.click()
        time.sleep(2)
        self.tries = 0

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def checkUser(self, expected_user) -> bool:
        el1 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.ImageView[@resource-id="com.chess:id/menu_item_avatar"]')
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/usernameTxt"]')
        return el2.text == expected_user

    def handleCaptcha(self) -> bool:
        if (len(self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Verification"]')) > 0):
            time.sleep(10)
            time.sleep(10)
            time.sleep(10)
            el1 = self.driver.find_elements(
                by=AppiumBy.XPATH, value='//android.widget.CheckBox[@text="Verify you are human"]')
            if (len(el1) > 0):
                el1[0].click()
            else:
                self.driver.back()
            time.sleep(10)
            return False
        else:
            return True

    def test_login_wrong_email_wrong_pass(self) -> None:
        while (True):
            el3 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.chess:id/usernameEdit"]')
            el3.send_keys(WRONG_EMAIL)
            time.sleep(2)
            el4 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.chess:id/passwordEdit"]')
            el4.send_keys(WRONG_PASS)
            time.sleep(2)
            el5 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="com.chess:id/loginBtn"]')
            el5.click()
            time.sleep(2)
            time.sleep(5)
            if (self.handleCaptcha() or self.tries > 5):
                break
            else:
                self.tries += 1
                continue

        assert len(self.driver.find_elements(by=AppiumBy.XPATH,
                   value='//android.widget.TextView[@resource-id="com.chess:id/incorrectPasswordErrorText"]')) > 0

    def test_login_no_email_no_pass(self) -> None:
        el3 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="com.chess:id/loginBtn"]')
        el3.click()
        time.sleep(2)
        assert len(self.driver.find_elements(by=AppiumBy.XPATH,
                   value='//*[@text="Cannot Be Empty"]')) > 0

    def test_login_google_valid(self) -> None:
        while (True):
            el3 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="com.chess:id/googleBtn"]/android.view.ViewGroup')
            el3.click()
            time.sleep(2)
            el4 = self.driver.find_element(
                by=AppiumBy.XPATH, value=f'//android.widget.TextView[@resource-id="com.google.android.gms:id/account_name" and @text="{EMAIL_GOOGLE_LOGIN}"]')
            el4.click()
            time.sleep(5)
            if (self.handleCaptcha() or self.tries > 5):
                break
            else:
                self.tries += 1
                continue
        if (len(self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Update to Legal Policies"]')) > 0):
            el5 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="com.chess:id/okayBtn"]')
            el5.click()
            time.sleep(2)

        assert self.checkUser(USERNAME_GOOGLE_LOGIN)

    def test_login_email_valid(self) -> None:
        while (True):
            el3 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.chess:id/usernameEdit"]')
            el3.send_keys(EMAIL_USER_1)
            time.sleep(2)
            el4 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.chess:id/passwordEdit"]')
            el4.send_keys(PASS_USER_1)
            time.sleep(2)
            el5 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="com.chess:id/loginBtn"]')
            el5.click()
            time.sleep(5)
            if (self.handleCaptcha() or self.tries > 5):
                break
            else:
                self.tries += 1
                continue

        if (len(self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')) > 0):
            el6 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')
            el6.click()
            time.sleep(2)

        if (len(self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Update to Legal Policies"]')) > 0):
            el7 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="com.chess:id/okayBtn"]')
            el7.click()
            time.sleep(2)

        assert self.checkUser(USERNAME_USER_1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
