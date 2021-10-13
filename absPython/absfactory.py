from __future__ import annotations
from abc import ABC, abstractmethod
from abstractproductA import AbstractProductA
from abstractproductB import AbstractProductB


class AbstractFactoryPython(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass
