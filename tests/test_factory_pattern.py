import unittest

from tests.res.test_classes import ClassWithFactoryPattern
from simple_factory_pattern import FactoryException


class Test(unittest.TestCase):
    def test_create_direct_instance(self) -> None:
        # this should fail
        with self.assertRaises(FactoryException):
            ClassWithFactoryPattern("value")

    def test_create_instance_with_factory_method(self) -> None:
        argument: str = "testArg"

        instance: ClassWithFactoryPattern = ClassWithFactoryPattern.create_cls(argument)

        # it should be a valid instance
        self.assertTrue(isinstance(instance, ClassWithFactoryPattern))

        # the argument should match (see the implementation of the test class)
        self.assertEqual(instance.arg, argument)


if __name__ == "__main__":
    unittest.main()
