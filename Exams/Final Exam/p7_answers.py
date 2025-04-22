# Your solutions to questions in part 7 on the exam will go in this file.
# Modify the code below per the provided specifications. Do NOT change the 
# names of functions/methods/classes nor their signatures.

from typing import Any

class BSTree:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    def __init__(self):
        self.size = 0
        self.root = None


    def add(self, val: Any) -> None:
        def add_rec(n):
            if n is None:
                return BSTree.Node(val)
            elif val < n.val:
                n.left = add_rec(n.left)
                return n
            elif val > n.val: 
                n.right = add_rec(n.right)
                return n
        
        self.root = add_rec(self.root)
        self.size += 1


    def __len__(self) -> int:
        return self.size
    

    # DO NOT CHANGE ANY CODE ABOVE THIS LINE


    def ancestors(self, val: Any) -> list[Any]:
        def find_ancestors(node, val, ancestors):
            if node is None:
                return None
            if node.val == val:
                return ancestors
            if val < node.val:
                return find_ancestors(node.left, val, ancestors + [node.val])
            else:
                return find_ancestors(node.right, val, ancestors + [node.val])
        return find_ancestors(self.root, val, [])

    

    def left_children(self) -> set[Any]:
        def traverse_left_children(node, left_children_set):
            if node is None:
                return left_children_set
            if node.left:
                left_children_set.add(node.left.val)
            left_children_set = traverse_left_children(node.left, left_children_set)
            left_children_set = traverse_left_children(node.right, left_children_set)
            return left_children_set
        return traverse_left_children(self.root, set())