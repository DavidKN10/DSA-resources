from typing import Any, Iterator


class BSTree:
    class Node:
        def __init__(self, key, val, left=None, right=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right

    def __init__(self):
        self.size = 0
        self.root = None

    def __getitem__(self, key: Any) -> Any:
        return self._get_value(self.root, key)

    def __setitem__(self, key: Any, val: Any) -> None:
        self.root = self._insert(self.root, key, val)

    def __delitem__(self, key: Any) -> None:
        self.root = self._delete(self.root, key)

    def __contains__(self, key: Any) -> bool:
        return self._search(self.root, key) is not None

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator[Any]:
        yield from self._traverse_inorder(self.root)

    def keys(self) -> Iterator[Any]:
        yield from self._traverse_inorder(self.root, key_only=True)

    def values(self) -> Iterator[Any]:
        yield from self._traverse_inorder(self.root, value_only=True)

    def items(self) -> Iterator[tuple[Any, Any]]:
        yield from self._traverse_inorder(self.root, key_value=True)

    def _get_value(self, node: Node, key: Any) -> Any:
        if node is None:
            raise KeyError(key)
        if key == node.key:
            return node.val
        elif key < node.key:
            return self._get_value(node.left, key)
        else:
            return self._get_value(node.right, key)

    def _insert(self, node: Node, key: Any, val: Any) -> Node:
        if node is None:
            self.size += 1
            return self.Node(key, val)
        if key == node.key:
            node.val = val
        elif key < node.key:
            node.left = self._insert(node.left, key, val)
        else:
            node.right = self._insert(node.right, key, val)
        return node

    def _delete(self, node: Node, key: Any) -> Node:
        if node is None:
            raise KeyError(key)
        if key == node.key:
            if node.left is None:
                self.size -= 1
                return node.right
            if node.right is None:
                self.size -= 1
                return node.left
            min_node = self._find_min(node.right)
            node.key = min_node.key
            node.val = min_node.val
            node.right = self._delete(node.right, min_node.key)
        elif key < node.key:
            node.left = self._delete(node.left, key)
        else:
            node.right = self._delete(node.right, key)
        return node

    def _search(self, node: Node, key: Any) -> Node:
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def _traverse_inorder(self, node: Node, key_only=False, value_only=False, key_value=False) -> Iterator[Any]:
        if node is not None:
            yield from self._traverse_inorder(node.left, key_only, value_only, key_value)
            if key_only:
                yield node.key
            elif value_only:
                yield node.val
            elif key_value:
                yield node.key, node.val
            else:
                yield node.key, '=', node.val
            yield from self._traverse_inorder(node.right, key_only, value_only, key_value)

    def _find_min(self, node: Node) -> Node:
        while node.left is not None:
            node = node.left
        return node
