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
