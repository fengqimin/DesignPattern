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


class BankPay(Payment):
    def pay(self, money):
        print("银行卡支付%d元." % money)


# 抽象工厂角色（Creator）
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


# 具体工厂角色（Concrete Creator）
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)


class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


# Client
if __name__ == '__main__':
    pf = BankPayFactory()
    p = pf.create_payment()
    p.pay(100)
