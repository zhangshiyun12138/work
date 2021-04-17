from time import sleep

import allure

from delete_member_homework.pages.base_page import BasePage
from delete_member_homework.pages.editmember_page import EditMemberPage


class MemberInfoPage(BasePage):
    # def goto_delete(self):
    #     with allure.step("查看即将删除成员的人数"):
    #         eles = self.parse_action("../pages/data.yaml","selector_members")
    #         sleep(2)
    #
    #     if len(eles) > 0:
    #         for ele in eles:
    #             self.clickable_wait(5,"xpath","//*[@resource-id='com.tencent.wework:id/dh2']")
    #             ele.click()
    #             with allure.step("点击选择成员"):
    #                 self.parse_action("../pages/data.yaml","delete_selection")
    #             with allure.step("点击右上角符号，进入成员编辑页"):
    #                 self.parse_action("../pages/data.yaml","click_info_button")
    #             with allure.step("点击编辑成员"):
    #                 self.parse_action("../pages/data.yaml","click_memberinfo_button")
    #             with allure.step("点击删除成员"):
    #                 self.parse_action("../pages/data.yaml","click_deletemember_button")
    #     else:
    #         with allure.step("改成员无搜索结果"):
    #             ele_text = self.parse_action("../pages/data.yaml","assert_result")
    #             assert ele_text == '无搜索结果'

    def click_info_button(self):
        self.parse_action("../pages/data.yaml","click_info_button")
        sleep(2)

        return EditMemberPage(self.driver)
