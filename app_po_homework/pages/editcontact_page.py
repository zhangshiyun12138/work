from app_po_homework.pages.base_page import BasePage


class EditContactPage(BasePage):
    def edit_contact(self):
        self.parse_action("../pages/editcontact_page.yaml")
        return True