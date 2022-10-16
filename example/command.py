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
