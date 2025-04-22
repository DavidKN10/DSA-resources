from typing import Any


class LinkedList:
    class Node:
        def __init__(self, value: Any, prior=None):
            self.value = value
            self.prior = prior

    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, value: Any) -> None:
        self.tail = LinkedList.Node(value, self.tail)
        self.size += 1

    def __len__(self) -> int:
        return self.size

    # DO NOT CHANGE THE CODE ABOVE THIS LINE

    def __getitem__(self, index: int) -> Any:
        assert 0 <= index < self.size
        current = self.tail
        for _ in range(self.size - index - 1):
            current = current.prior
        return current.value

    def __setitem__(self, index: int, value: Any) -> None:
        assert 0 <= index < self.size

        current = self.tail
        for _ in range(self.size - index - 1):
            current = current.prior
        current.value = value

    def __delitem__(self, index: int) -> None:
        assert 0 <= index < self.size
        if index == self.size - 1:
            self.tail = self.tail.prior
        else:
            current = self.tail
            for _ in range(self.size - index - 2):
                current = current.prior
            current.prior = current.prior.prior

        self.size -= 1

"""
my_list = LinkedList()
my_list.append('a')
my_list.append('b')
my_list.append('c')

print(my_list[0])  # Output: 'a'

my_list[1] = 'updated'
print(my_list[1])  # Output: 'updated'

del my_list[2]
print(len(my_list))  # Output: 2
"""