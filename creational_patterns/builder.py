from abc import ABC, abstractmethod
from typing import Any

class Product1:
    def __init__(self):
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {','.join(self.parts)}", end = "")

class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def create_part_A(self):
        pass
    @abstractmethod
    def create_part_B(self):
        pass

    @abstractmethod
    def create_part_C(self):
        pass

class ConcreteBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self) -> Product1:
        product = self._product
        self.reset()
        return product

    def create_part_A(self):
        self._product.add("PartA1")

    def create_part_B(self):
        self._product.add("PartB1")

    def create_part_C(self):
        self._product.add("PartC1")

class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self._builder.create_part_A()

    def build_full_featured_product(self) -> None:
        self._builder.create_part_A()
        self._builder.create_part_B()
        self._builder.create_part_C()
    
if __name__ == "__main__":
    