"""单例模式
单例模式，可以确保某个类只有一个实例存在。
"""
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
        t = Thread(target=task, args=(i, ))
        t.start()
