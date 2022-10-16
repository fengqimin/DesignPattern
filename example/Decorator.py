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
