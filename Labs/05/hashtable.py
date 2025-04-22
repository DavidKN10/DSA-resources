class OrderedHashtable:
    class Node:
        """This class is used to create nodes in the singly linked "chains" in
        each hashtable bucket."""

        def __init__(self, index, next=None):
            # don't rename the following attributes!
            self.index = index
            self.next = next

    def __init__(self, n_buckets=1000):
        # the following two variables should be used to implement the
        # "two-tiered" ordered hashtable described in class --
        # don't rename them!
        self.indices = [None] * n_buckets
        self.entries = []
        self.count = 0

    def __getitem__(self, key):
        # compute the hash index
        bucket_index = hash(key) % len(self.indices)
        # and get the value at i
        node = self.indices[bucket_index]
        # Using while loop iterate the value until the key is found

        while node is not None:
            if self.entries[node.index][0] == key:
                return self.entries[node.index][1]
            node = node.next
        raise KeyError

    def __setitem__(self, key, val):
        bucket_index = hash(key) % len(self.indices)
        val_index = len(self.entries)
        if self.indices[bucket_index] is None:
            self.entries.append([key, val])
            self.count += 1
            self.indices[bucket_index] = OrderedHashtable.Node(val_index, None)
        else:
            temp_value = self.indices[bucket_index]

            while temp_value:
                n = self.entries[temp_value.index]
                if n[0] == key:
                    n[1] = val
                    return

                if temp_value.next is None:
                    self.entries.append([key, val])
                    temp_value.next = OrderedHashtable.Node(val_index, None)
                    self.count += 1
                    return
                temp_value = temp_value.next

    def __delitem__(self, key):
        # set initial index value to none
        deleted_index = None
        bucket_index = hash(key) % len(self.indices)
        node = self.indices[bucket_index]

        # check if the key matched in the dictionary or not
        if self.entries[node.index][0] == key:
            self.count -= 1
            del self.entries[node.index]
            deleted_index = node.index

            if node.next is not None:
                self.indices[bucket_index] = node.next
            else:
                self.indices[bucket_index] = None
        else:
            while node is not None:
                last_node = node
                node = node.next

                if self.entries[node.index][0] == key:
                    self.count -= 1
                    del self.entries[node.index]
                    deleted_index = node.index
                    last_node.next = node.next
                    break
            else:
                raise KeyError

        for bucket in self.indices:
            node = bucket
            while node is not None:
                if node.index > deleted_index:
                    node.index -= 1
                node = node.next

    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except KeyError:
            return False

    def __len__(self):
        return self.count

    def __iter__(self):
        for key, _ in self.entries:
            yield key

    def keys(self):
        return iter(self)

    def values(self):
        for _, value in self.entries:
            yield value

    def items(self):
        return iter(self.entries)

    def __str__(self):
        return '{ ' + ', '.join(str(k) + ': ' + str(v) for k, v in self.items()) + ' }'

    def __repr__(self):
        return str(self)
