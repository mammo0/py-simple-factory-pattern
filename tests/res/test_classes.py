"""
The classes in this module are used by the unit tests.
"""
from simple_factory_pattern import FactoryPatternMeta


class ClassWithFactoryPattern(metaclass=FactoryPatternMeta):
    def __init__(self, arg):
        self.__arg = arg

    @property
    def arg(self):
        return self.__arg

    @classmethod
    def create_cls(cls, arg):
        return ClassWithFactoryPattern(arg)


class NormalClass():
    pass
