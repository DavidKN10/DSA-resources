class LinkedList:
    class Node:
        def __init__(self, val, prior=None, next=None):
            self.val = val
            self.prior = prior
            self.next = next

    def __init__(self):
        self.head = LinkedList.Node(None)  # sentinel node (never to be removed)
        self.head.prior = self.head.next = self.head  # "circular" topology
        self.cursor = self.head
        self.length = 0

    ### prepend and append, below, from class discussion

    def prepend(self, value):
        n = LinkedList.Node(value, prior=self.head, next=self.head.next)
        self.head.next.prior = self.head.next = n
        self.length += 1

    def append(self, value):
        n = LinkedList.Node(value, prior=self.head.prior, next=self.head)
        n.prior.next = n.next.prior = n
        self.length += 1

    ### subscript-based access ###

    def __getitem__(self, idx):
        """Implements `x = self[idx]`"""
        if isinstance(idx, int):
            if idx < 0:
                idx += self.length
            if not 0 <= idx < self.length:
                raise IndexError("Index out of range")

            curr = self.head.next
            for _ in range(idx):
                curr = curr.next

            return curr.val
        else:
            raise TypeError("Invalid index type")

    def __setitem__(self, idx, value):
        """Implements `self[idx] = x`"""
        if isinstance(idx, int):
            if idx < 0:
                idx += self.length
            if not 0 <= idx < self.length:
                raise IndexError("Index out of range")

            curr = self.head.next
            for _ in range(idx):
                curr = curr.next

            curr.val = value
        else:
            raise TypeError("Invalid index type")

    def __delitem__(self, idx):
        """Implements `del self[idx]`"""
        if isinstance(idx, int):
            if idx < 0:
                idx += self.length
            if not 0 <= idx < self.length:
                raise IndexError("Index out of range")

            curr = self.head.next
            for _ in range(idx):
                curr = curr.next

            curr.prior.next = curr.next
            curr.next.prior = curr.prior
            self.length -= 1
        else:
            raise TypeError("Invalid index type")

    ### cursor-based access ###

    def cursor_get(self):
        """retrieves the value at the current cursor position"""
        return self.cursor.val

    def cursor_set(self, idx):
        """sets the cursor to the node at the provided index"""
        if isinstance(idx, int):
            if not -self.length <= idx < self.length:
                raise IndexError("Index out of range")

            if idx < 0:
                idx += self.length

            curr = self.head.next
            for _ in range(idx):
                curr = curr.next

            self.cursor = curr
            return idx  # Return the adjusted index value
        else:
            raise TypeError("Invalid index type")

    def cursor_move(self, offset):
        """moves the cursor forward or backward by the provided offset (a
        positive or negative integer);  note that it is possible to advance the
        cursor past the beginning or end of the list, in which case the cursor
        will just "wrap around", skipping over the sentinel node"""
        if not isinstance(offset, int):
            raise TypeError("Invalid offset type")

        if offset == 0:
            return

        if offset > 0:
            for _ in range(offset):
                self.cursor = self.cursor.next
                if self.cursor == self.head:    # wrapping around to skip sentinel node
                    self.cursor = self.cursor.next
        else:
            for _ in range(-offset):
                self.cursor = self.cursor.prior
                if self.cursor == self.head:    # wrapping around to skip sentinel node
                    self.cursor = self.cursor.prior

    def cursor_insert(self, value):
        """inserts a new value after the cursor and sets the cursor to the
        new node"""
        new_node = LinkedList.Node(value, prior=self.cursor, next=self.cursor.next)
        self.cursor.next.prior = self.cursor.next = new_node
        self.cursor = new_node
        self.length += 1
        return self.length

    def cursor_delete(self):
        """deletes the node the cursor refers to and sets the cursor to the
        following node"""
        if self.cursor == self.head:
            return None

        deleted_value = self.cursor.val
        self.cursor.prior.next = self.cursor.next
        self.cursor.next.prior = self.cursor.prior
        self.cursor = self.cursor.next
        self.length -= 1

        if self.cursor == self.head: # check if cursor points to head after deletion
            self.cursor = self.head.next

        return deleted_value

    ### stringification ###

    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""
        if self.length == 0:
            return '[]'

        values = []
        curr = self.head.next
        while curr != self.head:
            values.append(str(curr.val))
            curr = curr.next

        return "[" + ", ".join(values) + "]"

    def __repr__(self):
        """Implements `repr(self)`. Similar to `__str__`, but represents the
        list as an expression that could be evaluated to reproduce the list."""
        return '[' + ', '.join(repr(x) for x in self) + ']'

    ### single-element manipulation ###

    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements down
        the list, as needed. Note that inserting a value at len(self) ---
        equivalent to appending the value --- is permitted. Raises IndexError
        if idx is invalid."""
        if not -self.length <= idx <= self.length:
            raise IndexError("Index out of range")

        if idx < 0:
            idx += self.length

        if idx == self.length:
            self.append(value)
            return value

        curr = self.head.next
        for _ in range(idx):
            curr = curr.next

        new_node = LinkedList.Node(value, prior=curr.prior, next=curr)
        curr.prior.next = curr.prior = new_node
        self.length += 1

        return value

    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""
        if not -self.length <= idx < self.length:
            raise IndexError("Index out of range")

        if idx < 0:
            idx += self.length

        curr = self.head.next
        for _ in range(idx):
            curr = curr.next

        value = curr.val
        curr.prior.next = curr.next
        curr.next.prior = curr.prior
        self.length -= 1

        return value

    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""
        curr = self.head.next
        while curr is not self.head:
            if curr.val == value:
                curr.prior.next = curr.next
                curr.next.prior = curr.prior
                self.length -= 1
                return curr.val
            curr = curr.next

        raise ValueError("value not found in the list")

    ### predicates (T/F queries) ###

    def __eq__(self, other):
        """Returns True if this LinkedList contains the same elements (in
        order) as others. If other is not an LinkedList, returns False."""
        if not isinstance(other, LinkedList):
            return False

        if len(self) != len(other): # compare lengths first
            return False

        curr_self = self.head.next
        curr_other = other.head.next

        while curr_self is not self.head:
            if curr_self.val != curr_other.val:
                return False
            curr_self = curr_self.next
            curr_other = curr_other.next

        return True


    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this
        list."""
        curr = self.head.next
        while curr is not self.head:
            if curr.val == value:
                return True
            curr = curr.next
        return False

    ### queries ###

    def __len__(self):
        """Implements `len(self)`"""
        return self.length

    def min(self):
        """Returns the minimum value in this list."""
        if len(self) == 0:
            raise ValueError("LinkedList is empty")

        curr = self.head.next
        min_val = curr.val

        while curr is not self.head:
            if curr.val < min_val:
                min_val = curr.val
            curr = curr.next

        return min_val

    def max(self):
        """Returns the maximum value in this list."""
        if len(self) == 0:
            raise ValueError("LinkedList is empty")

        curr = self.head.next
        max_val = curr.val

        while curr is not self.head:
            if curr.val > max_val:
                max_val = curr.val
            curr = curr.next

        return max_val

    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""
        if j is None:
            j = len(self)

        if i < 0:
            i = self.length + i
        if j < 0:
            j = self.length + j

        if i < 0 or j > self.length:
            raise IndexError("Index out of range")

        curr = self.head.next
        curr_idx = 0

        while curr_idx < j and curr is not self.head:
            if curr_idx >= i and curr.val == value:
                return curr_idx
            curr = curr.next
            curr_idx += 1

        raise ValueError("Value not found in list")

    def count(self, value):
        """Returns the number of times value appears in this list."""
        count = 0
        curr = self.head.next

        while curr is not self.head:
            if curr.val == value:
                count += 1
            curr = curr.next

        return count

    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_list`. Returns a new LinkedList
        instance that contains the values in this list followed by those
        of other."""
        if not isinstance(other, LinkedList):
            raise TypeError("Unsupported type")

        new_list = LinkedList()

        curr = self.head.next
        while curr is not self.head:
            new_list.append(curr.val)
            curr = curr.next

        curr = other.head.next
        while curr is not other.head:
            new_list.append(curr.val)
            curr = curr.next

        return new_list

    def clear(self):
        """Removes all elements from this list."""
        self.head.next = self.head.prior = self.head
        self.cursor = self.head
        self.length = 0

    def copy(self):
        """Returns a new LinkedList instance (with separate Nodes), that
        contains the same values as this list."""
        new_list = LinkedList()
        current = self.head.next
        while current != self.head:
            new_list.append(current.val)
            current = current.next
        return new_list

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this
        list."""
        for item in other:
            self.append(item)

    ### iteration ###

    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        n = self.head.next
        while n is not self.head:
            yield n.val
            n = n.next
