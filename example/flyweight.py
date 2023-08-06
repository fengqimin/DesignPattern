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
    c2 = CardPool('8', 'h')
    c3 = CardPool('9', 'h')
    print(list(CardPool._pool.keys()))
    print(c1, c2, c3)
    print(c1 == c3)
    print(id(c1), id(c2), id(c3))
