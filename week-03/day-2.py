"                     Exception Handling                 """
"""The exception Handling is means that the error or bug """


# try :
#     a=20
#     b=4
#     print(a+b)
    
# except TypeError as j:
#     print(j)
# except Exception as e :
"""the multiple error ke liye multiple "Except laga sakte hai  like ' type error and other error are also print the program """

#     print(e)
# else:
#     print("success")

# finally:
#     print("It will execute always ")




"Q."

# while True:
#     try:
#         a= int(input("Enter the first number: "))
#         b=int(input("Enter the second number :"))
#         print(a/b)
#         break
#     except Exception as e:
#         print("Error --",e)


# def rectangle(n):

   
#     for i in range(n):
#         for j in range(n):
#             if i==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1:
            
#                 print("*",end=" ")
            
#             else:
#                 print(" ",end=' ')
#         print()
# rectangle(9)



"Reverse string without using the slicing "
# n="jayverma"
# s=""
# for i in range(len(n)-1,-1,-1):
#     s+=n[i]
  
# print(s)


"half Uppercase"
# text = "jayverma"
# data = (len(text) // 2)

# sat = text[:data].upper() + text[data:].lower()

# print(sat)


"""check one small letter """
# data=input()
# if any(char.islower() for char in data):
#     print("True")

# else:
#     print("Flase")



"""Check the plindrom """
# def check_palindrom(s):
#     s1=''
#     for i in s :
#         s1=i+s1
    
#     if s1==s:
#         return True
#     else:
#         return False

# check_palindrom("madam")


"print the substring"

# def substring(s):
#     main_str=input()
#     if s in main_str:
#         return True 
#     return False
# print(substring(input()))


"""Remove the substring for the main string"""
# def remove_sub(s):
#     main=input()
#     if s in main:
#         global new
#         new=main.replace(s,' ')
#     return new
# print(remove_sub(input()))



"print the right angle triangle "
# n=6
# for i in range(n):
#     for j in range(n):
#         if i==n-1 or j==0 or i==j:
#             print('*',end=' ')

#         else:
#             print(" ",end=' ')
#     print()



# Q.1 the given of the intger's reargenge that  even and  first odd 
# Q.2 write a function for the longest string without repeting element's
# Q.3 Write a function to sum of all digits number for the user given the number and do not using for the loop 
# Q.4 Write a with using * multiplye the two  number all condition all allow  
# Q.5 Write a extracting element which avaliable greater then k time 
# Q.6 Write a check the largest non repeating element in string 2


"Q.4 Write a with using * multiplye the two  number all condition all allow"
# def multiple(a,b):
#     result =0
#     for i in range(abs(b)):
#         result+=a


#         return result if b >= 0 else- result

# multiple(2,5)




"Q.1 the given of the intger's reargenge that  even and  first odd "
# numbers=[123456789]
# even = []
# odd= []


# for i in numbers:
#     if i % 2 == 0:
#         even.append(sum)
#     else:
#         odd.append(sum)

# result = even + odd
# print(result)



" Q.3 Write a function to sum of all digits number for the user given the number and do not using for the loop  "
"this question are soluve for the recursion by me "
# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return (n%10) + sum(n//10)


# num = int(input("Enter a number: "))
# print("Sum :", sum(num))



" Q.2 write a function for the longest string without repeting element's"
# data = 'abcdhegdgkehdkfb'
# new=[]
# a=''
# a=a+data[0]
# for i in range(1,len(data)):
#     for j in range(i,len(data)):
#         if ord(data[i])+1 != ord(data[j]):


n=123
if n!=0:
    print((n%10) + sum(n//10))

else:
    print("0")