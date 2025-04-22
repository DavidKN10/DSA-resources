from typing import Any


class Heap:
    def __init__(self, key=lambda x: x):
        self.data = []
        self.key = key

    @staticmethod
    def _parent(idx):
        return (idx - 1) // 2

    @staticmethod
    def _left(idx):
        return 2 * idx + 1

    @staticmethod
    def _right(idx):
        return 2 * idx + 2

    def _heapify(self, pidx=0):
        while pidx < len(self.data):
            lidx = Heap._left(pidx)
            ridx = Heap._right(pidx)
            max_idx = pidx

            if lidx < len(self.data) and self.key(self.data[lidx]) > self.key(self.data[max_idx]):
                max_idx = lidx

            if ridx < len(self.data) and self.key(self.data[ridx]) > self.key(self.data[max_idx]):
                max_idx = ridx

            if max_idx != pidx:
                self.data[pidx], self.data[max_idx] = self.data[max_idx], self.data[pidx]
                pidx = max_idx
            else:
                break

    def add(self, x: Any) -> None:
        self.data.append(x)

        idx = len(self.data) - 1
        while idx > 0:
            pidx = Heap._parent(idx)
            if self.key(self.data[idx]) > self.key(self.data[pidx]):
                self.data[idx], self.data[pidx] = self.data[pidx], self.data[idx]
                idx = pidx
            else:
                return

    def peek(self) -> Any:
        if self.data:
            return self.data[0]
        return None

    def pop(self) -> Any:
        if not self.data:
            return None

        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        element = self.data.pop()
        self._heapify()
        return element

    def __bool__(self) -> bool:
        return len(self.data) > 0

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return repr(self.data)

