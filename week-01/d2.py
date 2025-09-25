# infinite for loop
# data = [0]
# for i in data:
#     data.append(i+1)
#     print(data[i])

# a  = 1234
# sum = 0
# rev = 0
# while a>0:
#     ld = a%10
#     sum += ld
#     rev = rev*10 + ld
#     a = a // 10
# print("the sum of all digits of number:",sum)
# print("the reversed number is:",rev)


# data = 12345
# sum = 0
# while data>0:
#     ld = data %10
#     sum += ld
#     data //= 10
#     if data==0 and sum//9 !=0:
#         data = sum
#         sum =0
# print(sum)

# find the factorial

# a = int(input())
# fact = 1
# while a>0:
#     fact *= a
#     a-=1
# print(fact)

# a = int(input())
# b = int(input())
# sum = 0
# while a<=b:
#     sum += a
#     a+= 1
# print(sum)

# a = int(input())
# num = a
# n = len(str(a))
# sum = 0
# while a>0:
#     ld = a %10
#     sum += ld ** n
#     a //= 10
# if sum == num:
#     print("yes, it is ")
# else:
#     print("no, it is not")

# list = []
# while 'a':
#     decision = input()
#     if 'add' in decision:
#         a= decision.split('add')
#         list.append(a[1])
#         print(list)
#     elif 'find' in decision:
#         a= decision.split('find')
#         count = 0
#         for i in list:
#             count += i.count(a[1])
#         print(count)
#     elif decision == 'end':
#         break

# strong number

# def factorial(n):
#     fact=1 
#     while n >0:
#         fact*=n
#         n-=1
#     return fact

# n = int(input())
# num = n
# sum = 0
# while n>0:
#     ld = n % 10 
#     sum += factorial(ld)
#     n//=10
# if sum == num:
#     print("it is a strong number")
# else:
#     print("no")

for i in range(7):
    for j in range(7):
        if (i-j)**2 == 3:
            print("*",end=" ")
        else:
            print(" ",end=" ")