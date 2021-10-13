from __future__ import annotations
from abc import ABC, abstractmethod
from absfactory import AbstractFactoryPython
from abstractproductA import AbstractProductA
from abstractproductB import AbstractProductB
from concreteproductA2 import ConcreteProductA2
from concreteproductB2 import ConcreteProductB2


class ConcreteFactory2(AbstractFactoryPython):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()