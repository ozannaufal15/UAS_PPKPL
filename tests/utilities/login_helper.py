from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time


class LoginHelper(object):

    def isLoggedIn(self):
        el1 = self.driver.find_elements(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/sign_up"]')
        if (len(el1) > 0):
            return False
        else:
            return True

    def handleCaptcha(self) -> None:
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

    def checkUser(self, expected_user) -> bool:
        if not self.driver:
            self.driver = webdriver.Remote(url, options=options)
        el1 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.ImageView[@resource-id="com.chess:id/menu_item_avatar"]')
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/usernameTxt"]')
        return el2.text == expected_user

    def login(self, url, options, emailgoogle) -> None:
        self.driver = webdriver.Remote(url, options=options)
        if (self.isLoggedIn() == False):
            tries = 0
            while (True):
                el1 = self.driver.find_elements(
                    by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/sign_up"]')
                el1[0].click()
                time.sleep(2)
                el2 = self.driver.find_element(
                    by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Log In"]')
                el2.click()
                time.sleep(2)
                el3 = self.driver.find_element(
                    by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="com.chess:id/googleBtn"]/android.view.ViewGroup')
                el3.click()
                time.sleep(2)
                el4 = self.driver.find_element(
                    by=AppiumBy.XPATH, value=f'//android.widget.TextView[@resource-id="com.google.android.gms:id/account_name" and @text="{emailgoogle}"]')
                el4.click()
                time.sleep(5)
                if (self.handleCaptcha() or tries > 5):
                    break
                else:
                    tries += 1
                    continue
            if (len(self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Update to Legal Policies"]')) > 0):
                el5 = self.driver.find_element(
                    by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="com.chess:id/okayBtn"]')
                el5.click()
                time.sleep(2)
        time.sleep(10)
        if (len(self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')) > 0):
            el6 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')
            el6.click()
            time.sleep(2)
