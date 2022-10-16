# 二十三种设计模式及其python实现

参考文献：
> 《大话设计模式》——吴强  
> [《Python设计模式》](http://pythontip.com)  
> [《23种设计模式》](http://www.cnblogs.com/beijiguangyong)  
> [《python设计模式》](https://www.cnblogs.com/Jony-li/articles/16249058.html> )  
> [《二十三种设计模式及其python实现》](https://www.cnblogs.com/Liqiongyu/p/5916710.html)  
> [《图解23种设计模式，不信你学不会！》](https://zhuanlan.zhihu.com/p/443132665)  
> [《Java教程-设计模式》](https://www.liaoxuefeng.com/wiki/1252599548343744/1264742167474528)

## 设计模式是什么？

> 设计模式是经过总结、优化的，对我们经常会碰到的一些编程问题的可重用解决方案。一个设计模式并不像一个类或一个库那样能够直接作用于我们的代码。
反之，设计模式更为高级，它是一种必须在特定情形下实现的一种方法模板。设计模式不会绑定具体的编程语言。
一个好的设计模式应该能够用大部分编程语言实现(如果做不到全部的话，具体取决于语言特性)。
最为重要的是，设计模式也是一把双刃剑，如果设计模式被用在不恰当的情形下将会造成灾难，进而带来无穷的麻烦。
然而如果设计模式在正确的时间被用在正确地地方，它将是你的救星。

> 起初，你会认为“模式”就是为了解决一类特定问题而特别想出来的明智之举。说的没错，看起来的确是通过很多人一起工作，从不同的角度看待问题进而形成的一个最通用、最灵活的解决方案。也许这些问题你曾经见过或是曾经解决过，但是你的解决方案很可能没有模式这么完备。

> 虽然被称为“设计模式”，但是它们同“设计“领域并非紧密联系。设计模式同传统意义上的分析、设计与实现不同，事实上设计模式将一个完整的理念根植于程序中，所以它可能出现在分析阶段或是更高层的设计阶段。很有趣的是因为设计模式的具体体现是程序代码，因此可能会让你认为它不会在具体实现阶段之前出现(
事实上在进入具体实现阶段之前你都没有意识到正在使用具体的设计模式)。

> 可以通过程序设计的基本概念来理解模式：增加一个抽象层。抽象一个事物就是隔离任何具体细节，这么做的目的是为了将那些不变的核心部分从其他细节中分离出来。当你发现你程序中的某些部分经常因为某些原因改动，而你不想让这些改动的部分引发其他部分的改动，这时候你就需要思考那些不会变动的设计方法了。这么做不仅会使代码可维护性更高，而且会让代码更易于理解，从而降低开发成本。

## 面向对象设计七大原则

**单一职责原则（Single responsibility principle）：**
> 不要存在多于一个导致类变更的原因。通俗的说，即一个类只负责一项职责。面向对象五个基本原则（SOLID）之一。

**开放封闭原则（Open Close Principle）：**
> 一个软件实体如类、模块和函数应该对扩展开放，对修改关闭。即软件实体应尽量在不修改原有代码的情况下进行扩展。想要达到这样的效果，我们需要使用接口和抽象类。面向对象五个基本原则（SOLID）之一。

**里氏替换原则（Liskov Substitution Principle）：**
> 所有引用父类的地方必须能透明地使用其子类的对象。里氏代换原则是对开闭原则的补充。实现开闭原则的关键步骤就是抽象化。面向对象五个基本原则（SOLID）之一。

**接口隔离原则（Interface Segregation Principle）：**
> 使用多个专门的接口，而不使用单一的总接口，即客户端不应该依赖那些它不需要的接口。它还有另外一个意思：降低类之间的耦合度。面向对象五个基本原则（SOLID）之一。

**依赖倒置原则（Dependence Inversion Principle）：**
> 高层模块不应该依赖低层模块，二者都应该依赖其抽象；抽象不应该依赖细节；细节应该依赖抽象。换言之，要针对接口编程，而不是针对实现编程。这个原则是开闭原则的基础。面向对象五个基本原则（SOLID）之一。

**迪米特法则，又称最少知道原则（Demeter Principle）:**
> 最少知道原则是指：一个实体应当尽量少地与其他实体之间发生相互作用，使得系统功能模块相对独立。

**合成复用原则（Composite Reuse Principle）:**
> 合成复用原则是指：尽量使用合成/聚合的方式，而不是使用继承。

## 设计模式分类

>1.创建模式（Creational Patterns），提供实例化的方法，为适合的状况提供相应的对象创建方法。  
>2.结构化模式，通常用来处理实体之间的关系，使得这些实体能够更好地协同工作。  
>3.行为模式，用于在不同的实体建进行通信，为实体之间的通信提供更容易，更灵活的通信方法。

### [创建型模式(5)](#创建型模式)

```text
1. Factory Method（工厂方法）
2. Abstract Factory（抽象工厂）
3. Builder（建造者）
4. Prototype（原型）
5. Singleton（单例）
```

### [结构型模式(7)](#结构型模式)

```text
6. Adapter（适配器）
7. Bridge（桥接）
8. Composite（组合）
9. Decorator（装饰）
10. Facade（外观）
11. Flyweight（享元）
12. Proxy（代理）
```

### [行为型模式(11)](#行为型模式)

```text
13. Interpreter（解释器）
14. Template Method（模板方法）
15. Chain of Responsibility（责任链）
16. Command（命令）
17. Iterator（迭代器）
18. Mediator（中介者）
19. Memento（备忘录）
20. Observer（观察者）
21. State（状态）
22. Strategy（策略）
23. Visitor（访问者）
```

## 创建型模式

### 1. Factory Method（工厂方法）

![工厂方法](https://images2015.cnblogs.com/blog/824579/201609/824579-20160928141135485-1986044710.gif)

#### **意图：**

> 定义一个用于创建对象的接口，让子类决定实例化哪一个类。Factory Method使一个类的实例化延迟到其子类。

#### **适用性：**

> 当一个类不知道它所必须创建的对象的类的时候。  
> 当一个类希望由它的子类来指定它所创建的对象的时候。  
> 当类将创建对象的职责委托给多个帮助子类中的某一个，并且你希望将哪一个帮助子类是代理者这一信息局部化的时候。
（使用较多）

#### **角色：**

```text
抽象工厂角色（Creator）
具体工厂角色（Concrete Creator）
抽象产品角色（Product）
具体产品角色（Concrete Product）
```

#### **实现：**

```python
# !/usr/bin/python
# coding:utf8

"""
Factory Method
"""
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
```

#### **优点：**

>1.每个具体产品都对应一个具体工厂类，不需要修改工厂类代码。  
>2.隐藏了对象创建的实现细节。

#### **缺点：**

>每增加一个具体产品类，就必须增加一个相应的具体工厂类

### 2. Abstract Factory（抽象工厂）

![抽象工厂](https://images2015.cnblogs.com/blog/824579/201609/824579-20160928181031672-1073974804.gif)

#### **意图：**

```text
提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。抽象工厂模式可以向客户端提供一个接口，使客户端在不必指定产品的具体情况下，创建多个产品族中的产品对象。
```

#### **适用性：**

```text
一个系统要独立于它的产品的创建、组合和表示时。

一个系统要由多个产品系列中的一个来配置时。

当你要强调一系列相关的产品对象的设计以便进行联合使用时。

当你提供一个产品类库，而只想显示它们的接口而不是实现时。
(使用较少)
```

#### **角色：**

```text
抽象工厂角色（Creator）

具体工厂角色（Concrete Creator）

抽象产品角色（Product）

具体产品角色（Concrete Product）
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
'''
Abstract Factory
'''
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


if __name__ == '__main__':
    p1 = Phone(IPhoneFactory())
    p1.show_info()
```

#### **优点：**

>将客户端与类的具体实现相分离  
>每个工厂创建了一个完整的产品系列，使得易于交换产品系列  
>有利于产品的一致性（即产品之间的约束关系）

#### **缺点：**

>难以支持新种类的（抽象）产品

### 3. Builder（建造者）

![建造者](https://images2015.cnblogs.com/blog/824579/201609/824579-20160928195334656-2085921203.gif)

#### **意图：**

```text
将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
```

#### **适用性：**

```text
当创建复杂对象的算法应该独立于该对象的组成部分以及它们的装配方式时。

当构造过程必须允许被构造的对象有不同的表示时。

建造者模式与抽象工厂模式相似，也用来创建复杂对象。
主要区别是建造者模式着重一步步构造一个复杂对象，而抽象工厂模式着重于多个系列的产品对象。
```

#### **角色：**

```text
抽象建造者（Abstract Builder）
具体建造者（Concrete Builder）
指挥者（Director）
产品（Product）
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8

"""
    Builder
"""


# Director

class Director(object):
    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


# Abstract Builder

class Builder(object):
    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()


# Concrete Builder

class BuilderHouse(Builder):
    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'


class BuilderFlat(Builder):
    def build_floor(self):
        self.building.floor = 'More than One'

    def build_size(self):
        self.building.size = 'Small'


# Product

class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: %s | Size: %s' % (self.floor, self.size)


# Client

if __name__ == "__main__":
    director = Director()
    director.builder = BuilderHouse()
    director.construct_building()
    building = director.get_building()
    print(building)
    director.builder = BuilderFlat()
    director.construct_building()
    building = director.get_building()
    print(building)
```

#### **优点：**

>1.封装性好，构建和表示分离。隐藏了一个产品的内部结构和装配过程。  
>2.扩展性好，各个具体的建造者相互独立，有利于系统的解耦。  
>3.客户端不必知道产品内部组成的细节，建造者可以对创建过程逐步细化，而不对其它模块产生任何影响，便于控制细节风险。

#### **缺点：**

>1.产品的组成部分必须相同，这限制了其使用范围。  
2.如果产品内部发生变化，则建造者也要同步修改，后期维护成本较大。

### 4. Prototype（原型）

![原型](https://images2015.cnblogs.com/blog/824579/201609/824579-20160928194103188-1537654983.gif)

#### **意图：**

```text
原型模式也可以称为复制模式，是在创造对象的时候使用。
用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
```

#### **适用性：**

```text
当要实例化的类是在运行时刻指定时，例如，通过动态装载；或者为了避免创建一个与产品类层次平行的工厂类层次时；
或者当一个类的实例只能有几个不同状态组合中的一种时。建立相应数目的原型并克隆它们可能比每次用合适的状态手工实例化该类更方便一些。
```

#### **角色：**

```text
原型（Prototype）
产品（Product）
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
"""
Prototype
"""
import copy


class TestObject:
    def __str__(self):
        return f"I am {self.__class__.__name__} object."


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, obj_name, obj):
        """Register an object"""
        self._objects[obj_name] = obj

    def unregister_object(self, obj_name):
        """Unregister an object"""
        del self._objects[obj_name]

    def clone(self, obj_name, **attr):
        """Clone a registered object and update inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(obj_name))
        obj.__dict__.update(attr)
        return obj


if __name__ == "__main__":
    a = TestObject()

    prototype = Prototype()
    prototype.register_object('a', a)
    b = prototype.clone('a', a=1, b=2, c=3)

    print(prototype._objects)
    print(b)
    print(b.a, b.b, b.c)

```

#### **优点：**

>原型模式用于创建复杂的或者耗时的实例：复制一个已经存在的实例使程序运行更高效。且对于工厂模式，原型模式减少了子类的构建。

#### **缺点：**

>每一个产品类都必须配置一个克隆方法，并且这个克隆方法需要对类的功能进行整体考虑。

### 5. Singleton（单例）

![单例](https://images2015.cnblogs.com/blog/824579/201609/824579-20160928194345281-610274391.gif)

#### **意图：**

```text
保证一个类仅有一个实例，并提供一个访问它的全局访问点。
```

#### **适用性：**

```text
当类只能有一个实例而且客户可以从一个众所周知的访问点访问它时。

当这个唯一实例应该是通过子类化可扩展的，并且客户应该无需更改代码就能使用一个扩展的实例时。
```

#### **角色：**

```text
单例（Singleton）
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
'''
Singleton
'''

from threading import Thread, Lock


class Singleton:
    """线程安全的单例模式"""
    _init_lock = Lock()

    def __new__(cls, *args, **kwargs):
        # 确保只有一个实例
        # __new__是线程安全的:
        if not hasattr(Singleton, '_instance'):
            print('first new')
            Singleton._instance = object.__new__(cls)
        return Singleton._instance

    def __init__(self):
        # 只运行一次init
        # __init__不是线程安全的，因此需要用线程锁
        with Singleton._init_lock:
            if not hasattr(Singleton, '_first_init'):
                print('first init')
                Singleton._first_init = True


if __name__ == "__main__":
    def task(i):
        obj = Singleton()
        print(f'Thread-{i}: {obj}')


    for i in range(10):
        t = Thread(target=task, args=(i,))
        t.start()
```

#### **优点：**

>对唯一实例的受控访问  
单例相当于全局变量，但防止了命名空间被污染

### 创建型模式小结

>抽象工厂模式和建造者模式相比于工厂方法模式而言更灵活也更复杂。  
>通常情况下、设计以工厂方法模式开始，当你发现设计需要更大的灵活性时，则像更复杂的设计模式演化。

## 结构型模式

### 6. Adapter（适配器）

![适配器](https://images2015.cnblogs.com/blog/824579/201609/824579-20160930081507250-268482079.gif)

#### **意图：**

```text
将一个类的接口转换成客户希望的另外一个接口。Adapter模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
```

#### **适用性：**

```text
你想使用一个已经存在的类，而它的接口不符合你的需求。

你想创建一个可以复用的类，该类可以与其他不相关的类或不可预见的类（即那些接口可能不一定兼容的类）协同工作。

（仅适用于对象Adapter）你想使用一些已经存在的子类，但是不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。
```

#### **角色：**

```text
目标接口（Target）
待适配的类（Adaptee）
适配器（Adapter）
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
'''
Adapter
'''

import os


class Dog(object):
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human(object):
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "hello"


class Car(object):
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom%s" % ("!" * octane_level)


class Adapter(object):
    """
    Adapts an object by replacing methods.
    Usage:
    dog = Dog
    dog = Adapter(dog, dict(make_noise=dog.bark))
    """

    def __init__(self, obj, adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)


def main():
    objects = []
    dog = Dog()
    objects.append(Adapter(dog, dict(make_noise=dog.bark)))
    cat = Cat()
    objects.append(Adapter(cat, dict(make_noise=cat.meow)))
    human = Human()
    objects.append(Adapter(human, dict(make_noise=human.speak)))
    car = Car()
    car_noise = lambda: car.make_noise(3)
    objects.append(Adapter(car, dict(make_noise=car_noise)))

    for obj in objects:
        print("A", obj.name, "goes", obj.make_noise())


if __name__ == "__main__":
    main()

```

#### **优点：**

 >1.可以让任何两个没有关联的类一起运行。  
2.提高了类的复用。  
3.增加了类的透明度。  
4.灵活性好。

#### **缺点：**

>1.过多地使用适配器，会让系统非常零乱，不易整体进行把握。一个系统如果太多出现这种情况，无异于一场灾难。因此如果不是很有必要，可以不使用适配器，而是直接对系统进行重构。  
>2.由于 JAVA 至多继承一个类，所以至多只能适配一个适配者类，而且目标类必须是抽象类。

### 7. Bridge（桥接）

![桥接](https://images2015.cnblogs.com/blog/824579/201609/824579-20160930082905203-1507021924.gif)

#### **意图：**

```text
将抽象部分与它的实现部分分离，使它们都可以独立地变化。
```

#### **适用性：**

```text
你不希望在抽象和它的实现部分之间有一个固定的绑定关系。例如这种情况可能是因为，在程序运行时刻实现部分应可以被选择或者切换。

类的抽象以及它的实现都应该可以通过生成子类的方法加以扩充。这时Bridge模式使你可以对不同的抽象接口和实现部分进行组合，并分别对它们进行扩充。

对一个抽象的实现部分的修改应对客户不产生影响，即客户的代码不必重新编译。

（C++）你想对客户完全隐藏抽象的实现部分。在C++中，类的表示在类接口中是可见的。

有许多类要生成。这样一种类层次结构说明你必须将一个对象分解成两个部分。Rumbaugh称这种类层次结构为“嵌套的普化”（nested
generalizations）。

你想在多个对象间共享实现（可能使用引用计数），但同时要求客户并不知道这一点。一个简单的例子便是Coplien的String类[ Cop92 ]
，在这个类中多个对象可以共享同一个字符串表示（StringRep）。
```

#### **角色：**

```text
抽象（Abstraction）
细化抽象（RefinedAbstraction）
实现者（Implementor）
具体实现者（ConcreteImplementor
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
"""
Bridge
"""
from abc import abstractmethod


# Implementor
class DrawingAPI(object):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        pass


# ConcreteImplementor 1/2
class RedCircle(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f'{self.__class__.__name__} at ({x}, {y}) radius {radius}')


# ConcreteImplementor 2/2
class GreenCircle(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f'{self.__class__.__name__} at ({x}, {y}) radius {radius}')


# Abstraction
class Shape(object):
    @abstractmethod
    def draw(self):
        pass


# Refined Abstraction
class Circle(Shape):
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    # low-level i.e. Implementation specific
    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)


def main():
    shapes = (
        Circle(1, 2, 3, RedCircle()),
        Circle(5, 7, 11, GreenCircle())
    )

    for shape in shapes:
        shape.draw()


if __name__ == '__main__':
    main()
```

#### **优点：**

>1、抽象和实现的分离。  
2、优秀的扩展能力。  
3、实现细节对客户透明。

#### **缺点：**

>桥接模式的引入会增加系统的理解与设计难度，由于聚合关联关系建立在抽象层，要求开发者针对抽象进行设计与编程。

### 8. Composite（组合）

![组合](https://images2015.cnblogs.com/blog/824579/201609/824579-20160930112848610-861983607.gif)

#### **意图：**

```text
将对象组合成树形结构以表示“部分-整体”的层次结构。Composite使得用户对单个对象和组合对象的使用具有一致性。
```

#### **适用性：**

```text
你想表示对象的部分-整体层次结构。

你希望用户忽略组合对象与单个对象的不同，用户将统一地使用组合结构中的所有对象。
```

#### **角色：**

```text
组件（Component）
叶子（Leaf）
组合（Composite）
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8

"""
Composite
"""


class Component:
    def __init__(self, strName):
        self.m_strName = strName

    def Add(self, com):
        pass

    def Display(self, nDepth):
        pass


class Leaf(Component):
    def Add(self, com):
        print
        "leaf can't add"

    def Display(self, nDepth):
        strtemp = "-" * nDepth
        strtemp = strtemp + self.m_strName
        print
        strtemp


class Composite(Component):
    def __init__(self, strName):
        self.m_strName = strName
        self.c = []

    def Add(self, com):
        self.c.append(com)

    def Display(self, nDepth):
        strtemp = "-" * nDepth
        strtemp = strtemp + self.m_strName
        print
        strtemp
        for com in self.c:
            com.Display(nDepth + 2)


if __name__ == "__main__":
    p = Composite("Wong")
    p.Add(Leaf("Lee"))
    p.Add(Leaf("Zhao"))
    p1 = Composite("Wu")
    p1.Add(Leaf("San"))
    p.Add(p1)
    p.Display(1);
```

#### **优点：**

>组合模式使得客户端代码可以一致地处理单个对象和组合对象，无须关心自己处理的是单个对象，还是组合对象，这简化了客户端代码；  
更容易在组合体内加入新的对象，客户端不会因为加入了新的对象而更改源代码，满足“开闭原则”；

#### **缺点：**

>设计较复杂，客户端需要花更多时间理清类之间的层次关系；  
不容易限制容器中的构件；  
不容易用继承的方法来增加构件的新功能；

### 9. Decorator（装饰）

![装饰](https://images2015.cnblogs.com/blog/824579/201609/824579-20160930115007891-1984670176.gif)

#### **意图：**

```text
动态地给一个对象添加一些额外的职责。就增加功能来说，Decorator模式相比生成子类更为灵活。
```

#### **适用性：**

```text
在不影响其他对象的情况下，以动态、透明的方式给单个对象添加职责。

处理那些可以撤消的职责。

当不能采用生成子类的方法进行扩充时。一种情况是，可能有大量独立的扩展，为支持每一种组合将产生大量的子类，使得子类数目呈爆炸性增长。另一种情况可能是因为类定义被隐藏，或类定义不能用于生成子类。
```

#### **角色：**

```text
组件（Componet）
具体组件（Concrete Componet）
装饰器（Decorator）
具体装饰器（Concrete Decorator）
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
"""
Decorator
"""
from typing import Any


class foo(object):
    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")


class foo_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print("decorated f1")
        self._decoratee.f1()

    def __getattr__(self, name):
        return getattr(self._decoratee, name)


class Decorator:
    def __init__(self, obj) -> None:
        self.obj = obj

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print(f'Decorator {self.obj}')
        return self.obj(*args, **kwargs)


@Decorator
class Foo(object):
    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")


u = foo()
v = foo_decorator(u)
v.f1()
v.f2()

u = Foo()
u.f1()
u.f2()
```

#### **优点：**

>装饰类和被装饰类可以独立发展，不会相互耦合，装饰模式是继承的一个替代模式，装饰模式可以动态扩展一个实现类的功能。

#### **缺点：**

>多层装饰比较复杂。

### 10. Facade（外观）

![外观](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001085208891-1109181708.gif)

#### **意图：**

```text
为子系统中的一组接口提供一个一致的界面，Facade模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。
```

#### **适用性：**

```text
当你要为一个复杂子系统提供一个简单接口时。子系统往往因为不断演化而变得越来越复杂。大多数模式使用时都会产生更多更小的类。这使得子系统更具可重用性，也更容易对子系统进行定制，但这也给那些不需要定制子系统的用户带来一些使用上的困难。Facade可以提供一个简单的缺省视图，这一视图对大多数用户来说已经足够，而那些需要更多的可定制性的用户可以越过facade层。

客户程序与抽象类的实现部分之间存在着很大的依赖性。引入facade将这个子系统与客户以及其他的子系统分离，可以提高子系统的独立性和可移植性。

当你需要构建一个层次结构的子系统时，使用facade模式定义子系统中每层的入口点。如果子系统之间是相互依赖的，你可以让它们仅通过facade进行通讯，从而简化了它们之间的依赖关系。
```

#### **角色：**

```text
子系统（Subsystem）
外观（Facade）
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
"""
Facade
"""

import time

SLEEP = 0.5


# Complex Parts

class TestCase1:
    def run(self):
        print("###### In Test 1 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")


class TestCase2:
    def run(self):
        print("###### In Test 2 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")


class TestCase3:
    def run(self):
        print("###### In Test 3 ######")
        time.sleep(SLEEP)
        print("Setting up")
        time.sleep(SLEEP)
        print("Running test")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")


# Facade

class TestRunner:
    def __init__(self):
        self.tc1 = TestCase1()
        self.tc2 = TestCase2()
        self.tc3 = TestCase3()
        self.tests = [i for i in (self.tc1, self.tc2, self.tc3)]

    def runAll(self):
        [i.run() for i in self.tests]


# Client

if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()
```

#### **优点：**

>利用外观模式可以去掉子系统与客户程序间的直接绑定，从而提高子系统的独立性，也降低了客户程序与子系统的直接耦合度。  
此外，利用外观模式可以使系统层次化。

#### **缺点：**

>不符合开闭原则，如果要改东西很麻烦，继承重写都不合适。

### 11. Flyweight（享元）

![享元](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001085622719-40480507.gif)

#### **意图：**

```text
运用共享技术有效地支持大量细粒度的对象。
当我们需要使用大量细粒度对象时，如果每个都需要创建实例，可能会浪费大量空间。如果这些对象有共同的内部状态，我们可以考虑使用Flyweight模式。
```

#### **适用性：**

```text
1.一个应用程序使用了大量的对象。

2.完全由于使用大量的对象，造成很大的存储开销。

3.对象的大多数状态都可变为外部状态。

4.如果删除对象的外部状态，那么可以用相对较少的共享对象取代很多组对象。

5.应用程序不依赖于对象标识。由于Flyweight对象可以被共享，对于概念上明显有别的对象，标识测试将返回真值。

我们来看一个实例，比如我们要开发一款RPG游戏，游戏地图通常非常大，而且有各种各样，有草地、沙漠、荒原，水路等等，在写代码之前，我们先思考下应该怎样去建模。对于这种地图，我们加载一整张图片来做地图？如果地图太大，图片加载相当卡顿吧？而且大片地图上其实都是重复的图片素材，整图加载设计也有失灵活性。再仔细观察下，这地图无非就是很多小图片（元）拼起来的哦，这不就是类似于我们装修时贴马赛克嘛？
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
"""
Flyweight
"""
import weakref


class CardPool(object):
    """The object pool. Has builtin reference counting"""
    _pool = weakref.WeakValueDictionary()

    """Flyweight implementation. If the object exists in the
    pool just return it (instead of creating a new one)"""

    def __new__(cls, value, suit):
        obj = CardPool._pool.get(value + suit, None)
        if not obj:
            obj = object.__new__(cls)
            CardPool._pool[value + suit] = obj
            # obj.value, obj.suit = value, suit
        return obj

    def __init__(self, value, suit):
        self.value, self.suit = value, suit

    def __repr__(self):
        return "Card: %s%s;" % (self.value, self.suit)


if __name__ == '__main__':
    # comment __new__ and uncomment __init__ to see the difference
    c1 = CardPool('9', 'h')
    c2 = CardPool('9', 'h')
    print(list(CardPool._pool.keys()))
    print(c1, c2)
    print(c1 == c2)
    print(id(c1), id(c2))
```

#### **优点：**

>相同对象只要保存一份，这降低了系统中对象的数量，从而降低了系统中细粒度对象给内存带来的压力。

#### **缺点：**

>1.为了共享对象，需要将不能共享的状态外部化，会增加程序的复杂性  
2.对享元模式的外部状态会增长运行时间

### 12. Proxy（代理）

![代理](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001085925641-1480548759.gif)

#### **意图：**

```text
为其他对象提供一种代理以控制对这个对象的访问。
代理模式与装饰器模式很类似，但代理模式更强调的是对被代理对象的控制，而不是仅限于去装饰目标对象并增强其原有的功能。就像明星的例子一样，如果钱没给够，合同未达成，则不让明星随意作秀。
```

#### **适用性：**

```text
在需要用比较通用和复杂的对象指针代替简单的指针的时候，使用Proxy模式。下面是一些可以使用Proxy模式常见情况：

1)远程代理（Remote Proxy）为一个对象在不同的地址空间提供局部代表。NEXTSTEP[Add94]使用NXProxy类实现了这一目的。Coplien[Cop92]
称这种代理为“大使”（Ambassador）。
2 )虚代理（Virtual Proxy）根据需要创建开销很大的对象。在动机一节描述的ImageProxy就是这样一种代理的例子。
3)保护代理（Protection
Proxy）控制对原始对象的访问。保护代理用于对象应该有不同的访问权限的时候。例如，在Choices操作系统[ CIRM93]
中KemelProxies为操作系统对象提供了访问保护。
4 )智能指引（Smart
Reference）取代了简单的指针，它在访问对象时执行一些附加操作。它的典型用途包括：对指向实际对象的引用计数，这样当该对象没有引用时，可以自动释放它(
也称为SmartPointers[Ede92 ] )。

当第一次引用一个持久对象时，将它装入内存。

在访问一个实际对象前，检查是否已经锁定了它，以确保其他对象不能改变它。
```

#### **实现：**

```python
# !/usr/bin/python
# coding:utf8

"""
Proxy
"""

from re import T
import time


class SalesManager:
    def work(self):

        print("Sales Manager working...")

    def talk(self):
        print("Sales Manager ready to talk")


class Proxy:
    def __init__(self):

        self.busy = False
        self.sales = SalesManager()

    def work(self):
        print("Proxy checking for Sales Manager availability")
        if not self.busy:
            time.sleep(2)
            self.sales.talk()
            self.busy = True
            self.sales.work()
        else:
            self.sales.work()
            time.sleep(2)
            self.busy = False


if __name__ == '__main__':
    p = Proxy()
    p.work()
    p.work()
```

## 行为型模式

### 13. Interpreter（解释器）

![解释器](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001090812703-551743707.gif)

#### **意图：**

```text
给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子。
```

#### **适用性：**

```text
当有一个语言需要解释执行,并且你可将该语言中的句子表示为一个抽象语法树时，可使用解释器模式。而当存在以下情况时该模式效果最好：

该文法简单对于复杂的文法,文法的类层次变得庞大而无法管理。此时语法分析程序生成器这样的工具是更好的选择。它们无需构建抽象语法树即可解释表达式,这样可以节省空间而且还可能节省时间。

效率不是一个关键问题最高效的解释器通常不是通过直接解释语法分析树实现的,而是首先将它们转换成另一种形式。例如，正则表达式通常被转换成状态机。但即使在这种情况下,转换器仍可用解释器模式实现,该模式仍是有用的。
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
"""
Interpreter

"""

from abc import abstractmethod
import time
import datetime

class Expression:
    """AbstractExpression"""

    @abstractmethod
    def interpret(self, context):
        pass


class Interpreter(Expression):
    """Expression"""

    def interpret(self, context):
        code_dict = {'获取当前时间戳': time.time(
        ), "获取当前日期": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        print(f"{context}: {code_dict.get(context)}")


if __name__ == '__main__':
    test = Interpreter()
    text = '获取当前时间戳'
    data1 = test.interpret(text)
    text = '获取当前日期'
    data2 = Interpreter().interpret(text)
```

#### **优点：**

>可扩展性比较好，灵活。  
增加了新的解释表达式的方式。  
易于实现简单文法。

#### **缺点：**

>可利用场景比较少。  
对于复杂的文法比较难维护。  
解释器模式会引起类膨胀。

### 14. Template Method（模板方法）

![模板方法](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001091921547-1734506577.gif)

#### **意图：**

```text
模板方法是一个比较简单的模式。它的主要思想是，定义一个操作的一系列步骤，对于某些暂时确定不下来的步骤，就留给子类去实现好了，这样不同的子类就可以定义出不同的步骤。
模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。
```

#### **适用性：**

```text
一次性实现一个算法的不变的部分，并将可变的行为留给子类来实现。

各子类中公共的行为应被提取出来并集中到一个公共父类中以避免代码重复。这是Opdyke和Johnson所描述过的“重分解以一般化”的一个很好的例子[ OJ93 ]。首先识别现有代码中的不同之处，并且将不同之处分离为新的操作。最后，用一个调用这些新的操作的模板方法来替换这些不同的代码。

控制子类扩展。模板方法只在特定点调用“hook ”操作，这样就只允许在这些点进行扩展。
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
"""
Template Method
"""
from abc import abstractmethod
SETTING = {
    'default': 0,
    'command': 10,
    'project': 20,
    'spider': 30,
    'cmdline': 40,
}


class AbstractSetting:
    def __init__(self, setting) -> None:
        self.setting = setting
        self.setting_cache = {}

    def get_setting(self, key):
        value = self.get_setting_from_cache(key)
        if value is None:
            value = self.read_setting_from_file(key)
            self.put_setting_to_cache(key, value)
        else:
            print(f"get setting from cache, key=='{key}'.")

        return value

    def read_setting_from_file(self, key):
        print(f"read setting from file, key=='{key}'.")
        return self.setting.get(key)

    @abstractmethod
    def get_setting_from_cache(self, key):
        pass

    @abstractmethod
    def put_setting_to_cache(self, key, value):
        pass


class LocalSetting(AbstractSetting):
    def get_setting_from_cache(self, key):
        return self.setting_cache.get(key)

    def put_setting_to_cache(self, key, value):
        self.setting_cache[key] = value


class RedisSetting:
    pass


if __name__ == '__main__':
    s = LocalSetting(SETTING)
    print(s.get_setting('default'))
    print(s.get_setting('default'))
```

#### **优点：**

>1、利用模板方法将相同处理逻辑的代码放到抽象父类中，可以提高代码的复用性。  
2、将不同的代码不同的子类中，通过对子类的扩展增加新的行为，提高代码的扩展性。  
3、把不变的行为写在父类上，去除子类的重复代码，提供了一个很好的代码复用平台，符合开闭原则。

#### **缺点：**

>1、每一个抽象类都需要一个子类来实现，这样导致类的个数增加。  
2、类数量的增加，间接地增加了系统实现的复杂度。  
3、继承关系自身缺点，如果父类添加新的抽象方法，所有子类都要改一遍。

### 15. Chain of Responsibility（责任链）

![责任链](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001092311094-692760233.gif)

#### **意图：**

```text
使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。
还有一些责任链模式，每个Handler都有机会处理Request，通常这种责任链被称为拦截器（Interceptor）或者过滤器（Filter），它的目的不是找到某个Handler处理掉Request，而是每个Handler都做一些工作。
```

#### **适用性：**

```text
有多个的对象可以处理一个请求，哪个对象处理该请求运行时刻自动确定。

你想在不明确指定接收者的情况下，向多个对象中的一个提交一个请求。

可处理一个请求的对象集合应被动态指定。
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
"""
Chain of Responsibility
责任链模式（Chain of Responsibility）是一种处理请求的模式，它让多个处理器都有机会处理该请求，直到其中某个处理成功为止。还有一些责任链模式，每个Handler都有机会处理Request，通常这种责任链被称为拦截器（Interceptor）或者过滤器（Filter），它的目的不是找到某个Handler处理掉Request，而是每个Handler都做一些工作。

在实际场景中，财务审批就是一个责任链模式。假设某个员工需要报销一笔费用，审核者可以分为：
    1.Director：只能审核1000元以下的报销；
    2.Executive Director：只能审核10000元以下的报销；
    3.Managing Director：可以审核任意额度。
"""
from abc import abstractmethod


class Request:
    def __init__(self, name, amount) -> None:
        self.name: str = name
        self.amount: float = amount

    def __repr__(self) -> str:
        return f"{self.name}<{self.amount}>"

    __str__ = __repr__


class Handler:
    @abstractmethod
    def handle(self, request: Request) -> bool:
        pass


class DHandler(Handler):
    def handle(self, request: Request) -> bool:
        if request.amount > 1000:
            return None
        return request.name.lower() == 'bob'


class EDHandler(Handler):
    def handle(self, request: Request) -> bool:
        if request.amount > 10000:
            return None
        return request.name.lower() == 'feng'


class MDHandler(Handler):
    def handle(self, request: Request) -> bool:
        pass


class HandlerChain:
    def __init__(self) -> None:
        self.handlers: list[Handler] = []

    def add_handler(self, handler: Handler):
        self.handlers.append(handler)

    def handle(self, request: Request):
        for handler in self.handlers:
            r = handler.handle(request)
            if r is not None:
                print(
                    f"{request} {'Approved by '  if r else 'Denied by '} {handler.__class__.__name__}")


if __name__ == '__main__':
    hc = HandlerChain()
    hc.add_handler(DHandler())
    hc.add_handler(EDHandler())
    hc.handle(Request('Feng', 100))
```

#### **优点：**

>责任链模式的优点是将请求和处理分开，请求者可以不用知道是谁处理的，处理者可以不用知道请求的全貌，两者解耦。  
责任链模式可以动态组合 , 使用配置设置责任链的顺序，可以随时对责任链排序,随时增加拆除责任链中的某个请求对象。

#### **缺点：**

>责任链有两个非常显著的缺点  
一是性能问题，如果责任链太长，或责任链中请求的处理时间过长，可能会影响性能；  
二是调试不很方便，特别是链条比较长，责任链可能过多，调试的时候逻辑可能比较复杂。

### 16. Command（命令）

![命令](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001093244063-1060485648.gif)

#### **意图：**

```text
将一个请求封装为一个对象，从而使你可用不同的请求对客户进行参数化，对请求排队或记录请求日志，以及支持可撤销的操作。

命令模式是指，把请求封装成一个命令，然后执行该命令。
```

#### **适用性：**

```text
抽象出待执行的动作以参数化某对象，你可用过程语言中的回调（call
back）函数表达这种参数化机制。所谓回调函数是指函数先在某处注册，而它将在稍后某个需要的时候被调用。Command模式是回调机制的一个面向对象的替代品。

在不同的时刻指定、排列和执行请求。一个Command对象可以有一个与初始请求无关的生存期。如果一个请求的接收者可用一种与地址空间无关的方式表达，那么就可将负责该请求的命令对象传送给另一个不同的进程并在那儿实现该请求。

支持取消操作。Command的Excute操作可在实施操作前将状态存储起来，在取消操作时这个状态用来消除该操作的影响。Command接口必须添加一个Unexecute操作，该操作取消上一次Execute调用的效果。执行的命令被存储在一个历史列表中。可通过向后和向前遍历这一列表并分别调用Unexecute和Execute来实现重数不限的“取消”和“重做”。

支持修改日志，这样当系统崩溃时，这些修改可以被重做一遍。在Command接口中添加装载操作和存储操作，可以用来保持变动的一个一致的修改日志。从崩溃中恢复的过程包括从磁盘中重新读入记录下来的命令并用Execute操作重新执行它们。

用构建在原语操作上的高层操作构造一个系统。这样一种结构在支持事务( transaction)
的信息系统中很常见。一个事务封装了对数据的一组变动。Command模式提供了对事务进行建模的方法。Command有一个公共的接口，使得你可以用同一种方式调用所有的事务。同时使用该模式也易于添加新事务以扩展系统。
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8

#!/usr/bin/python
# coding:utf8

"""
Command
"""
import os
from abc import abstractmethod


class Command:
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class GetCWDCommand(Command):
    def execute(self):
        print(os.getcwd())

    def undo(self):
        pass


class MoveFileCommand(Command):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        print('renaming {} to {}'.format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        print('renaming {} to {}'.format(self.dest, self.src))
        os.rename(self.dest, self.src)


if __name__ == "__main__":
    command_stack = []

    # commands are just pushed into the command stack
    command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))
    command_stack.append(GetCWDCommand())

    # they can be executed later on
    for cmd in command_stack:
        cmd.execute()

    # and can also be undone at will
    for cmd in reversed(command_stack):
        cmd.undo()

```

#### **优点：**

>1、降低了系统耦合度。  
2、新的命令可以很容易添加到系统中去。

#### **缺点：**

>使用命令模式可能会导致某些系统有过多的具体命令类。

### 17. Iterator（迭代器）

![迭代器](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001094329172-309095903.gif)

#### **意图：**

```text
提供一种方法顺序访问一个聚合对象中各个元素,而又不需暴露该对象的内部表示。
```

#### **适用性：**

```text
访问一个聚合对象的内容而无需暴露它的内部表示。

支持对聚合对象的多种遍历。

为遍历不同的聚合结构提供一个统一的接口(即,支持多态迭代)。
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
"""
Iterator
迭代器模式（Iterator）实际上在Python的集合类中已经广泛使用了。

"""


class Iterator:
    def __init__(self, max: int = 100, *, first: int = 0) -> None:
        self._first = first
        self._current = self._first
        self.max = max

    def __iter__(self,):
        return self

    def __next__(self,):
        self._current += 1
        self.is_done()
        return self._current-1

    def first(self):
        return self._first

    def current_item(self):
        return self._current

    def is_done(self):
        if self._current > self.max:
            raise StopIteration


if __name__ == '__main__':
    iterator = Iterator(max=100)
    print(iterator.current_item())
    iterator.__next__()
    print(iterator.current_item())

    for i in Iterator(100):
        print(i)
```

#### **优点：**

>1、它支持以不同的方式遍历一个聚合对象。  
2、迭代器简化了聚合类。  
3、在同一个聚合上可以有多个遍历。  
4、在迭代器模式中，增加新的聚合类和迭代器类都很方便，无须修改原有代码。

#### **缺点：**

>由于迭代器模式将存储数据和遍历数据的职责分离，增加新的聚合类需要对应增加新的迭代器类，类的个数成对增加，这在一定程度上增加了系统的复杂性。

### 18. Mediator（中介者）

![中介者](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001094749000-380429958.gif)

#### **意图：**

```text
用一个中介对象来封装一系列的对象交互。中介者使各对象不需要显式地相互引用，从而使其耦合松散，而且可以独立地改变它们之间的交互。
中介模式又称调停者模式，它的目的是把多方会谈变成双方会谈，从而实现多方的松耦合。
```

#### **适用性：**

```text
一组对象以定义良好但是复杂的方式进行通信。产生的相互依赖关系结构混乱且难以理解。

一个对象引用其他很多对象并且直接与这些对象通信,导致难以复用该对象。

想定制一个分布在多个类中的行为，而又不想生成太多的子类。
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
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
```

#### **优点：**

>1、降低了类的复杂度，将一对多转化成了一对一。  
2、各个类之间的解耦。  
3、符合迪米特原则。

#### **缺点：**

>复杂项目，中介者会变得庞大，难以维护。

### 19. Memento（备忘录）

![备忘录](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001095443000-87266383.gif)

#### **意图：**

```text
在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。这样以后就可将该对象恢复到原先保存的状态。
备忘录模式主要用于捕获一个对象的内部状态，以便在将来的某个时候恢复此状态。其实我们使用的几乎所有软件都用到了备忘录模式。最简单的备忘录模式就是保存到文件，打开文件。
```

#### **适用性：**

```text
必须保存一个对象在某一个时刻的(部分)状态,这样以后需要时它才能恢复到先前的状态。

如果一个用接口来让其它对象直接得到这些状态，将会暴露对象的实现细节并破坏对象的封装性。
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
"""
Memento

发起人角色（Originator）：
    它是一个需要保存状态的类，可以创建一个备忘录/备份，并存储它的当前内部状态，也可以使用备忘录来恢复其内部状态。

备忘录角色（Memento）：
    用于存储Originator的内部状态，可以防止Originator以外的对象访问

管理员角色（Caretaker）：
    它只负责存储对象，而不能修改对象（只提供备忘录对象的读写接口，不提供备忘录属性的读写接口），也无须知道对象的实现细节。
    管理员角色可以保存一个备忘录数组，从而实现发起人角色的多次撤销。
"""

import copy
import json


class Memento:
    def __init__(self, state) -> None:
        self.state = state

    def get_state(self):
        return self.state


class Originator:
    def __init__(self):
        self.state = None

    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.state)

    def set_state(self, state):
        self.state = state

    def create_memento(self):
        return Memento(self.state)

    def set_memento(self, memento: Memento):
        self.state = memento.get_state()


class Caretaker:
    def __init__(self) -> None:
        self.mementos: list[Memento] = []

    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.mementos)

    def add(self, memento: Memento):
        self.mementos.append(memento)

    def get(self, index=0):
        return self.mementos.pop(index)

    def save(self):
        try:
            return json.dumps(self.mementos)
        except json.JSONDecodeError:
            pass


class NumObj(object):
    def __init__(self, value):
        self.originator = Originator()
        self.caretaker = Caretaker()
        self.value = value
        self.memento()

    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.value)

    def increment(self):
        self.value += 1

    def commit(self):
        self.memento()

    def memento(self):
        self.originator.set_state({'value': self.value})
        self.caretaker.add(self.originator.create_memento())

    def rollback(self, index: int = 0):
        self.originator.set_memento(self.caretaker.get(index))
        print("rollback: ", self.originator.state)
        self.__dict__.update(self.originator.state)


if __name__ == '__main__':
    n = NumObj(-1)
    print(n)
    n.caretaker.add(n.originator.create_memento())
    n.increment()
    n.commit()
    n.originator.set_memento(n.caretaker.get())
    print(n)
    n.rollback()
    print(n)
```

#### **优点：**

>1.给用户提供了一种可以恢复状态的机制，可以使用户能够比较方便地回到某个历史的状态  
2.实现了信息的封装，使得用户不需要关心状态的保存细节

#### **缺点：**

>如果类的成员变量过多，会占用比较大的资源，而且每一次保存都会消耗一定的内存

### 20. Observer（观察者）

![观察者](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001095725391-893775521.gif)

#### **意图：**

```text
定义对象间的一种一对多的依赖关系,当一个对象的状态发生改变时,所有依赖于它的对象都得到通知并被自动更新。
观察者模式又称发布-订阅模式（Publish-Subscribe：Pub/Sub）。它是一种通知机制，让发送通知的一方（被观察方）和接收通知的一方（观察者）能彼此分离，互不影响。
```

#### **适用性：**

```text
当一个抽象模型有两个方面,其中一个方面依赖于另一方面。将这二者封装在独立的对象中以使它们可以各自独立地改变和复用。

当对一个对象的改变需要同时改变其它对象,而不知道具体有多少对象有待改变。

当一个对象必须通知其它对象，而它又不能假定其它对象是谁。换言之,你不希望这些对象是紧密耦合的。
```

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
'''
Observer
'''

class Subject(object):
def **init**(self):
self._observers = []

    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

# Example usage

class Data(Subject):
def **init**(self, name=''):
Subject.**init**(self)
self.name = name
self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

class HexViewer:
def update(self, subject):
print('HexViewer: Subject %s has data 0x%x' %
(subject.name, subject.data))

class DecimalViewer:
def update(self, subject):
print('DecimalViewer: Subject %s has data %d' %
(subject.name, subject.data))

# Example usage

def main():
data1 = Data('Data 1')
data2 = Data('Data 2')
view1 = DecimalViewer()
view2 = HexViewer()
data1.attach(view1)
data1.attach(view2)
data2.attach(view2)
data2.attach(view1)

    print("Setting Data 1 = 10")
    data1.data = 10
    print("Setting Data 2 = 15")
    data2.data = 15
    print("Setting Data 1 = 3")
    data1.data = 3
    print("Setting Data 2 = 5")
    data2.data = 5
    print("Detach HexViewer from data1 and data2.")
    data1.detach(view2)
    data2.detach(view2)
    print("Setting Data 1 = 10")
    data1.data = 10
    print("Setting Data 2 = 15")
    data2.data = 15

if **name** == '**main**':
main()
```

### 21. State（状态）

![状态](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001100150906-852963744.gif)

**意图：**

允许一个对象在其内部状态改变时改变它的行为。对象看起来似乎修改了它的类。

**适用性：**

一个对象的行为取决于它的状态,并且它必须在运行时刻根据状态改变它的行为。

一个操作中含有庞大的多分支的条件语句，且这些分支依赖于该对象的状态。这个状态通常用一个或多个枚举常量表示。通常,有多个操作包含这一相同的条件结构。State模式将每一个条件分支放入一个独立的类中。这使得你可以根据对象自身的情况将对象的状态作为一个对象，这一对象可以不依赖于其他对象而独立变化。

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
'''
State
'''

class State(object):
"""Base state. This is to share functionality"""

    def scan(self):
        """Scan the dial to the next station"""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Scanning... Station is", self.stations[self.pos], self.name)

class AmState(State):
def **init**(self, radio):
self.radio = radio
self.stations = ["1250", "1380", "1510"]
self.pos = 0
self.name = "AM"

    def toggle_amfm(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate

class FmState(State):
def **init**(self, radio):
self.radio = radio
self.stations = ["81.3", "89.1", "103.9"]
self.pos = 0
self.name = "FM"

    def toggle_amfm(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate

class Radio(object):
"""A radio. It has a scan button, and an AM/FM toggle switch."""
def **init**(self):
"""We have an AM state and an FM state"""
self.amstate = AmState(self)
self.fmstate = FmState(self)
self.state = self.amstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

# Test our radio out

if **name** == '**main**':
radio = Radio()
actions = [radio.scan] *2 + [radio.toggle_amfm] + [radio.scan]* 2
actions = actions * 2

    for action in actions:
        action()
```

### 22. Strategy（策略）

![策略](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001100423828-707061510.gif)

**意图：**

定义一系列的算法,把它们一个个封装起来,并且使它们可相互替换。本模式使得算法可独立于使用它的客户而变化。

**适用性：**

许多相关的类仅仅是行为有异。“策略”提供了一种用多个行为中的一个行为来配置一个类的方法。

需要使用一个算法的不同变体。例如，你可能会定义一些反映不同的空间/时间权衡的算法。当这些变体实现为一个算法的类层次时[H087]
,可以使用策略模式。

算法使用客户不应该知道的数据。可使用策略模式以避免暴露复杂的、与算法相关的数据结构。

一个类定义了多种行为,并且这些行为在这个类的操作中以多个条件语句的形式出现。将相关的条件分支移入它们各自的Strategy类中以代替这些条件语句。

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
"""
Strategy
In most of other languages Strategy pattern is implemented via creating some base strategy interface/abstract class and
subclassing it with a number of concrete strategies (as we can see at http://en.wikipedia.org/wiki/Strategy_pattern),
however Python supports higher-order functions and allows us to have only one class and inject functions into it's
instances, as shown in this example.
"""
import types


class StrategyExample:
    def **init ** (self, func=None):

    self.name = 'Strategy Example 0'
    if func is not None:
        self.execute = types.MethodType(func, self)


def execute(self):
    print(self.name)


def execute_replacement1(self):
    print(self.name + ' from execute 1')


def execute_replacement2(self):
    print(self.name + ' from execute 2')


if ** name ** == '**main**':
    strat0 = StrategyExample()

    strat1 = StrategyExample(execute_replacement1)
    strat1.name = 'Strategy Example 1'

    strat2 = StrategyExample(execute_replacement2)
    strat2.name = 'Strategy Example 2'

    strat0.execute()
    strat1.execute()
    strat2.execute()
```

### 23. Visitor（访问者）

![访问者](https://images2015.cnblogs.com/blog/824579/201610/824579-20161001100727844-1430710049.gif)

**意图：**

定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。TemplateMethod使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。

**适用性：**

一次性实现一个算法的不变的部分，并将可变的行为留给子类来实现。

各子类中公共的行为应被提取出来并集中到一个公共父类中以避免代码重复。这是Opdyke和Johnson所描述过的“重分解以一般化”的一个很好的例子[OJ93]
。首先识别现有代码中的不同之处，并且将不同之处分离为新的操作。最后，用一个调用这些新的操作的模板方法来替换这些不同的代码。

控制子类扩展。模板方法只在特定点调用“hook ”操作（参见效果一节），这样就只允许在这些点进行扩展。

#### **实现：**

```python
#!/usr/bin/python
# coding:utf8
'''
Visitor
'''


class Node(object):
    pass


class A(Node):
    pass


class B(Node):
    pass


class C(A, B):
    pass


class Visitor(object):
    def visit(self, node, *args, **kwargs):
        meth = None
        for cls in node. **class **.** mro **:
            meth_name = 'visit_' + cls. ** name **
            meth = getattr(self, meth_name, None)
            if meth:
                break

        if not meth:
            meth = self.generic_visit
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print('generic_visit ' + node.__class__.__name__)

    def visit_B(self, node, *args, **kwargs):
        print('visit_B ' + node.__class__.__name__)


a = A()
b = B()
c = C()
visitor = Visitor()
visitor.visit(a)
visitor.visit(b)
visitor.visit(c)
```

以上　　
