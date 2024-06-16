import unittest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from utilities.env import *
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
    "appium:forceAppLaunch": True,
    "uiautomator2ServerInstallTimeout": 60000
}

appium_server_url = 'http://127.0.0.1:4723'
options = AppiumOptions().load_capabilities(capabilities)


class TestGameArchived(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        login = LoginHelper()
        if (login.isLoggedIn(appium_server_url, options) == True):
            if (login.checkUser(appium_server_url, options, USERNAME_GOOGLE_LOGIN) == False):
                login.logout(appium_server_url, options)
                login.login(appium_server_url, options, EMAIL_GOOGLE_LOGIN)
        else:
            login.login(appium_server_url, options, EMAIL_GOOGLE_LOGIN)

    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=options)
        if (len(self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')) > 0):
            el6 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')
            el6.click()
            time.sleep(2)
        if (len(self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')) > 0):
            el6 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')
            el6.click()
            time.sleep(2)
        el1 = self.driver.find_element(
            by=AppiumBy.ACCESSIBILITY_ID, value="Mastery")
        el1.click()
        time.sleep(2)
        if (len(self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')) > 0):
            el6 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')
            el6.click()
            time.sleep(2)
        if (len(self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')) > 0):
            el6 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')
            el6.click()
            time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/tileTxt" and @text="Analysis"]')
        el2.click()
        time.sleep(2)
        el3 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/tileTxt" and @text="Game Archive"]')
        el3.click()
        time.sleep(5)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_game_archived_filter_no_games(self) -> None:
        el4 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="Search"]')
        el4.click()
        time.sleep(2)
        el5 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.chess:id/resultDrawButton"]')
        el5.click()
        time.sleep(2)
        el6 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="com.chess:id/searchButton"]')
        el6.click()
        time.sleep(5)
        el7 = self.driver.find_elements(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/noResultsTxt"]')
        assert len(el7) > 0

    def test_game_archived_filter(self) -> None:
        el4 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.ImageView[@content-desc="Search"]')
        el4.click()
        time.sleep(2)
        el5 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.chess:id/gameTypeBlitzButton"]')
        el5.click()
        time.sleep(2)
        el6 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.Button[@resource-id="com.chess:id/resultWonButton"]')
        el6.click()
        time.sleep(2)
        el7 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@resource-id="com.chess:id/searchButton"]')
        el7.click()
        time.sleep(5)
        el8 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/finishedOpponentUsername"]')
        assert el8.text == "vasaa77"

    def test_game_archived_analysis(self) -> None:
        el4 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value='//androidx.recyclerview.widget.RecyclerView[@resource-id="com.chess:id/recyclerView"]/android.view.ViewGroup')
        el4.click()
        time.sleep(2)
        el5 = self.driver.find_elements(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Analysis"]')
        assert len(el5) > 0


if __name__ == '__main__':
    unittest.main(verbosity=2)
