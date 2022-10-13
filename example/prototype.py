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
