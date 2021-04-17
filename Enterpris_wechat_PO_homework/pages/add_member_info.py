from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Enterpris_wechat_PO_homework.pages.base_page import BasePage


class AddMemberInfoPage(BasePage):
    def add_member(self,name,account,phone_number):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, 'username')))
        self.date_driven('../page/data.yml', 'by2', 'value2', 'action2', name)
        self.date_driven('../page/data.yml', 'by3', 'value3', 'action3', account)
        self.date_driven('../page/data.yml', 'by4', 'value4', 'action4', phone_number)
        self.date_driven('../page/data.yml', 'by5', 'value5', 'action5', None)
        return True

    def get_memeber_info(self):
        """
        成员信息一共有两页，
        首先查看是否在第一页，不在第一页的话点击下一页进行查询
        :return:
        """
        member_list = self.driver.find_element(By.XPATH,'//*[@class="member_colRight_memberTable_tr  member_colRight_memberTable_tr_Inactive"]')
        member_info = []
        for name in member_list:
            member_info.append(name.text)
        print(member_info)

        if "A-23" in member_info:
            assert True

        elif "A-23" not in member_info:
            self.find_ele(By.XPATH, "//*[@class='ww_pageNav js_page_container']/div/a[2]").click()
            member_list1 = self.finds_ele(By.XPATH,
                                          '//*[@class="member_colRight_memberTable_tr  member_colRight_memberTable_tr_Inactive"]')
            member_info1 = []
            for i in member_list1:
                member_info1.append(i.text)
            print(member_info1)
            if "A-23" in member_info1:
                assert True

        else:
            assert False
