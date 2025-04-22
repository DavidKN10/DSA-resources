import numpy as np
from typing import Any


class Queue:
    def __init__(self, limit=10):
        self.data = np.empty(limit, dtype=object)
        self.head = -1
        self.tail = -1
        self.count = 0

    
    def empty(self):
        return self.count == 0


    def __bool__(self):
        return not self.empty()
   

    def __str__(self):
        if not(self):
            return ''
        return ', '.join(str(x) for x in self)
    

    def __repr__(self):
        return str(self)
    
   
    ## Don't change the above code!
    
    def enqueue(self, val: Any):
        if self.count == len(self.data):
            raise RuntimeError("Queue is full")
        if self.empty():
            self.head = 0
        self.tail = (self.tail + 1) % len(self.data)
        self.data[self.tail] = val
        self.count += 1        


    def dequeue(self) -> Any:
        if self.empty():
            raise IndexError("cannot dequeue from an empty queue")
        val = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % len(self.data)
        self.count -= 1
        if self.empty():
            self.head = -1
            self.tail = -1
        return val
        


    def resize(self, newsize: int):
        assert len(self.data) < newsize
        assert len(self.data) < newsize
        new_data = np.empty(newsize, dtype=object)
        for i, val in enumerate(self):
            new_data[i] = val
        self.data = new_data
        self.head = 0
        self.tail = self.count - 1



    def __iter__(self):
        idx = self.head
        for _ in range(self.count):
            yield self.data[idx]
            idx = (idx + 1) % len(self.data)

