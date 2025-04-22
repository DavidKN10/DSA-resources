import numpy as np


class ArrayList:
    def __init__(self):
        self.data = np.empty(1, dtype=object)
        self.size = 0

    """subscript-based access """

    def __getitem__(self, idx):
        """ Implements x = self[idx] """
        assert isinstance(idx, int), 'Index must be an integer'
        if idx < 0:
            idx += self.size
        if idx < 0 or idx >= self.size:
            raise IndexError('list index out of range')
        return self.data[idx]

    def __setitem__(self, idx, value):
        """ Implements self[idx] = x """
        assert isinstance(idx, int), 'Index must be an integer'
        if idx < 0:
            idx += self.size
        if idx < 0 or idx >= self.size:
            raise IndexError('list index out of range')
        self.data[idx] = value

    def __delitem__(self, idx):
        """ Implements del self[idx] """
        assert isinstance(idx, int), 'Index must be an integer'
        if idx < 0:
            idx += self.size
        if idx < 0 or idx >= self.size:
            raise IndexError('list index out of range')
        for i in range(idx, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1

    """ stringification """

    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""
        if self.size == 0:
            return "[]"
        elements = [str(self.data[i]) for i in range(self.size)]
        return "[" + ", ".join(elements) + "]"

    def __repr__(self):
        """Implements `repr(self)`. Similar to `__str__`, but represents the
        list as an expression that could be evaluated to reproduce the list."""
        return '[' + ', '.join(repr(self.data[i]) for i in range(self.size)) + ']'

    """ single-element manipulation """

    def append(self, value):
        """Appends value to the end of this list."""
        if self.size == len(self.data):  # if the backing array is full
            n_data = np.empty(len(self.data) * 2, dtype=object)  # create a new one with double the capacity
            for i in range(self.size):  # copy elements over
                n_data[i] = self.data[i]
            self.data = n_data  # replace our backing store with the new array

        self.data[self.size] = value
        self.size += 1

    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements
        down the list, as needed. Note that inserting a value at len(self) ---
        equivalent to appending the value --- is permitted. Raises IndexError
        if idx is invalid."""
        if idx < 0:
            idx += self.size
        if idx < 0 or idx > self.size:
            raise IndexError("Index out of range")
        if self.size == len(self.data):
            n_data = np.empty(len(self.data) * 2, dtype=object)  # create a new one with double the capacity
            for i in range(len(self.data)):  # copy elements over
                n_data[i] = self.data[i]
            self.data = n_data  # replace our backing store with the new array
        for i in range(self.size, idx, -1):
            self.data[i] = self.data[i - 1]
        self.data[idx] = value
        self.size += 1

    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""
        if self.size == 0:
            raise IndexError("pop from empty list")
        if self.size < 0:
            idx += self.size
        if idx < 0 or idx >= self.size:
            raise IndexError("index out of range")
        value = self.data[idx]
        for i in range(idx, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1
        return value

    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""
        for i in range(self.size):
            if self.data[i] == value:
                for j in range(i, self.size -1):
                    self.data[j] = self.data[j + 1]
                self.size -= 1
                return value
        raise ValueError("value not found in list")

    """ predicates (T/F queries) """

    def __eq__(self, other):
        """Returns True if this ArrayList contains the same elements (in order)
        as others. If other is not an ArrayList, returns False."""
        if not isinstance(other, ArrayList):
            return False
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this
        list."""
        for i in range(self.size):
            if self.data[i] == value:
                return True
        return False

    """ queries """

    def __len__(self):
        """Implements `len(self)`"""
        return self.size

    def min(self):
        """Returns the minimum value in this list."""
        if self.size == 0:
            raise ValueError("List is empty")
        min_value = self.data[0]
        for i in range(1, self.size):
            if self.data[i] < min_value:
                min_value = self.data[i]
        return min_value

    def max(self):
        if self.size == 0:
            raise ValueError("List is empty")
        max_value = self.data[0]
        for i in range(1, self.size):
            if self.data[i] > max_value:
                max_value = self.data[i]
        return max_value

    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""
        if j is None:
            j = self.size
        if i < 0:
            i += self.size
        if j < 0:
            j += self.size
        if i < 0 or i >= self.size or j < 0 or j > self.size:
            raise ValueError("Index out of range")

        for index in range(i, j):
            if self.data[index] == value:
                return index

        raise ValueError("value not found in list")

    def count(self, value):
        """Returns the number of times value appears in this list."""
        count = 0
        for i in range(self.size):
            if self.data[i] == value:
                count += 1
        return count

    """ bulk operations """

    def __add__(self, other):
        """Implements `self + other_array_list`. Returns a new ArrayList
        instance that contains the values in this list followed by those
        of others."""
        if not isinstance(other, ArrayList):
            raise TypeError("Unsupported operand type(s) for ArrayList and '{}'".format(type(other).__name__))

        new_list = ArrayList()
        new_list.data = np.empty(self.size + other.size, dtype=object)
        new_list.size = self.size + other.size

        for i in range(self.size):
            new_list.data[i] = self.data[i]

        for i in range(other.size):
            new_list.data[self.size + i] = other.data[i]

        return new_list

    def clear(self):
        self.data = np.empty(1, dtype=object)
        self.size = 0

    def copy(self):
        """Returns a new ArrayList instance (with a separate data store), that
        contains the same values as this list."""
        new_list = ArrayList()
        new_list.data = np.empty(self.size, dtype=object)
        new_list.size = self.size

        for i in range(self.size):
            new_list.data[i] = self.data[i]

        return new_list

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this
        list."""
        try:
            iterator = iter(other)
        except TypeError:
            raise TypeError("'{}' object is not an iterable".format(type(other).__name__))

        for item in iterator:
            self.append(item)

    """ iteration """

    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        for i in range(self.size):
            yield self.data[i]
