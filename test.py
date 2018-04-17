#coding:utf-8
a = {'a':0,'b':1,'c':2}
d = [x(y) for x in [lambda s: a[s]*2 for s in a ]for y in 'abc']
print(d)
