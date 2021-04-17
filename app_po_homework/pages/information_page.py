from app_po_homework.pages.addresslist_page import AddressListPage
from app_po_homework.pages.base_page import BasePage


class InformationPage(BasePage):
    def goto_addressList(self):
        self.parse_action("../pages/information_page.yaml")
        return AddressListPage(self.driver)