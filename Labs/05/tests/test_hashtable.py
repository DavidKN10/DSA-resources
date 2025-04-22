import pytest
import random
from hashtable import OrderedHashtable

class TestHashtable:
    @pytest.mark.points(3)
    def test_simple(self):
        # (3 tests) Short tests
        ht = OrderedHashtable(2)

        for k, v in (('batman', 'bruce wayne'), ('superman', 'clark kent'), ('spiderman', 'peter parker')):
            ht[k] = v
            
        assert len(ht) == 3
        assert ht['superman'] == 'clark kent'

        assert 'spiderman' in ht
        assert 'iron man' not in ht

        with pytest.raises(KeyError):
            ht['iron man']

    @pytest.mark.points(3)
    def test_basic_ops(self):
        # (3 points) Basic tests (insertion, fetch, count, chain-lengths)
        class MyInt(int):
            def __hash__(self):
                """MyInts hash to themselves — already current Python default, 
                but just to ensure consistency."""
                return self
            
        def ll_len(l):
            """Returns the length of a linked list with head `l` (assuming no sentinel)"""
            c = 0
            while l:
                c += 1
                l = l.next
            return c
            
        ht = OrderedHashtable(10)
        for i in range(25):
            ht[MyInt(i)] = i*2

        assert len(ht) == 25

        for i in range(5):
            assert ll_len(ht.indices[i]) == 3
            
        for i in range(5, 10):
            assert ll_len(ht.indices[i]) == 2

        for i in range(25):
            assert MyInt(i) in ht
            assert ht[MyInt(i)] == i*2

    @pytest.mark.points(3)
    def test_updates(self):
        # (3 points) Update testing
        ht = OrderedHashtable(100)
        d = {}

        for i in range(100):
            k, v = str(i), str(i*2)
            d[k] = v
            ht[k] = v
            
        for j in range(0, 100, 2):
            k, v = str(i), str(i*3)
            d[k] = v
            ht[k] = v
            
        for j in range(0, 100, 4):
            k, v = str(i), str(i*4)
            d[k] = v
            ht[k] = v
            
        for i in range(100):
            assert k in ht
            assert d[k] == ht[k]

    @pytest.mark.points(3)
    def test_deletion(self):
        # (3 points) Deletion testing
        ht = OrderedHashtable(100)
        d = {}

        for i in range(100):
            k, v = str(i), str(random.randrange(10000000, 99999999))
            d[k] = v
            ht[k] = v

        for _ in range(50):
            k = str(random.randrange(100))
            if k in d:
                del d[k]
                del ht[k]

        assert len(ht) == len(d)

        for k,v in ht.items():
            assert d[k] == v

    @pytest.mark.points(4)
    def test_iteration_order(self):
        # (4 points) Iteration order testing
        ht = OrderedHashtable(1000)
        l = [str(i) for i in range(0, 1000)]
        random.shuffle(l)

        for x in l:
            ht[x] = x

        for _ in range(50):
            idx_to_del = random.randrange(len(l))
            val_to_del = l[idx_to_del]
            del ht[val_to_del]
            del l[idx_to_del]
            if random.randrange(2) == 0:
                l.append(val_to_del)
                ht[val_to_del] = val_to_del

        for x, y in zip(l, ht):
            assert x == y

    @pytest.mark.points(4)
    def test_stress(self):
        # (5 points) Stress testing
        from time import time
        ht = OrderedHashtable(100000)
        d = {}

        start = time()
        for _ in range(100000):
            k, v = str(random.randrange(100000)), str(random.randrange(10000000, 99999999))
            d[k] = v
            ht[k] = v
            
        for k,v in d.items():
            assert k in ht
            assert d[k] == ht[k]
        end = time()
        print(end-start)
        assert end-start < 1.5, 'Your implementation ran too slow!'
