from typing import Any


class Staque:
    class Node:
        def __init__(self, value: Any, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.top = self.head = None
        self.tail = None

    def __bool__(self) -> bool:
        return self.top is not None

    # DO NOT CHANGE THE CODE ABOVE THIS LINE

    def push(self, value: Any):
        new_node = self.Node(value)
        if not self.top:  # Staque is empty
            self.top = self.tail = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self) -> Any:
        value = self.top.value
        if self.top is self.tail:  # Only one element in the Staque
            self.top = self.tail = None
        else:
            self.top = self.top.next
        return value

    def enqueue(self, value: Any):
        new_node = self.Node(value)
        if not self.top:  # Staque is empty
            self.top = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self) -> Any:
        value = self.top.value
        if self.top is self.tail:
            self.top = self.head = self.tail = None
        else:
            self.top = self.head = self.top.next
        return value

        """
        value = self.top.value
        if self.top is self.tail:  # Only one element in the Staque
            self.top = self.tail = None
        else:
            node = self.top
            while node.next is not self.tail:
                node = node.next
            node.next = None
            self.tail = node
        return value
"""