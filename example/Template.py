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
