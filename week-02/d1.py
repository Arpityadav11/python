# print(data.capitalize()) capitalizes the first letter of string 
# print(data.find('i'))
# print(data.index('i')) print the index of the first occurance 
# print(data.replace('arpit','iit'))
# print(data.rjust(10))
# print(data.('i'))

# remove the duplicate element
# data = "my college name name is jit jit"
# result = ''
# for i in data.split():
#     if i not in result:
#         result+=i
#         result +=' '
# print(result)

# count the duplicate values 

# data = "my college name name is jit jit"
# result = ''
# for i in data.split():
#     count = data.count(i)
#     if count>1 and i not in result:
#         print(i, count)
#         result += i +' '

# new approach using dictionary
# data = "my college name name is jit jit"
# duplicate = {}
# for i in data.split():
#     c = data.split().count(i)
#     if c >=2:
#         duplicate[i]=c
# print(duplicate)

# chars = ["a"]
# result = ''
# for i in chars:
#     count = chars.count(i)
#     if count>1 and i not in result:
#         result += i +' '
#         for j in str(count):
#             result += j+' '
#     elif count ==1:
#         result += i+' '
# chars = result.split()
# print(chars)