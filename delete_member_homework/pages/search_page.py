import allure

from delete_member_homework.pages.base_page import BasePage
from delete_member_homework.pages.member_info_page import MemberInfoPage


class SearchPage(BasePage):
    @allure.story("输入想删除成员的名字")
    def search_member(self,name):
        self._params['name'] = name
        self.parse_action("../pages/data.yaml","search_member")
        return  MemberInfoPage(self.driver)