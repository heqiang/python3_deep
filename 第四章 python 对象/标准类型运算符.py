#数值和字符串对象是不可变的 每一次的新对象被创建 取代了旧的对象 地址已经变了
y="hello"
print("y 的地址是 :{0}".format(id(y)))
y=0
print("y 的地址是 :{0}".format(id(y)))
