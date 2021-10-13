from absfactory import AbstractFactoryPython
from abstractproductA import AbstractProductA
from abstractproductB import AbstractProductB
from concreteproductA1 import ConcreteProductA1
from concreteproductB1 import ConcreteProductB1


class ConcreteFactory1(AbstractFactoryPython):

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()
