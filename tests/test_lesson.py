import unittest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

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
    "uiautomator2ServerInstallTimeout": 60000,
    "appium:autoGrantPermissions": True,
    "appium:forceAppLaunch": True
}

appium_server_url = 'http://127.0.0.1:4723'
options = AppiumOptions().load_capabilities(capabilities)


class TestLesson(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=options)
        WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Learn"]')))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_lesson_filter(self) -> None:
        if (len(self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')) > 0):
            el6 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')
            el6.click()
            time.sleep(2)
        el1 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="Learn"]')
        el1.click()
        time.sleep(2)
        if (len(self.driver.find_elements(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')) > 0):
            el6 = self.driver.find_element(
                by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No, thank you"]')
            el6.click()
            time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/tileTxt" and @text="Lessons"]')
        el2.click()
        time.sleep(5)
        el3 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@content-desc="All Lessons"]')
        el3.click()
        time.sleep(5)
        el4 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/levelTv"]')
        el4.click()
        time.sleep(2)
        el5 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/textView" and @text="Advanced"]')
        el5.click()
        time.sleep(5)
        el6 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/instructorTv"]')
        el6.click()
        time.sleep(2)
        el7 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/textView" and @text="Thomas Wolski"]')
        el7.click()
        time.sleep(5)
        el8 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/authorTv"]')
        el9 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/thumbnailLevelTv"]')

        assert "Thomas Wolski" in el8.text
        assert el9.text == "Advanced"

    def test_lesson_search(self) -> None:
        el1 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="Learn"]')
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/tileTxt" and @text="Lessons"]')
        el2.click()
        time.sleep(5)
        el3 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@content-desc="All Lessons"]')
        el3.click()
        time.sleep(5)
        el4 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.chess:id/lessonSearchView"]')
        el4.send_keys("jeremy Silman")
        el4.click()
        self.driver.press_keycode(66)  # click enter pada keyboard mobile
        time.sleep(10)
        el5 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/authorTv"]')

        assert "Jeremy Silman" in el5.text

    def test_lesson_no_result(self) -> None:
        el1 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="Learn"]')
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.chess:id/tileTxt" and @text="Lessons"]')
        el2.click()
        time.sleep(5)
        el3 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.LinearLayout[@content-desc="All Lessons"]')
        el3.click()
        time.sleep(5)
        el4 = self.driver.find_element(
            by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.chess:id/lessonSearchView"]')
        el4.send_keys("31jeqwje104142j412oij")
        el4.click()
        self.driver.press_keycode(66)
        time.sleep(10)
        el5 = self.driver.find_elements(
            by=AppiumBy.XPATH, value='//android.widget.TextView[@text="No Results"]')
        assert len(el5) > 0
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
