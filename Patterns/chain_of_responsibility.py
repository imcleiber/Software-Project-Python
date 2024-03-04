from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

# Define an abstract handler
class Handler(ABC):
    @abstractmethod
    def handle_request(self, request: int) -> Optional[str]:
        pass

    def set_successor(self, successor: Handler) -> None:
        self.successor = successor

# Concrete handlers
class ConcreteHandler1(Handler):
    def handle_request(self, request: int) -> Optional[str]:
        if request > 59:
            return f"Handled by ConcreteHandler1: {request}"
        elif self.successor:
            return self.successor.handle_request(request)
        else:
            return None

class ConcreteHandler2(Handler):
    def handle_request(self, request: int) -> Optional[str]:
        if request > 17:
            return f"Handled by ConcreteHandler2: {request}"
        elif self.successor:
            return self.successor.handle_request(request)
        else:
            return None

class ConcreteHandler3(Handler):
    def handle_request(self, request: int) -> Optional[str]:
        if  request > 12:
            return f"Handled by ConcreteHandler3: {request}"
        else:
            return None

# Client code
def client_code(handler: Handler, requests: list[int]) -> None:
    for request in requests:
        result = handler.handle_request(request)
        if result is not None:
            print(result)
        else:
            print(f"No handler found for request: {request}")

if __name__ == "__main__":
    # Create handlers and set successors
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()
    handler1.set_successor(handler2)
    handler2.set_successor(handler3)

    # Client sends requests
    ages = [18, 60, 14, 8]
    client_code(handler1, ages)
