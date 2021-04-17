from app_po_homework.pages.app import App


class TestContact():
    def setup(self):
        self.app = App()

    def test_addcontact(self):
        self.app.goto_main().goto_addressList().click_addcontact().addcontact_menual().edit_contact()