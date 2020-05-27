# Simple Python Factory pattern

![PyPI package](https://github.com/mammo0/py-simple-factory-pattern/workflows/PyPI%20package/badge.svg)
[![PyPI version](https://badge.fury.io/py/simple-factory-pattern.svg)](https://badge.fury.io/py/simple-factory-pattern)

This module provides a simple way to prevent the direct creation of an instance of a class. Instead a `classmethod` of this class can be used.


### Install

You can install this python module via **pip**:
```shell
pip install simple-factory-pattern
```

Otherwise the module can be downloaded from PyPI: https://pypi.org/project/simple-factory-pattern/


### Usage

1. Import the module:
   ```python
   from simple_factory_pattern import FactoryPatternMeta
   ```
2. Create a class that uses the above meta class:
   ```python
   class NewClass(metaclass=FactoryPatternMeta):
       pass
   ```
3. Add a `classmethod` to the new class that returns an instance of the class:
   ```python
   @classmethod
   def create_instance(cls):
       return NewClass()
   ```
   You can choose any name for the method. But it must be a `classmethod`!

   It's also possible to define multiple `classmethod`s. Only in those methods a new instance of the class can be created.


### Behavior of the new class

It's not possible to create an instance of the class directly:
```python
instance = NewClass()  # this will fail
```
This throws a `FactoryException` (also included in the `simple_factory_pattern` package).

The only way to get an instance is to call the above definded `classmethod`:
```python
instance = NewClass.create_instance()  # this works
```
