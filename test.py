import time, functools
from types import MethodType
from types import FunctionType
from enum import Enum, unique
from turtle import *
from collections import *
import logging
class TestMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['sex'] = 'Female'
        return type.__new__(cls, name, bases, attrs)

class A(object, metaclass = TestMetaclass):
    pass

class MyError(ValueError):
    def show(self):
        print("valueError")


from functools import reduce

def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
A = 10 / 0


            



        






