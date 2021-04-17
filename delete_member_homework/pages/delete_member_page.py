from delete_member_homework.pages.base_page import BasePage


class DeleteMemberPage(BasePage):
    def delete_member(self):
        self.parse_action("../pages/data.yaml", "click_deletemember_button")
        return True
