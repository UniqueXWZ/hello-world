# hello-world
'my first repository'
from functools import reduce
l = [1, 2, 3, 4, 5, 6]
l1 = map(lambda x: x**2, l)
res = reduce(lambda x, y: x+y, l1)
print('result is %d' %res)
