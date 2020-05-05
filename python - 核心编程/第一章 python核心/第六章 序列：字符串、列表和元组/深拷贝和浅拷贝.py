import copy

a=[1,2,3,4,['a','b',[2]]]
b=a
c=copy.copy(a)
d=copy.deepcopy(a)
a.append(5)
print(a)
print(b)
a[4].append('c')
a[4][2].append(3)
print(a)
print(b)

