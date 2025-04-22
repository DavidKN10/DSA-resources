import pytest
import random
from linkedlist import LinkedList

class TestLinkedList:
    @pytest.mark.points(6)
    def test_subscript_access(self):
        # (6 points) test subscript-based access
        data = [1, 2, 3, 4]
        lst = LinkedList()
        for d in data:
            lst.append(d)

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
        lst = LinkedList()
        for d in data:
            lst.append(d)

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

    @pytest.mark.points(6)
    def test_cursor_access(self):
        ### (6 points) test cursor-based access

        ## insert a bunch of values at different cursor positions

        lst1 = []
        lst2 = LinkedList()
        for _ in range(100):
            val = random.randrange(1000)
            lst1.append(val)
            lst2.append(val)

        for _ in range(10):
            pos = random.randrange(len(lst1))
            vals = [random.randrange(1000) for _ in range(10)]
            lst1[pos+1:pos+1] = vals
            lst2.cursor_set(pos)
            for x in vals:
                lst2.cursor_insert(x)

        assert len(lst1) == len(lst2)
        for i in range(len(lst1)):
            assert lst1[i] == lst2[i]

        ## move the cursor around and check that values are correct
            
        lst1 = []
        lst2 = LinkedList()
        for _ in range(100):
            val = random.randrange(1000)
            lst1.append(val)
            lst2.append(val)

        idx = 0
        lst2.cursor_set(0)
        for _ in range(100):
            offset = random.randrange(-200, 200)
            idx = (idx + offset) % 100
            lst2.cursor_move(offset)
            assert lst1[idx] == lst2.cursor_get()

        ## move the cursor around and delete values at the cursor

        lst1 = []
        lst2 = LinkedList()
        for _ in range(500):
            val = random.randrange(1000)
            lst1.append(val)
            lst2.append(val)

        idx = 0
        lst2.cursor_set(0)
        for _ in range(100):
            offset = random.randrange(-200, 200)
            idx = (idx + offset) % len(lst1)
            lst2.cursor_move(offset)
            del lst1[idx]
            lst2.cursor_delete()
            
        assert len(lst1) == len(lst2)
        for i in range(len(lst1)):
            assert lst1[i] == lst2[i]

        ## deleting the last element via the cursor should work correctly
        lst2.cursor_set(len(lst2)-1)
        lst2.cursor_delete()
        assert lst2.cursor is lst2.head.next

    @pytest.mark.points(2)
    def test_stringification(self):
        # (2 points) test stringification

        lst = LinkedList()
        assert '[]' == str(lst)
        assert '[]' == repr(lst)

        lst.append(1)
        assert '[1]' == str(lst)
        assert '[1]' == repr(lst)

        lst = LinkedList()
        for d in (10, 20, 30, 40, 50):
            lst.append(d)
        assert '[10, 20, 30, 40, 50]' == str(lst)
        assert '[10, 20, 30, 40, 50]' == repr(lst)

    @pytest.mark.points(6)
    def test_single_elem_manip(self):
        # (6 points) test single-element manipulation
        lst = LinkedList()
        data = []

        for _ in range(100):
            to_ins = random.randrange(1000)
            ins_idx = random.randrange(len(data)+1)
            data.insert(ins_idx, to_ins)
            lst.insert(ins_idx, to_ins)

        for i in range(100):
            assert data[i] == lst[i]

        for _ in range(50):
            pop_idx = random.randrange(len(data))
            assert data.pop(pop_idx) == lst.pop(pop_idx)
            
        for i in range(50):
            assert data[i] == lst[i]

        for _ in range(25):
            to_rem = data[random.randrange(len(data))]
            data.remove(to_rem)
            lst.remove(to_rem)
            
        for i in range(25):
            assert data[i] == lst[i]

        with pytest.raises(ValueError):
            lst.remove(9999)

    @pytest.mark.points(4)
    def test_predicates(self):
        # (4 points) test predicates
        lst = LinkedList()
        lst2 = LinkedList()

        assert lst == lst2

        lst2.append(100)
        assert lst != lst2

        lst.append(100)
        assert lst == lst2

        assert 1 not in lst
        assert None not in lst

        lst = LinkedList()
        for i in range(100):
            lst.append(i)
        assert 100 not in lst
        assert 50 in lst

    @pytest.mark.points(6)
    def test_queries(self):
        # (6 points) test queries
        lst = LinkedList()

        assert 0 == len(lst)
        assert 0 == lst.count(1)
        with pytest.raises(ValueError):
            lst.index(1)

        import random
        data = [random.randrange(1000) for _ in range(100)]
        for d in data:
            lst.append(d)

        assert 100 == len(lst)
        assert min(data) == lst.min()
        assert max(data) == lst.max()
        for x in data:    
            assert data.index(x) == lst.index(x)
            assert data.count(x) == lst.count(x)

        with pytest.raises(ValueError):
            lst.index(1000)

        lst = LinkedList()
        for d in (1, 2, 1, 2, 1, 1, 1, 2, 1):
            lst.append(d)
        assert 1 == lst.index(2)
        assert 1 == lst.index(2, 1)
        assert 3 == lst.index(2, 2)
        assert 7 == lst.index(2, 4)
        assert 7 == lst.index(2, 4, -1)
        with pytest.raises(ValueError):
            lst.index(2, 4, -2)

    @pytest.mark.points(6)
    def test_bulk(self):
        # (6 points) test bulk operations
        lst = LinkedList()
        lst2 = LinkedList()
        lst3 = lst + lst2

        assert isinstance(lst3, LinkedList)
        assert 0 == len(lst3)

        import random
        data  = [random.randrange(1000) for _ in range(50)]
        data2 = [random.randrange(1000) for _ in range(50)]
        for d in data:
            lst.append(d)
        for d in data2:
            lst2.append(d)
        lst3 = lst + lst2
        assert 100 == len(lst3)
        data3 = data + data2
        for i in range(len(data3)):
            assert data3[i] == lst3[i]

        lst.clear()
        assert 0 == len(lst)
        with pytest.raises(IndexError):
            lst[0]

        for d in data:
            lst.append(d)
        lst2 = lst.copy()
        assert lst is not lst2
        assert lst.head.next is not lst2.head.next
        for i in range(len(data)):
            assert lst[i] == lst2[i]
        assert lst == lst2

        lst.clear()
        lst.extend(range(10))
        lst.extend(range(10,0,-1))
        lst.extend(data.copy())
        assert 70 == len(lst)

        data = list(range(10)) + list(range(10, 0, -1)) + data
        for i in range(len(data)):
            assert data[i] == lst[i]

    @pytest.mark.points(2)
    def test_iteration(self):
        # (2 points) test iteration
        lst = LinkedList()

        import random
        data = [random.randrange(1000) for _ in range(100)]
        lst = LinkedList()
        for d in data:
            lst.append(d)
        assert data == [x for x in lst]

        it1 = iter(lst)
        it2 = iter(lst)
        for x in data:
            assert next(it1) == x
            assert next(it2) == x
