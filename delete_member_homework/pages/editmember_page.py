from delete_member_homework.pages.base_page import BasePage
from delete_member_homework.pages.delete_member_page import DeleteMemberPage


class EditMemberPage(BasePage):
    def goto_editmember(self):
        self.parse_action("../pages/data.yaml", "click_memberinfo_button")
        return DeleteMemberPage(self.driver)