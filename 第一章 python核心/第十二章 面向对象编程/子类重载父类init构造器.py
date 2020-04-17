class Father(object):
    def __init__(self, name):
        self.name = name
        print("name: %s" % (self.name))

    def getName(self):
        return 'Father ' + self.name


class Son(Father):
    def __init__(self, name,age):
        '''
        以下两种方式皆可实现对父类构造器的重写 简而言之少写了 self.name=name
        '''
        # Father.__init__(self,name)
        super(Son, self).__init__(name)
        self.age=age

if __name__ == '__main__':
    son = Son('runoob',15)
    print(son.age)
    print(son.getName())