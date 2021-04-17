from app_po_homework.pages.addcontact_page import AddContactPage
from app_po_homework.pages.base_page import BasePage


class AddressListPage(BasePage):
    def click_addcontact(self):
        self.parse_action("../pages/addresslist_page.yaml")
        return AddContactPage(self.driver)
