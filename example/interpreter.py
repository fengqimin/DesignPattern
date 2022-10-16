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
