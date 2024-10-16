from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Operation perfomed on Product 1}"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Operation perfomed on Product 2}"

class Constructor(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        operation = f"Constructor: Some operation has been performed over {product.operation}"
        return operation

class ConcreteConstructor1(Constructor):
    def factory_method(self) -> Product:
        return ConcreteProduct1()

class ConcreteConstructor2(Constructor):
    def factory_method(self) -> Product:
        return ConcreteProduct2()

def client_code(creator: Constructor):
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")

if __name__ == "__main__":
    print("App: launched with the ConcreteConstructor1")
    client_code(ConcreteConstructor1())
    print("\n")

    print("App: launched with the ConcreteConstructor2")
    client_code(ConcreteConstructor2())
