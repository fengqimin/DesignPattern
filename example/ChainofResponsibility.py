#!/usr/bin/python
# coding:utf8
"""
Chain of Responsibility

    投行的职称体系从高到低如下：
    董事总经理（MD, Managing Director）
    执行总经理（ED，Executive Director）
    总监(D，Director)
    高级副总裁(SVP，Senior Vice President)
    副总裁(VP，Vice President)
    高级经理(SA，Senior Associate)
    经理(A，Associate)
    助理（AS，Assistant）

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
