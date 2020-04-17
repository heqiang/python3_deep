import os

#目录遍历
path=input("请输入目录")
for dirpath,dirnames,filenames in os.walk(path):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            print(fullpath)


