from delete_member_homework.pages.address_list_page import AddressListPage
from delete_member_homework.pages.base_page import BasePage


class MainPage(BasePage):
    def goto_addresslist_page(self):
        self.parse_action("../pages/data.yaml","goto_addresslist_page")
        return AddressListPage(self.driver)