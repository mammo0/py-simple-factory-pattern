"""
This module provides a simple implementation of a factory pattern.
"""
from simple_factory_pattern.factorypattern_meta import _FactoryPatternMeta, \
    _FactoryException


__all__ = ["FactoryPatternMeta", "FactoryException"]


FactoryPatternMeta = _FactoryPatternMeta
FactoryException = _FactoryException
