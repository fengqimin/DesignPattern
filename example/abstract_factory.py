# coding:utf8
"""Abstract Factory
Abstract Factory（抽象工厂）


意图：



提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。
适用性：

 一个系统要独立于它的产品的创建、组合和表示时。

 一个系统要由多个产品系列中的一个来配置时。

 当你要强调一系列相关的产品对象的设计以便进行联合使用时。

 当你提供一个产品类库，而只想显示它们的接口而不是实现时。
"""

from abc import abstractmethod, ABCMeta

# ------抽象产品------


class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# ------抽象工厂------


class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# ------具体产品------


class SmallShell(PhoneShell):
    def show_shell(self):
        print("普通手机小手机壳")


class BigShell(PhoneShell):
    def show_shell(self):
        print("普通手机大手机壳")


class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("骁龙CPU")


class MediaTekCPU(CPU):
    def show_cpu(self):
        print("联发科CPU")


class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")


class Android(OS):
    def show_os(self):
        print("Android系统")


class IOS(OS):
    def show_os(self):
        print("iOS系统")


# ------具体工厂------


class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return BigShell()


class HuaweiFactory(PhoneFactory):
    def make_cpu(self):
        return MediaTekCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return SmallShell()


class IPhoneFactory(PhoneFactory):
    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()

    def make_shell(self):
        return AppleShell()


# ------客户端------


class Phone:
    def __init__(self, factory):
        self.cpu = factory.make_cpu()
        self.os = factory.make_os()
        self.shell = factory.make_shell()

    def show_info(self):
        print("手机信息:")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_shell()

    def make_phone(self, factory):
        self.cpu = factory.make_cpu()
        self.os = factory.make_os()
        self.shell = factory.make_shell()


if __name__ == "__main__":
    p1 = Phone(IPhoneFactory())
    p1.show_info()
