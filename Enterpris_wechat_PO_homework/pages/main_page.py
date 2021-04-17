from Enterpris_wechat_PO_homework.pages.add_member_info import AddMemberInfoPage
from Enterpris_wechat_PO_homework.pages.base_page import BasePage


class MainPage(BasePage):
    def goto_add_member(self):
        self.get_url("https://work.weixin.qq.com/wework_admin/frame")
        self.date_driven('../page/data.yml','by1','value1','action1',None)
        return AddMemberInfoPage(self.driver)