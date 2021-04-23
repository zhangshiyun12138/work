import json
from typing import Dict, List

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    _params = {}
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def find(self,by, locator):
        return self.driver.find_element(by,locator)

    def find_click(self, by, locator):
        self.find(by,locator).click()

    def visibility_wait(self,timeout,by,locator):#定义一个显示等待方法
        wait_time = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located((by,locator)))
        return wait_time

    def clickable_wait(self,timeout,by,locator):
        wait_time = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator)))
        return wait_time

    def swip_click(self,text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                               'scrollable(true).instance(0)).'
                                                               'scrollIntoView(new UiSelector().'
                                                               f'text("{text}").instance(0));').click()

    def parse_action(self,path,fun_num):
        with open(path,"r",encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_num]
            raw = json.dumps(steps)
            for key,value in self._params.items():
                raw = raw.replace("${"+key+"}",value)
            steps = json.loads(raw)
            for step in steps:
                if step["action"] == "find_click":
                    self.find_click(step["by"],step["locator"])
                elif step["action"] == "swip_click":
                    self.swip_click(step["text"])
                elif step["action"] == "find":
                    self.find(step["by"],step["locator"])
                elif step["action"] == "find_sendkeys":
                    self.find(step["by"],step["locator"]).send_keys(step["text"])