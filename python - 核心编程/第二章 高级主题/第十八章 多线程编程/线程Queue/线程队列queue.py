#队列
# 先进先出
#  可以存放任意类型数据
import queue

q = queue.Queue(maxsize=10)
q.put('1')
q.put(1)
q.put({"num":12})

print(q.get())
print(q.get())
print(q.get()['num'])
print("*"*50)

#堆栈Queue 可以存放任意类型数据 Lifo代表后进先出
q1 = queue.LifoQueue()
q1.put('1')
q1.put(1)
q1.put({"num":12})
print(q1.get())
print(q1.get())
print(q1.get())
print("*"*50)
#优先级队列
# 存放的数据是元组类型，带有优先级数字越小优先级越高。
# 数据优先级高的优先被取出。
# 用于VIP用户数据优先被取出场景，因为上面两种都要挨个取出。
q2 = queue.PriorityQueue()
q2.put((10, 'Q'))
q2.put((30, 'Z'))
q2.put((20, 'A'))

print(q2.get())
print(q2.get())
print(q2.get())