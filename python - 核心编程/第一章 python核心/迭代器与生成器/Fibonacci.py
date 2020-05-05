def  Fib(n):
    a,b=0,1
    while b <= n:
        yield b
        a ,b =b,a+b

for  x in Fib(5):
    print(x)