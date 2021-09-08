"""
The classes in this module are used by the unit tests.
"""
from simple_factory_pattern import FactoryPatternMeta


class ClassWithFactoryPattern(metaclass=FactoryPatternMeta):
    def __init__(self, arg: str) -> None:
        self.__arg: str = arg

    @property
    def arg(self) -> str:
        return self.__arg

    @classmethod
    def create_cls(cls, arg: str) -> "ClassWithFactoryPattern":
        return ClassWithFactoryPattern(arg)


class NormalClass():
    pass
