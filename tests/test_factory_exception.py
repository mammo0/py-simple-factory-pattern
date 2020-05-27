import unittest

from simple_factory_pattern import FactoryException
from tests.res.test_classes import ClassWithFactoryPattern, NormalClass


class Test(unittest.TestCase):
    def test_factory_exception_right(self):
        # this should throw no exception
        FactoryException(ClassWithFactoryPattern)

    def test_factory_exception_wrong(self):
        with self.assertRaises(ValueError):
            FactoryException(NormalClass)


if __name__ == "__main__":
    unittest.main()
