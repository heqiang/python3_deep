# -*- coding:utf-8 -*-

def cutDown(n):
    while n > 0:
        yield n
        n-=1
    print("Done")

if __name__ == '__main__':
    for x in cutDown(5):
        print(x,end=',')


