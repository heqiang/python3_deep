#文件过滤. 显示一个文件的所有行, 忽略以井号( # )开头的行. 这个字符被用做 Python , Perl, Tcl, 等大多脚本文件的注释符号.
f=open("hhga.txt",'r')
res=[x for x in f  if not  x.startswith("#")]
print(res)
f.close()
#文件访问. 提示输入数字 N 和文件 F, 然后显示文件 F 的前 N 行
filename=input("请输入文件路径")
f=open("{0}".format(filename),'r')
row=input("显示多少行")
for count,line in  enumerate([x for x in f if not x.startswith("#")]):
     if  count<int(row):
        print("{0} {1}".format(count,line))
     else:
        break
f.close()
#文件信息. 提示输入一个文件名, 然后显示这个文本文件的总行数
f=open("hhga.txt",'r')
sum_rows=len(f.readlines())
print(sum_rows)