import main
import p2
from p2 import ArrayList

l = ['reed', 'bar', 'deer', 'peels', 'foo', 'sleep']
output1 = main.f01(l)
print(output1)


d = {
    'tom': {1, 2, 3},
    'jack': {4, 6},
    'TOM': {2, 3, 4},
    'Tom': {3, 4, 5},
    'JACK': {5, 7}
}

output2 = main.f02(d)
print(output2)

m = 3
n = 6
c = '*'

output = main.f03(m, n, c)
print(output)


passage = 'the cat sat on the mat'
subs = {'cat': 'dog', 'mat': 'rug'}

output3 = main.f04(passage, subs)
print(output3)


s1 = 'the cat sat on the mat'
s2 = 'the dog sat on the rug'

output = main.f05(s1, s2)
print(output)




# Create an instance of ArrayList
arr_list = ArrayList()

# Add elements to the ArrayList
arr_list.append('c')
arr_list.append('o')
arr_list.append('m')
arr_list.append('p')
arr_list.append('u')
arr_list.append('t')
arr_list.append('e')
arr_list.append('r')

# Test iter_in_order method
idxs = [3, 1, 1, 7, 2, 6]
output = list(arr_list.iter_in_order(idxs))
print(output)


# Create an instance of ArrayList
arr_list = ArrayList()

# Add elements to the ArrayList
for i in range(10):
    arr_list.append(i)

# Test move_range method
arr_list.move_range(src=1, dst=6, n=3)
print(arr_list)