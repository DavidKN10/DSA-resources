# Your solutions to questions in part 4 on the exam will go in this file.
# Modify the code below per the provided specifications. Do NOT change the 
# names of functions/methods/classes nor their signatures.

from typing import Any

class LinkedList:
    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, val: Any) -> None:
        self.head = self.Node(val, self.head)
        self.size += 1

    # DO NOT CHANGE ANY CODE ABOVE THIS LINE

    def interpolate(self, val: Any, k: int):
        assert k > 0
        if k == 1:
            # If k is 1, we prepend the value before each element, including the first element
            current = self.head
            if current is not None:
                new_node = self.Node(val)
                new_node.next = current
                self.head = new_node
                self.size += 1
            while current is not None:
                new_node = self.Node(val)
                new_node.next = current.next
                current.next = new_node
                current = new_node.next
                self.size += 1
        else:
            # If k is greater than 1, we insert the value after every k elements
            current = self.head
            count = 1
            if current is not None:
                new_node = self.Node(val)
                new_node.next = current
                self.head = new_node
                current = current.next
                count += 1
                self.size += 1
            while current is not None:
                if count % k == 0:
                    new_node = self.Node(val)
                    new_node.next = current.next
                    current.next = new_node
                    current = new_node.next
                    self.size += 1
                else:
                    current = current.next
                count += 1
