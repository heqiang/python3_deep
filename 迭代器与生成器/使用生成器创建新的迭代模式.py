from itertools import dropwhile
class cutDown(object):
    def __init__(self,start):
        self.start=start
    def __iter__(self):
        n=self.start
        while n > 0:
            yield n
            n-=1
    def  __reversed__(self):
        n = 1
        while n<=self.start:
                yield n
                n += 1
for x in reversed(cutDown(30)):
    print(x)

with open("file_name.txt",'r') as f:
    for line  in  dropwhile(lambda line:line.startwith("#"),f):
        print(line,end='')


# for x in cutDown(30):
#     print(x)