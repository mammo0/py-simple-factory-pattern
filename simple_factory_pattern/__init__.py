"""
This module provides a simple implementation of a factory pattern.
"""
from .factorypattern_meta import _FactoryPatternMeta, _FactoryException


__all__ = ["FactoryPatternMeta", "FactoryException"]


class FactoryPatternMeta(_FactoryPatternMeta):
    pass


FactoryException = _FactoryException
