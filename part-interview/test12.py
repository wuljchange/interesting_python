# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-05 20:00
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test12.py
# ----------------------------------------------
from abc import abstractmethod, ABCMeta


class Interface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def test(self):
        pass

    def new(self):
        pass


class NewTest(Interface):
    def __init__(self):
        print("interface")

    def test(self):
        print("test")

    def new(self):
        print("new")


if __name__ == "__main__":
    print("test")
    # nt = NewTest()
    # nt.test()
    # nt.new()