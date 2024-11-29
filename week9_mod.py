from typing import Optional


class Stack:
    """Stack class with a list as the underlying data structure 
    Proves the following methods:
    -is_empty - check if the stack is empty
    push - add an item to the stack
    pop - remove and return the top item from the stack
    peek - return the top item from the stack
    """

    def __init__(self) -> None:
        """Create a new stack"""

        self.items: list = []

    def push(self, item: int) -> None:
        """Add an item to the stack"""

        self.items.append(item)

    def pop(self) -> Optional[int]:
        """Remove and return the top item from the stack."""

        if self.is_empty():
            return None
        else:
            return self.items.pop()
    
    def peek(self) -> int:
        """Return the top item from the stack but do not remove"""

        if self.is_empty():
            return None
        else:
            return self.items[-1]
    
    def is_empty(self) -> bool:
        """Return True if the stack is empty, False otherwise"""

        return len(self.items) <= 0

    def __str__(self) -> str:
        """Return a string representation of the stack for print"""

        return "Stack Items: " + str(self.items)
    

#Queue class
class Queue:
    """Queue class with a list as the underlying data structure 
    Proves the following methods:
    -is_empty - check if the queue is empty
    add - add an item to the queue
    remove - remove and return the first item in the queue
    peek - return the first item from the queue
    """

    def __init__(self) -> None:
        """Create a new queue"""

        self.items: list = []

    def add(self, item: int) -> None:
        """Add an item to the queue"""

        self.items.append(item)

    def remove(self) -> Optional[int]:
        """Remove and return the first item in the queue."""

        if self.is_empty():
            return None
        else:
            return self.items.pop(0)
    
    def peek(self) -> int:
        """Return the first item in the queue but do not remove"""

        if self.is_empty():
            return None
        else:
            return self.items[0]
    
    def is_empty(self) -> bool:
        """Return True if the queue is empty, False otherwise"""

        return len(self.items) <= 0

    def __str__(self) -> str:
        """Return a string representation of the queue for print"""

        return "Queue Items: " + str(self.items)