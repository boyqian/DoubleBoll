#-* - coding: UTF-8 -* -
"""
@project=pythonWeb
@file=test
@author=Administrator
@createTime=2018/10/17 17:03
"""
import  random
list1=[]
while True:
    list1.append(random.choice(range(1, 34)))
    list1=list(set(list1))
    if len(list1)==6:
        break
print(list1)

