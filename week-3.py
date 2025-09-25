"""bubble sort """

# data = [5,3,4,41]
# len = len(data)
# for i in range(len):
#     count = 0
#     for j in range(len-i-1):
#         if(data[j]>data[j+1]):
#             temp = data[j]
#             data[j] = data[j+1]
#             data[j+1] = temp
#             count +=1
#     if count == 0:
#         break 
# print(data)

"""
-> to do 
roman to integer leetcode , interger to roman 
"""

'''sq of each element in the list'''
# data = [1,2,3,3,4,4,5]
# li = [x**2 for x in data]
# print(li)

"""
dictionary comprehension
dictionary k andr jo key h vo ek single value hoti h jese ki string,int,float,boolean 
and if we talk about the values then in value any data types can be there even the collections too.

if we want to access the value of a key in dictionary we can use the key as a index here

agar dictionary m key h toh fir vo update hogi aur agr vo key exist nahi krti toh nahi key create hogi

it is mutable and it is ordered

before the python version 3.7 dictionary was unordered and after the version 3.7 it is ordered

"""
# data = {chr(k):k for k in range(65,71)}
# print(data)

# data = {'age': 20 , 'name' : 'Arpit'}
# data['age'] = 20
# data['loc'] = 'bhulgaon'

# print(data)

"""
                                            SET
if we want to create a empty set we can use the set keyword : a= set() and we can also create a set including the values in it : a = {1,2,3,}
we can use add method if we want to insert a value in it and that method is a.add(# value)
"""

"""
                                                        High ordered function
A function in which another function se sent as an arguments below is the given solution for it.
"""
# def add(a,b):
#     return a+b

# def operation(a,b,c):
#     return c(a,b)

# print(operation(10,20,add))

# sq = lambda x:x**2
# half = lambda x:x//2

# def high(a,b,c):
#     return a(b(c))
# print(high(sq,half,12))

""" 
                                        variable argument function 
* is used to send the variable argument if we want to send it  eg below. this is used to take the multiple lines of input.
 """
# def sum(*argument):
#     sum = 0
#     for i in argument:
#         sum+=i
#     return sum

# print(sum(11,12,13,14,15))

'sum of the numbers divisible by 3 and 5 '
# def sum(*argument):
#     s = 0
#     for i in argument:
#         if i % 3 == 0 and i % 5 == 0:
#             s+=i
#     return s
# print(sum(1,2,3,15,30,45))

'flatten a nested list'
'brute force'
# data = [[1,2,3],[4,5,6],[7,8,9]]

# def flated(x):
#     res = []
#     for i in x:
#         for j in i:
#             res.append(j)
#     return res

# print(flated(data))

'optimal or shortcut if the number of element changes it will throw error'
# data = [[1,2,3],[4,5,6],[7,8,9]]
# new = []
# for a,b,c in data:
#     new.append(a)
#     new.append(b)
#     new.append(c)
# print(new)