import numpy as np
from typing import Any, Iterator


class ArrayList:
    def __init__(self):
        self.data = np.empty(1, dtype=object)
        self.size = 0

    def append(self, value: Any) -> None:
        if self.size == len(self.data):
            ndata = np.empty(2 * len(self.data), dtype=object)
            for i in range(len(self.data)):
                ndata[i] = self.data[i]
            self.data = ndata
        self.data[self.size] = value
        self.size += 1

    def __iter__(self) -> Iterator:
        for i in range(self.size):
            yield self.data[i]

    def __len__(self) -> str:
        return self.size

    def __repr__(self) -> str:
        return '[' + ', '.join(repr(x) for x in self) + ']'

    def __getitem__(self, idx: int) -> Any:
        if idx < 0 or idx >= self.size:
            raise IndexError
        return self.data[idx]

    # You should not modify any code above this line!

    def iter_in_order(self, idxs: list[int]) -> Iterator:
        """Solution to question 1."""
        for idx in idxs:
            if idx < 0 or idx >= self.size:
                raise IndexError
            yield self.data[idx]

    def move_range(self, src: int, dst: int, n: int) -> None:
        """Solution to question 2."""
        temp_array = np.empty(n, dtype=object)
        if src < dst:
            # Move elements from src to temp_array in increasing order
            for i in range(n):
                temp_array[i] = self.data[src + i]
        else:
            # Move elements from src to temp_array in decreasing order
            for i in range(n):
                temp_array[i] = self.data[src - i]

        # Shift elements in the underlying array to make room for the move
        if src < dst:
            # Shift elements down to make room for the move
            for i in range(self.size - 1, dst - 1, -1):
                self.data[i + n] = self.data[i]
        else:
            # Shift elements up to make room for the move
            for i in range(dst, self.size):
                self.data[i - n] = self.data[i]

        # Copy elements from temp_array to the destination range
        for i in range(n):
            self.data[dst + i] = temp_array[i]

        # Update the size of the ArrayList
        self.size += n