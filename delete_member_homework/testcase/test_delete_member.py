import allure

from delete_member_homework.pages.app import App


class TestDeleteMember():
    def setup(self):
        self.app = App()

    @allure.story("成员删除测试")
    def test_delete_member(self):
        name = 'aaa'
        #self.app.goto_main().goto_addresslist_page().click_search_button().search_member(name).goto_delete()
        self.app.goto_main().goto_addresslist_page().click_search_button().search_member(name).click_info_button().goto_editmember().delete_member()