from app_po_homework.pages.base_page import BasePage
from app_po_homework.pages.editcontact_page import EditContactPage


class AddContactPage(BasePage):
    def addcontact_menual(self):
        self.parse_action("../pages/addcontact_page.yaml")
        return EditContactPage(self.driver)