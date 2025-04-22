# Your solutions to questions in part 3 on the exam will go in this file.
# Modify the code below per the provided specifications. Do NOT change the 
# names of functions/methods/classes nor their signatures.

from typing import Any
import numpy as np

class Arraylist:
    def __init__(self):
        self.data = np.empty(1, dtype=object)
        self.size = 0

    def append(self, val: Any) -> None:
        if self.size == self.data.size:
            ndata = np.empty(self.size * 2, dtype=object)
            for i in range(self.size):
                ndata[i] = self.data[i]
            self.data = ndata
        self.data[self.size] = val
        self.size += 1

    def __len__(self) -> int:
        return self.size
    
    # DO NOT CHANGE ANY CODE ABOVE THIS LINE

    def sort_around(self, idx: int) -> None:
        # Sorting elements before idx in ascending order
        for i in range(idx):
            for j in range(idx - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

        # Sorting elements after idx in descending order
        for i in range(idx, self.size - 1):
            for j in range(i + 1, self.size):
                if self.data[i] < self.data[j]:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
