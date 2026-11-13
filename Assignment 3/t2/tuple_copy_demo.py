import copy, sys

coordinates = [('A', (2, 3)), ('B', (5, 8))]
print('Bus stops:', coordinates)

row = [0, 0, 0]
shared = [row, row, row]
shared[0][1] = 9
print('Buggy shared row grid:', shared)

correct = [[0 for _ in range(3)] for _ in range(3)]
correct[0][1] = 9
print('Correct grid:', correct)

a = [[1, 2], [3, 4]]
b = a
c = a.copy()
d = copy.deepcopy(a)
a[0][0] = 99
print('a:', a)
print('b alias:', b)
print('c shallow copy:', c)
print('d deep copy:', d)
print('List size:', sys.getsizeof([1, 2, 3]))
print('Tuple size:', sys.getsizeof((1, 2, 3)))
print('Tuple keys are immutable and hashable; lists are mutable and not hashable as dictionary keys.')
