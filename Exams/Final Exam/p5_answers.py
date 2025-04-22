# Your solutions to questions in part 5 on the exam will go in this file.
# Modify the code below per the provided specifications. Do NOT change the 
# names of functions/methods/classes nor their signatures.

from typing import Any

class Hashtable:
    class Node:
        def __init__(self, key, val, next=None):
            self.key = key
            self.val = val
            self.next = next

    def __init__(self, n_buckets=100):
        self.buckets = [None] * n_buckets
        self.size = 0
    
    def __len__(self) -> int:
        return self.size

    def __setitem__(self, key: Any, val: Any) -> None:
        idx = hash(key) % len(self.buckets)
        n = self.buckets[idx]
        while n:
            if n.key == key:
                n.val = val
                return
            n = n.next
        self.buckets[idx] = self.Node(key, val, self.buckets[idx])
        self.size += 1

    # DO NOT CHANGE ANY CODE ABOVE THIS LINE

    def __getitem__(self, key: Any) -> Any:
        idx = hash(key) % len(self.buckets)
        n = self.buckets[idx]
        prev = None

        while n:
            if n.key == key:
                if prev:
                    prev.next = n.next
                    n.next = self.buckets[idx]
                    self.buckets[idx] = n
                return n.val
            prev = n
            n = n.next
        raise KeyError(key)

