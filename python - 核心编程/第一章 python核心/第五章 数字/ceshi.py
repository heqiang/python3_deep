a=input("请输入你想要兑换的美元金额")
print(a)
a=float(a)

if a < 1:
    a=a*100
    a=divmod(a,25)
    if a[0]>0:
        print("可以得到{}枚25美分".format(a))
    


