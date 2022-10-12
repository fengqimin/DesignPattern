from abc import ABCMeta, abstractmethod


# 抽象产品角色（Product）
class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass


# 具体产品角色（Concrete Product）
class Alipay(Payment):

    def __init__(self, use_huabei=False):
        self.use_huaei = use_huabei

    def pay(self, money):
        if self.use_huaei:
            print("花呗支付%d元." % money)
        else:
            print("支付宝余额支付%d元." % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." % money)


# 工厂角色（Creator）
class PaymentFactory:

    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        elif method == 'huabei':
            return Alipay(use_huabei=True)
        else:
            raise TypeError("No such payment named %s" % method)


# Client
if __name__ == '__main__':
    pf = PaymentFactory()
    p = pf.create_payment('wechat')
    p.pay(100)
