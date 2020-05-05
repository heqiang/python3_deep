myDict = {'host': 'earth', 'port': 80}
myDict.setdefault("ceshi",55)
print(myDict)
frozenset1=frozenset('1')
print(frozenset1)
# myDict1={}
# myDict1=myDict1.fromkeys(frozenset1)
# print(myDict1)

list1=[1, 2, 3]
list2=['abc', 'def', 'ghi']
dict1=zip(list1,list2)
dict1=dict(dict1)
print(dict1)