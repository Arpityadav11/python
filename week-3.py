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

'function to reverse a string without using slicing'
# def reverse(s):
#     new = ''
#     for i in range(len(s)-1,-1,-1): # for i in s:
#         new += s[i]                 #   new=i+new
#     return new
# print(reverse('arpit'))

'OR'

# def reverse(s):
#     new = ''
#     for i in reversed(s): 
#         new += i                 
#     return new
# print(reverse('arpit'))

'''
                                                                Recursion
When a function call itself again and again then it is a Recursive function.
The recursive function can be stopped using the base case.
'''
# def f1():
#     print('hello')
#     return f1()
# f1()

'print number from 10 to 1 using recursion'
# def count(n=10):

'sum of the numbers'
# def sum(n=10):
#     if n<=0:
#         return 0
#     else:
#         return n+sum(n-1)
# print(sum())

'factorial of a number'
# def factorial(n):
#     if n>1:
#         return n * factorial(n-1)
#     else:
#         return 1
# print(factorial(5))

'reverse a string'
# def reverse(s,i=0,new = ''):
#     if i==len(s):
#         return new
#     else:
#         new = s[i] + new
#         return reverse(s,i+1,new)

# print(reverse('lucky'))

''' 
                                                            keyword argument
this is done using the double astric i.e. ** and the arguments are stored in the key value pairs. The data is stored in dictionary.
'''
# def k1(**kw):
#     print(kw)

# k1(a=1,b=2,c=3)

'Q.1 '
# def k1 (**kwargs):
#     return kwargs['a']
# print(k1(b=10,a=9))

"""
                                                            nested function
Function is written inside of a function
If there are two given function and if we are writing a nested function then we can return the whole function that is written inside.
"""

"""
                                                            Nested recursive function
printing the nested for loop
"""
# def f2(b):
#     def f1(a):
#         if a == 11:
#             return f2(b+1)
#         print(a,end=' ')
#         return f1(a+1)
#     if b<=10:
#         print()
#         return f1(1)
#     else:
#         return 1
# f2(1)

"""atm simulation"""
# from tkinter import messagebox
# def atm():
#     global balance
#     global pin
#     pin=123
#     balance=100000
# atm()
# def deposit(amount):
#     global balance
#     balance+=amount
# def check_balance():
#     print(balance)
# def withdraw(amount):
#     global balance
#     auth_pin=int(input("enter the pin : "))
#     if amount <= balance and pin==auth_pin:
#         balance-=amount
#         messagebox.showinfo("success","paisa gaya ...")
#     elif amount >balance:
#         messagebox.showinfo("failure","aukat m ")
#     else:
#         messagebox.showinfo("failure","wrong pin")

# def change_pin(old_pin_input, new_pin_input):
#     global pin
#     if old_pin_input == pin:
#         pin = new_pin_input
#         print("PIN changed successfully.")
#     else:
#         print("Incorrect old PIN. Try again.")
# def main():
#     while True:
#         print("""
#     press 1 for deposit
#     press 2 for check_balance
#     press 3 for withdraw
#     press 4 for change_pin
#     press 0 for exit
#             """)
#         decison=int(input("enter : "))
#         if decison==1:
#             amount=int(input("enter the amount to deposit : "))
#             deposit(amount)
#         elif decison==2:
#             check_balance()
#         elif decison==3:
#             amount=int(input("enter the amount to withdraw : "))
#             withdraw(amount)
#         elif decison==4:
#             new_pin=int(input("enter new pin"))
#             old_pin= int(input("enter old pin"))
#             change_pin(new_pin)
#         if decison ==0:
#             break
# main()

