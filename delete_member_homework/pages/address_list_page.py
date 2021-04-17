from delete_member_homework.pages.base_page import BasePage
#from delete_member_homework.pages.member_info_page import MemberInfoPage
from delete_member_homework.pages.search_page import SearchPage


class AddressListPage(BasePage):
    def click_search_button(self):
        self.parse_action("../pages/data.yaml","click_search_button")
        return SearchPage(self.driver)