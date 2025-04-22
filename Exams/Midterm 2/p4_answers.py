# Your solutions to questions in part 4 on the exam will go in this file.
# Modify the code below per the provided specifications. Do NOT change the 
# names of functions/methods/classes nor their signatures.

from typing import Any

class Hashtable:
    class Node:
        def __init__(self, key, value: Any, next=None):
            self.key = key
            self.value = value
            self.next = next
    
    def __init__(self, n_buckets: int=100):
        self.buckets = [None] * n_buckets
        self.size = 0
    
    def __len__(self) -> int:
        return self.size
    
    def __getitem__(self, key: Any) -> Any:
        bidx = hash(key) % len(self.buckets)
        n = self.buckets[bidx]
        while n is not None:
            if n.key == key:
                return n.value
            n = n.next
        else:
            raise KeyError(key)
        
    def __setitem__(self, key: Any, value: Any) -> None:
        bidx = hash(key) % len(self.buckets)
        n = self.buckets[bidx]
        while n is not None:
            if n.key == key:
                n.value = value
                return
            n = n.next
        else:
            self.buckets[bidx] = Hashtable.Node(key, value, self.buckets[bidx])
            self.size += 1

    # DO NOT CHANGE THE CODE ABOVE THIS LINE

    def del_all_by_val(self, value: Any) -> None:
        for bidx in range(len(self.buckets)):
            prev = None
            n = self.buckets[bidx]
            while n is not None:
                if n.value == value:
                    if prev is None:
                        # if the first node in the bucket matches the value
                        self.buckets[bidx] = n.next
                    else:
                        # if a node in the middle or end of the bucket matches the value
                        prev.next = n.next
                    self.size -= 1
                else:
                    prev = n
                n = n.next


# Do not change the following line!
version = 'sum23mid2dca'
