import sys


class _FactoryPatternMeta(type):
    """
    This is a meta class that implements the factory pattern.

    If it is used in a class, no direct instances of this class can be created (e.g. instance = Class()). Instead this
    class must have a classmethod, which creates the instance.
    """

    # in this list all (hashed) classmethods of the class that uses this meta class will be listed
    __classmethods = []

    def __init__(cls, name: str, bases: tuple, attr: dict):
        super(_FactoryPatternMeta, cls).__init__(name, bases, attr)

        # iterate over the attributes of this class
        for attr_name, attribute in attr.items():
            # add all classmethods to a list
            # only these methods can create instances of the class that uses this meta class
            if isinstance(attribute, classmethod):
                class_method = getattr(cls, attr_name)
                # add the hash to the classmethod list
                cls.__classmethods.append(hash(class_method))

    def __call__(cls, *args, **kwargs):
        # get the calling method name
        name = sys._getframe().f_back.f_code.co_name

        # this method must be in the class that uses this meta class
        func = getattr(cls, name, None)
        # and the hash must be in the classmethods list
        if hash(func) not in cls.__classmethods:
            # if not, the class was instantiated from outside of the class
            # so raise an exception here
            raise _FactoryException(cls)

        # continue if everything is alright
        return type.__call__(cls, *args, **kwargs)


class _FactoryException(Exception):
    def __init__(self, factory_cls: type):
        # check if the provided class uses the factory pattern meta class
        if type(factory_cls) != _FactoryPatternMeta:
            raise ValueError("The class '%s' must have 'FactoryPatternMeta' as its meta class!" % factory_cls.__name__)

        super(_FactoryException, self).__init__("The class '%s' can't be instantiated directly!" % factory_cls.__name__)
