from abc import ABC, abstractmethod

class Implementation(ABC):
    @abstractmethod
    def some_operation(self) -> str:
        pass

class ConcreteImplementationA(Implementation):
    def some_operation(self) -> str:
        return "ConcreteImplementationA: Here's the result of platform A"

class ConcreteImplementationB(Implementation):
    def some_operation(self) -> str:
        return "ConcreteImplementationB: Here's the result of platform B"

class Abstraction:
    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with: \n"
                f"{self.implementation.some_operation()}")

class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with: \n"
                f"{self.implementation.some_operation()}")

def client_code(abstraction: Abstraction):
    print(abstraction.operation())


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
