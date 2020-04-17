def createNum(n):
    for x in  range(n):
        yield x**3
for x in createNum(5):
    print(x,end=',')
print()
#生成的send方法
temp=set()
def test():
    while True:
        a=yield
        temp.add(a)
t=test()
t.send(None)
for x in  range(5):
    t.send(x)
t.close()
print(temp)

def a():
    print('aaa')
    p1 = yield '123'
    if (p1 == 'hello'):
        print('p1是send传过来的')

r = a()
next(r)

print()
def generator():
    for x in range(6):
        a=yield x
        print(a)
t=generator()
next(t)
for x in range(3):
    t.send(x)
t.close()

temp=set()
def test():
    while 1:
        a=yield
        temp.add(a)

t=test()
#或者 next(t)
t.send(None)
for x  in range(5):
    t.send(x)
print(temp)
