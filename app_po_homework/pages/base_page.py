from typing import Dict, List

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage():
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def find(self,locator):
        return self.driver.find_element_by_xpath(locator)

    def find_click(self,locator):
        self.find(locator).click()

    def swip_click(self,text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
                                                               f'text("{text}").instance(0));').click()

    def parse_action(self,path):
        with open(path,'r',encoding="utf-8") as f:
            steps: List[Dict] = yaml.safe_load(f)
        for step in steps:
            if step["action"] == "find":
                self.find(step["locator"])
            elif step["action"] == "find_click":
                self.find_click(step["locator"])
            elif step["action"] == 'swip_click':
                self.swip_click(step["text"])
            elif step["action"] == "find_sendkeys":
                self.find(step["locator"]).send_keys(step["text"])