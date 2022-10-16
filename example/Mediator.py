"""
Mediator

 考虑一个简单的点餐输入：
 汉堡、鸡块、薯条、咖啡，

具体的选项：选择全部、取消所有、反选，
当选择变化时，它会影响“选择全部”和“取消所有”的状态（是否可点击），当用户点击某个按钮时，例如“反选”，除了会影响多选框的状态，它又可能影响“选择全部”和“取消所有”按钮的状态。
"""


class Colleague:
    def __init__(self) -> None:
        self.checkboxs = {
            '汉堡': False,
            '鸡块': False,
            '薯条': False,
            "咖啡": False
        }
        self.buttons = {
            '选择全部': True,
            '取消所有': False,
            '反向选择': True,

        }


class Mediator:
    def __init__(self, colleague: Colleague) -> None:
        self.colleague = colleague

    def show_checkbox(self):
        """显示选项的选择状态"""

        self.change_checkbox()
        for k, v in self.colleague.checkboxs.items():
            print(f"{k}: {'√' if v else 'X'}")

        for k, v in self.colleague.buttons.items():
            print(f"{k}: {'可点击' if v else '不可点击'}")

    def change_checkbox(self):
        """改变选项的选择状态"""
        all_checked = True
        all_unchecked = False

        for v in self.colleague.checkboxs.values():
            all_checked = all_checked and v
            all_unchecked = all_unchecked or v

        self.colleague.buttons['选择全部'] = not all_checked
        self.colleague.buttons['取消所有'] = all_unchecked

    def select_all(self):
        for k in self.colleague.checkboxs.keys():
            self.colleague.checkboxs[k] = True

        self.show_checkbox()

    def select_none(self):

        for k in self.colleague.checkboxs.keys():
            self.colleague.checkboxs[k] = False

        self.show_checkbox()

    def select_inverse(self):
        for k, v in self.colleague.checkboxs.items():
            self.colleague.checkboxs[k] = not v

        self.show_checkbox()

    def select_one(self, checkbox: str):
        self.colleague.checkboxs[checkbox] = True
        self.show_checkbox()


if __name__ == '__main__':
    m = Mediator(Colleague())
    m.show_checkbox()
    m.select_inverse()
    m.select_all()
    m.select_none()
    m.select_one('汉堡')
