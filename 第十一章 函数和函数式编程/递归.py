def fib(num):
    n0=1
    n1=1
    count=2
    print(n0,n1,end=',')
    while count < num:
        next=n0+n1
        print(next,end=',')
        n0=n1
        n1=next
        count+=1
fib(8)
print()
#阶乘
def jiecheng(num):
    if num < 2:
        return 1
    else:
        return num*jiecheng((num-1))
res=jiecheng(5)
print(res)