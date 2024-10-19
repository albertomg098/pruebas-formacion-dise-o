from typing import List
from abc import ABC, abstractmethod

class Component(ABC):
    @property
    def parent(self) -> 'Component':
        return self._parent

    @parent.setter
    def parent(self, parent: 'Component'):
        self._parent = parent

    def add(self, component: 'Component'):
        pass

    def remove(self, component: 'Component'):
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass

class Leaf(Component):
    def operation(self) -> str:
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self._children: List[Component] = []

    def add(self, component: Component):
        self._children.append(component)
        component.parent = self

    def remove(self, component:Component):
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self):
        results = []
        for children in self._children:
            results.append(children.operation())
        return f"Branch({'+'.join(results)})"

def client_code(component: Component):
    print(f"RESULT: {component.operation()}", end = "")

def client_code_2(component_1: Component, component_2: Component):
    if component_1.is_composite():
        component_1.add(component_2)

    print(f"RESULT: {component_1.operation()}", end = "")

if __name__ == "__main__":
    simple = Leaf()
    print("Client: I've got a simple component")
    client_code(simple)
    print("\n")

    tree = Composite()
    branch_1 = Composite()
    branch_1.add(Leaf())
    branch_1.add(Leaf())

    branch_2 = Composite()
    branch_2.add(Leaf())

    tree.add(branch_1)
    tree.add(branch_2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components even when managing the tree:")
    client_code_2(tree, simple)
