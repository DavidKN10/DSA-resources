from p3 import LinkedList
from p4 import Hashtable
from p5 import Staque

sq = Staque()
sq.push(1)
sq.push(2)
sq.enqueue(3)
sq.enqueue(4)
print(sq.pop() == 2)
print(sq.pop() == 1)
print(sq.dequeue() == 3)
print(sq.dequeue() == 4)
print(not sq)
print(sq.top is None)
print(sq.head is None)
print(sq.tail is None)


"""
ht = Hashtable()
ht['a'] = 1
ht['b'] = 2
ht['c'] = 1
ht['d'] = 2
ht['e'] = 1
print(ht)

nodes = {}
for n in ht.buckets:
    while n is not None:
        nodes[n.key] = n
        n = n.next
print(nodes)

print(ht['a'] == 1)
print(ht['b'] == 2)
print(ht['c'] == 1)
print(ht['d'] == 2)
print(ht['e'] == 1)

old_buckets = ht.buckets
old_nodes = collect_nodes(ht)

ht.del_all_by_val(2)
"""

"""
ll = LinkedList()
for i in range(10):
    ll.append(i)
print(ll.__str__())

print(ll.tail.value == 9)
print(ll.size == 10)
n = ll.tail
for _ in range(9):
    n = n.prior
print(n.value == 0)
print(n.prior is None)

for i in range(10):
    print(ll[i] == i)
for i in range(10):
    ll[i] = str(i)
for i in range(10):
    print(ll[i] == str(i))
del ll[0]
for i in range(9):
    print(ll[i] == str(i + 1))
"""
