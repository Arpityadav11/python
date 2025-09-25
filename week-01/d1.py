def printHollowNum(n):
    a=1
    for i in range(n):
        for j in range(i+1):
            if j==0 or i==j or i==n-1:
                print(a,end=' ')
            else:
                print(' ',end=' ')
            a+=1
        print()

# printHollowNum(4)

def printFab(n):
    a = 0
    b = 1
    for i in range(n):
        for j in range(i+1):
            c=a+b
            print(a,end=' ')
            a = b
            b = c
        print()

# printFab(4)

# li = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# sr = 0
# edr = 3 
# sc = 0
# edc = 3
# while sr<edr and sc<edc :
#     #left to right
#     for i in range(sr,edc):
#         print(li[sr][i],end=' ')
#     #top to bottom
#     for j in range(sr+1,edr):
#         print(li[j][edc],end=' ')
#     #right to left
#     for k in range(edc,sc,-1):
#         print(li[edr][k],end=' ')
#     #bottom to top
#     for l in range(edr,sc,-1):
#         print(li[l][sc],end=' ')
#     sr +=1
#     edr -=1
#     sc +=1
#     edc -=1

# data = [12,[1,2,3]]
# for i in data[1]:
#     print(i)

#reverse the sentance
# data = "hemant is a very good boy"
# end = len(data)
# for i in range(len(data)-1,-1,-1):
#     if data[i] ==' ':
#         print(data[i+1:end],end=' ')
#         end=i
#     elif i==0:
#         print(data[i:end])

