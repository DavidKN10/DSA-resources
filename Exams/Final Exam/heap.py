from typing import Any

class Heap:
    def __init__(self, key=lambda x: x):
        self.data = []
        self.key = key
        

    @staticmethod
    def _parent(idx: int) -> int:
        return (idx - 1) // 2
    

    @staticmethod
    def _left(idx: int) -> int:
        return idx*2 + 1


    @staticmethod
    def _right(idx: int) -> int:
        return idx*2 + 2


    def add(self, val: Any) -> None:
        self.data.append(val)
        idx = len(self.data) - 1
        while idx > 0:
            pidx = Heap._parent(idx)
            if self.key(self.data[pidx]) < self.key(self.data[idx]):
                self.data[pidx], self.data[idx] = self.data[idx], self.data[pidx]
                idx = pidx
            else:
                break    


    def peek(self) -> Any:
        assert len(self) > 0
        return self.data[0]


    def pop(self) -> Any:
        assert len(self) > 0
        ret = self.data[0]
        self.data[0] = self.data[-1]
        del self.data[-1]
        
        idx = 0
        while idx < len(self.data):
            lidx = Heap._left(idx)
            ridx = Heap._right(idx)
            maxidx = idx
            if lidx < len(self.data) and self.key(self.data[lidx]) > self.key(self.data[idx]):
                maxidx = lidx
            if ridx < len(self.data) and self.key(self.data[ridx]) > self.key(self.data[maxidx]):
                maxidx = ridx
            if maxidx != idx:
                self.data[idx], self.data[maxidx] = self.data[maxidx], self.data[idx]
                idx = maxidx
            else:
                break
        
        return ret            


    def __bool__(self) -> bool:
        return len(self.data) > 0


    def __len__(self) -> int:
        return len(self.data)
