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
