from typing import Optional


class BaseStructure:
    """Base class for Stack and Queue."""

    def __init__(self, type: str, items: list) -> None:
        """Create a new data structure."""

        self.items: list = items
        self.type: str = type

    def enter_value(self, item: object) -> None:
        """Add the item to the data structure."""

        self.items.append(item)

    def is_empty(self) -> bool:
        """Return True if the structure is empty, False otherwise"""

        return len(self.items) <= 0

    def __str__(self) -> str:
        """Return a string representation of the structure for print"""

        return f"{self.type} Items: {str(self.items)}"


class Stack(BaseStructure):
    """Stack class for working with data."""

    def __init__(self) -> None:
        """Create a new stack."""

        super().__init__("Stack", [])

    def get_value(self) -> Optional[object]:
        """Remove and return the top item from the stack."""

        if self.is_empty():
            return None
        else:
            return self.items.pop()
    
    def view_next(self) -> object:
        """Return the top item from the stack but do not remove"""

        if self.is_empty():
            return None
        else:
            return self.items[-1]


class Queue(BaseStructure):
    """Queue class for working with data."""

    def __init__(self) -> None:
        """Create a new Queue."""

        super().__init__("Queue", [])

    def get_value(self) -> Optional[object]:
        """Remove and return the first item from the Queue."""

        if self.is_empty():
            return None
        else:
            return self.items.pop(0)
    
    def view_next(self) -> object:
        """Return the first item from the queue but do not remove"""

        if self.is_empty():
            return None
        else:
            return self.items[0]


