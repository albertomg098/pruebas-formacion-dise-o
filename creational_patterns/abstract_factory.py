from abc import ABC, abstractmethod

class AbstractProduct1(ABC):
    @abstractmethod
    def useful_function_1(self) -> str:
        pass

class ConcreteProduct1A(AbstractProduct1):
    def useful_function_1(self) -> str:
        return "Result of product 1A"

class ConcreteProduct1B(AbstractProduct1):
    def useful_function_1(self) -> str:
        return "Result of product 1B"


class AbstractProduct2(ABC):
    @abstractmethod
    def useful_function_2(self):
        pass

class ConcreteProduct2A(AbstractProduct2):
    def useful_function_2(self) -> str:
        return "Result of product 2A"

class ConcreteProduct2B(AbstractProduct2):
    def useful_function_2(self) -> str:
        return "Result of product 2B"


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_1(self) -> AbstractProduct1:
        pass

    @abstractmethod
    def create_product_2(self) -> AbstractProduct2:
        pass

class FactoryA(AbstractFactory):
    def create_product_1(self) -> AbstractProduct1:
        return ConcreteProduct1A()

    def create_product_2(self) -> AbstractProduct2:
        return ConcreteProduct2A()

class FactoryB(AbstractFactory):
    def create_product_1(self) -> AbstractProduct1:
        return ConcreteProduct1B()

    def create_product_2(self) -> AbstractProduct2:
        return ConcreteProduct2B()


def client_code(factory: AbstractFactory):
    product_1 = factory.create_product_1()
    product_2 = factory.create_product_2()

    print(f"{product_1.useful_function_1()}")
    print(f"{product_2.useful_function_2()}")

if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(FactoryA())

    print("Client: Testing the same client code with the second factory code:")
    client_code(FactoryB())
