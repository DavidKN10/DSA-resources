import pytest
import random
import numpy as np
from arraylist import ArrayList

class TestArrayList:
    @pytest.mark.points(6)
    def test_subscript_access(self):
        lst = ArrayList()
        data = [1, 2, 3, 4]
        lst.data = np.array(data, dtype=object)
        lst.size = 4

        for i in range(len(data)):
            assert lst[i] == data[i]
        
        with pytest.raises(IndexError):
            x = lst[100]

        with pytest.raises(IndexError):
            lst[100] = 0

        with pytest.raises(IndexError):
            del lst[100]

        lst[1] = data[1] = 20
        del data[0]
        del lst[0]

        for i in range(len(data)):
            assert lst[i] == data[i]

        data = [random.randint(1, 100) for _ in range(100)]
        lst.data = np.array(data, dtype=object)
        lst.size = len(data)

        for i in range(len(data)):
            lst[i] = data[i] = random.randint(101, 200)
        for i in range(50):
            to_del = random.randrange(len(data))
            del lst[to_del]
            del data[to_del]

        for i in range(len(data)):
            assert lst[i] == data[i]
            
        for i in range(0, -len(data), -1):
            assert lst[i] == data[i]

    @pytest.mark.points(4)
    def test_stringification(self):
        lst = ArrayList()
        assert isinstance(lst.data, np.ndarray)
        assert '[]' == str(lst)
        assert '[]' == repr(lst)

        lst.data = np.array([1])
        lst.size = 1

        assert '[1]' == str(lst)
        assert '[1]' == repr(lst)

        lst.data = np.array([10, 20, 30, 40, 50, None, None, None, None, None])
        lst.size = 5

        assert '[10, 20, 30, 40, 50]' == str(lst)
        assert '[10, 20, 30, 40, 50]' == repr(lst)

    @pytest.mark.points(8)
    def test_single_elem_manip(self):
        lst = ArrayList()
        data = []

        for _ in range(100):
            to_add = random.randrange(1000)
            data.append(to_add)
            lst.append(to_add)

        assert isinstance(lst.data, np.ndarray)
        assert data == list(lst.data[:len(data)])

        for _ in range(100):
            to_ins = random.randrange(1000)
            ins_idx = random.randrange(len(data)+1)
            data.insert(ins_idx, to_ins)
            lst.insert(ins_idx, to_ins)

        assert data == list(lst.data[:len(data)])

        for _ in range(100):
            pop_idx = random.randrange(len(data))
            assert data.pop(pop_idx) == lst.pop(pop_idx)
            
        assert data == list(lst.data[:len(data)])

        for _ in range(25):
            to_rem = data[random.randrange(len(data))]
            data.remove(to_rem)
            lst.remove(to_rem)
            
        assert data == list(lst.data[:len(data)])

        with pytest.raises(ValueError):
            lst.remove(9999)

    @pytest.mark.points(4)
    def test_predicates(self):
        lst = ArrayList()
        lst2 = ArrayList()

        lst.data = np.empty(1, dtype=object)
        lst.size = 0
        lst2.data = np.array([1, 2, 3], dtype=object)
        lst2.size = 3
        assert lst != lst2

        lst.data = np.array([1, 2, 3, None, None, None], dtype=object)
        lst.size = 3
        assert lst == lst2

        lst.size = 0
        assert 1 not in lst
        assert None not in lst

        lst.data = np.array(range(100), dtype=object)
        lst.size = 100
        assert 100 not in lst
        assert 50 in lst

    @pytest.mark.points(10)
    def test_queries(self):
        lst = ArrayList()

        assert 0 == len(lst)
        assert 0 == lst.count(0)
        with pytest.raises(ValueError):
            lst.index(1)

        import random
        data = [random.randrange(1000) for _ in range(100)]
        lst.data = np.array(data, dtype=object)
        lst.size = 100

        assert 100 == len(lst)
        assert min(data) == lst.min()
        assert max(data) == lst.max()
        for x in data:    
            assert data.index(x) == lst.index(x)
            assert data.count(x) == lst.count(x)

        with pytest.raises(ValueError):
            lst.index(1000)
            
        lst.data = np.array([1, 2, 1, 2, 1, 1, 1, 2, 1], dtype=object)
        lst.size = 9
        assert 1 == lst.index(2)
        assert 1 == lst.index(2, 1)
        assert 3 == lst.index(2, 2)
        assert 7 == lst.index(2, 4)
        assert 7 == lst.index(2, 4, -1)
        with pytest.raises(ValueError):
            lst.index(2, 4, -2)

    @pytest.mark.points(6)
    def test_bulk(self):
        lst = ArrayList()
        lst2 = ArrayList()
        lst3 = lst+lst2

        assert isinstance(lst3, ArrayList)
        assert isinstance(lst3.data, np.ndarray)
        assert lst3.size == 0

        data  = [random.randrange(1000) for _ in range(50)]
        data2 = [random.randrange(1000) for _ in range(50)]
        lst.data = np.array(data, dtype=object)
        lst.size = len(data)
        lst2.data = np.array(data2, dtype=object)
        lst2.size = len(data2)
        lst3 = lst + lst2
        assert 100 == len(lst3)
        assert data + data2 == list(np.array(lst3.data[:len(data + data2)],
                                              dtype=object))

        lst.clear()
        assert isinstance(lst.data, np.ndarray)
        assert 0 == lst.size

        lst.data = np.array([random.randrange(1000) for _ in range(50)], dtype=object)
        lst.size = 50
        lst2 = lst.copy()
        assert lst is not lst2
        assert lst.data is not lst2.data
        assert np.all(lst.data[:50] == lst2.data[:50])

        lst.clear()
        lst.extend(range(10))
        lst.extend(range(10,0,-1))
        lst.extend(data.copy())
        assert 70 == len(lst)
        assert list(range(10))+list(range(10,0,-1))+data == list(lst.data[:70])

    @pytest.mark.points(2)
    def test_iteration(self):
        lst = ArrayList()
        data = [random.randrange(1000) for _ in range(100)]
        lst.data = np.array(data, dtype=object)
        lst.size = len(data)
        assert data, [x for x in lst]

        it1 = iter(lst)
        it2 = iter(lst)
        for x in data:
            assert next(it1) == x
            assert next(it2) == x
