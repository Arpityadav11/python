# Q1. Print a solid square of stars (n=5).
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(n):
#         print("*",end=' ')
#     print()

# Q2. Print a right-angled triangle of stars (n=5).
# *
# * *
# * * *
# * * * *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=' ')
#     print()

# Q3. Print an inverted right-angled triangle of stars (n=5).
# * * * * *
# * * * *
# * * *
# * *
# *

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=' ')
#     print()

# Q4. Print a left-angled triangle of stars (n=5).
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# Q5. Print an inverted left-angled triangle of stars (n=5).

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(end=' ')
#     for j in range(n-i):
#         print("*",end=' ')
#     print()

# Q6. Print a hollow square (n=5).
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or j ==0 or i == n-1 or j == n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# Q7. Print a hollow right-angled triangle (n=5).
# *
# * *
# *   *
# *     *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(i+1):
#         if j == 0 or i ==n-1 or i== j:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# Q8. Print a hollow inverted right-angled triangle (n=5).
# * * * * *
# *     *
# *   *
# * *
# *

# n = 5
# for i in range(n):
#     for j in range(n-i):
#         if j==0 or j==n-i-1 or i==0:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# Q9. Print a pyramid of stars (n=5).
#     * 
#    * *
#   * * *
#  * * * *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# Q10. Print an inverted left-angled triangle of stars (n=5).

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(end=' ')
#     for j in range(n-i):
#         print("*",end=' ')
#     print()

# Q11. Print a diamond star pattern (n=5).

#     * 
#    * * 
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n = 5 

# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(i):
#         print("* ", end="")
#     print()

# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(i):
#         print("* ", end="")
#     print()

# Q14. Print a half-diamond pattern (n=5).
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# n = 5
# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# Q15. Print a number right-angled triangle (n=5).
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# Q16. Print a Floyd’s triangle (n=5).
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# n=5
# count = 1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(count,end=' ')
#         count+=1
#     print()


# Q17. Print a 0–1 triangle (n=5).
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

# n=5
# for i in range(n):
#     count = 1
#     for j in range(i+1):
#         print(count,end=' ')
#         if count == 0:
#             count+=1
#         elif count==1:
#             count -=1
#     print()

# Q18. Print a Pascal’s triangle (n=5).
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

# another formula for pascal is that a=1
# a = a*(i-j)//(j+1)

# def factorial(n):
#     fact = 1
#     while n > 0:
#         fact *= n
#         n-=1
#     return fact

# n = 5
# for i in range(n):
#     for j in range(n-i-1):
#         print(end=' ')
#     for j in range(i+1):
#         ncr = factorial(i)//(factorial(k)*factorial(i-k))
#         print(ncr,end=' ')
#     print()


# n = 5
# for i in range(n):
#     for j in range(n-i-1):
#        print(end=' ')
#     a=1
#     for j in range(i+1):
#        print(a,end=' ')
#        a = a*(i-j)//(j+1)
#     print()

# Q19. Print a 0–1 triangle (n=5).
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

# n=5
# for i in range(n):
#     count = 1
#     for j in range(i+1):
#         print(count,end=' ')
#         if count == 0:
#             count+=1
#         elif count==1:
#             count -=1
#     print()

# Q20. Print a continuous number triangle (n=5).
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# n=5
# count = 1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(count,end=' ')
#         count+=1
#     print()

# Q21. Print a right-angled triangle with same number in row (n=5).
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=' ')
#     print()

# Q22. Print a star hill pattern (n=5).
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(end=' ')
#     for k in range(i+1):
#         print("*",end=' ')
#     print()

# Q23. Print alphabet C pattern (n=6)

#  ****
# *
# *
# *
# *
#  ****

# n=6
# for i in range(1,n+1):
#     for j in range(n-1):
#         if i==1 and j == 0 or i == n and j == 0:
#             print(' ',end=' ')
#         elif i==1 or j == 0 or i==n:
#             print("*",end=' ')
#     print()

# Q12. Print a hollow pyramid (n=5).

#     *
#    * *
#   *   *
#  *     *
# * * * * *

# n = 5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(end=' ')
#     for k in range(i):
#         if k==0 or k== i-1 or i==n:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# Q24. Print an X pattern (n=5). 
 
 
# *       * 
#   *   * 
#     * 
#   *   * 
# *       * 

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j == n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# Q25. Print a plus sign pattern (n=5). 
 
 
#   * 
#   * 
# ***** 
#   * 
#   * 

# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == n//2 or j==n//2:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# Q26. Print a hollow diamond inside square (n=7). 
 
 
# ******* 
# **   ** 
# * * * * 
# *  *  * 
# * * * * 
# **   ** 
# ******* 

# n = 7
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i ==n-1 or j==n-1 or i == j or i+j==n-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# Q27. Print a zigzag pattern (n=9). 
 
 
#     *       * 
#   *   *   *   * 
# *       *       * 

# n = 9
# for i in range(n//3):
#     for j in range(n):
#         if i+j==2 or i+j==6 or j-i == 2 or j-i ==6:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# Q28. Print a snake number pattern (n=5). 
 
# li =  [[1, 2, 3, 4, 5], 
#  [10, 9, 8, 7, 6 ],
#  [11, 12, 13, 14, 15], 
#  [20, 19, 18, 17, 16], 
#  [21, 22, 23, 24, 25 ]]

# n=5
# for i in range(n):
#     if i%2 ==0:
#         for j in range(n):
#             print(li[i][j],end=' ')
#     else:
#         for j in range(n-1,-1,-1):
#             print(li[i][j],end=' ')

#  ADVANCE PATTERN PROBLEM 
# 1. Print a hollow diamond pattern of stars (n=5). 
#      * 
#     * * 
#    *   * 
#   *     * 
#  *       * 
#   *     * 
#    *   * 
#     * * 
#      * 

# n = 5
# for i in range(n):
#     for j in range(2*n-1):
#         if i+j==4 or j-i==4:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()
# for i in range(n,2*n-1):
#     for j in range(2*n-2):
#         if i-j == 4 or i+j== 12:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

# 2. Pascal's Triangle (n=5). 
#     1 
#    1 1 
#   1 2 1 
#  1 3 3 1 
# 1 4 6 4 1

# def factorial(n):
#     fact = 1
#     while n > 0:
#         fact *= n
#         n-=1
#     return fact

# n = 5 
# for i in range(n):
#     for j in range(n-i):
#         print(end=' ')
#     for k in range(i+1):
#         ncr = factorial(i)//(factorial(k)*factorial(i-k))
#         print(ncr,end=' ')
#     print()

# 3. Floyd's Triangle reverse aligned (n=5). 
# 15 14 13 12 11 
# 10 9 8 7 
# 6 5 4 
# 3 2 
# 1 

# count = 15
# n = 5
# for i in range(n-1,-1,-1):
#     for j in range(i+1):
#         print(count,end=' ')
#         count-=1
#     print()

# 4. Butterfly pattern (n=5).

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     for j in range(1,2*(n-i)+1):
#         print(' ',end='')
#     for j in range(1,i+1):
#         print('*',end='')
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         print('*',end='')
#     for j in range(1,2*(n-i)+1):
#         print(' ',end='')
#     for j in range(1,i+1):
#         print('*',end='')
#     print()
        
# 5. Print a zigzag pattern (n=9). 
 
 
#     *       * 
#    * *     * * 
#   *   *   *   * 
#  *     * *     * 
# *       *       *

# rows = 5
# columns = 17
# for i in range(rows):
#     for j in range(columns):
#         if i+j==columns-rows or i+j == rows-1 or j-i==rows-1 or j-i == columns- rows:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# 6. Numeric pyramid increasing left to right (n=5). 
#     1 
#    2 3 
#   4 5 6 
#  7 8 9 10 
# 11 12 13 14 15 

# count = 1
# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print(end=' ')
#     for j in range(i+1):
#         print(count,end=' ')
#         count += 1
#     print()

# 7. Cross-diagonal rectangle pattern (n=5). 
# * * * * * 
# * *   * * 
# *   *   * 
# * *   * * 
# * * * * *

# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j== n or i==j or i+j==n+1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# 8. Hollow pyramid numbers (n=5). 
#     1 
#    2 2 
#   3   3 
#  4     4 
# 5 5 5 5 5 

# n =5
# for i in range(n):
#     for j in range(2*(n-1)):
#         if  i==n-1 and j<n:
#             print(i+1,end=' ')
#         elif i+j == n-1 or j-i == n-1:
#             print(i+1,end='')
#         else:
#             print(end=' ')
#     print()

# 9. Diamond with numbers increasing from center (n=5). 
#     1 
#    2 2 
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5
#  4 4 4 4
#   3 3 3
#    2 2
#     1

# n = 5 
# num = 1 
# for i in range(1, n+1): 
#     for j in range(n-i): 
#         print(end=" ") 
#     for k in range(i): 
#         print(num, end=" ") 
#     print() 
#     num+=1 
# num-=2 
# for i in range(1,n): 
#     for j in range(i): 
#         print(end=" ") 
#     for k in range(n-i): 
#         print(num, end=" ") 
#     num-=1 
#     print() 

# 10. Sandglass star pattern (n=5). 
# ********* 
#  ******* 
#   ***** 
#    *** 
#     * 
#    *** 
#   ***** 
#  ******* 
# *********

# n =5 
# for i in range(n):
#     for j in range(1,i+1):
#         print(' ',end='')
#     for j in range(2*(n-i)-1):
#         print('*',end='')
#     print()
# for i in range(n-2,0,-1):
#     for j in range(1,i+1):
#         print(' ',end='')
#     for j in range(2*(n-i)-1):
#         print('*',end='')
#     print()

# 11. Spiral matrix clockwise (n=4). 
# matrix = [ 
#     [1, 2, 3, 4], 
#     [12, 13, 14, 5], 
#     [11, 16,15,6], 
#     [10,9,8,7] 
# ] 

# m,n = 4,4 
# layers = max(m,n)//2
# for i in range(layers):
#     left,right = i,n-i-1
#     top,bottom = i,m-i-1
#     # l->r
#     for j in range(left,right+1):
#         print(matrix[left][j],end=' ')
#     # t->b
#     for j in range(top+1,bottom+1):
#         print(matrix[j][right],end=' ')
#     # r->l
#     for j in range(right-1,left-1,-1):
#         print(matrix[bottom][j],end=' ')
#     # b->t
#     for j in range(bottom-1,top,-1):
#         print(matrix[j][left],end=' ')

# 12. Checkerboard 1/0 (n=6). 
# 1 0 1 0 1 0 
# 0 1 0 1 0 1 
# 1 0 1 0 1 0 
# 0 1 0 1 0 1 
# 1 0 1 0 1 0 
# 0 1 0 1 0 1 
# count = 1
# n = 6
# for i in range(n):
#     for j in range(n):
#         print(count,end=' ')
#         if count == 1 and j!=n-1:
#             count -= 1
#         elif j!=n-1:
#             count += 1
#     print()

# 13. Odd rows stars, even rows numbers (n=5). 
# * * * * * 
# 1 2 3 4 5 
# * * * * * 
# 1 2 3 4 5 
# * * * * * 
# n = 5
# for i in range(n):
#     for j in range(1,n+1):
#         if i%2==0:
#             print('*',end=' ')
#         else:
#             print(j,end=' ')
#     print()

# 14. Pyramid of Fibonacci numbers (n=5). 
#     0 
#    1 1 
#   2 3 5 
#  8 13 21 34 
# 55 89 144 233 377
# n = 5
# a,b = 0, 1
# for i in range(n):
#     for j in range(n-i):
#         print(end=' ')
#     for j in range(i+1):
#         print(a,end=' ')
#         c = a+b
#         a = b
#         b = c
#     print()

# 15.Hollow square with diagonals (n=5). 
# * * * * * 
# * *   * * 
# *   *   * 
# * *   * * 
# * * * * *

# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j== n or i==j or i+j==n+1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# 17. Sandglass star pattern (n=5). 
# ********* 
#  ******* 
#   ***** 
#    *** 
#     * 
#    *** 
#   ***** 
#  ******* 
# *********

# n =5 
# for i in range(n):
#     for j in range(1,i+1):
#         print(' ',end='')
#     for j in range(2*(n-i)-1):
#         print('*',end='')
#     print()
# for i in range(n-2,0,-1):
#     for j in range(1,i+1):
#         print(' ',end='')
#     for j in range(2*(n-i)-1):
#         print('*',end='')
#     print()

# Q.8. Rhombus with numbers (n=5).  
#     11111 
#    22222 
#   33333 
#  44444 
# 55555 

# n = 5
 
# for i in range(1,n+1): 
#     for j in range(n-i): 
#         print(end=" ") 
#     for k in range(n): 
#         print(i,end="") 
#     print() 

# 19. Wave-like star pattern (rows=4, 
# cols=9).   

# 1 2 3 4 5 
# 10 9 8 7 6 
# 11 12 13 14 15 
# 20 19 18 17 16 
# 21 22 23 24 25 
# n = int(input("Enter the input: ")) 
# num = 1 
# for i in range(1,n+1): 
#     if i%2==0: 
#         num += n-1 
#         for j in range(n): 
#             print(num, end=" ") 
#             num-=1 
#         print() 
#         num += n+1 
#     else: 
#         for j in range(n): 
#             print(num, end=" ") 
#             num+=1 
#         print()

# 20. Numeric diamond repeating numbers (n=5).  
#     1 
#    2 2 
#   3 3 3 
#  4 4 4 4 
# 5 5 5 5 5 
#  4 4 4 4 
#   3 3 3 
#    2 2 
#     1 
 
# n = 5
# num = 1 
# for i in range(1, n+1): 
#     for j in range(n-i): 
#         print(end=" ") 
#     for k in range(i): 
#         print(num, end=" ") 
#     print() 
#     num+=1 
# num-=2 
# for i in range(1,n): 
#     for j in range(i): 
#         print(end=" ") 
#     for k in range(n-i): 
#         print(num, end=" ") 
#     num-=1 
#     print() 

# 21. Alphabet pyramid (n=5).  
#     A 
#    B B 
#   C C C 
#  D D D D 
# E E E E E 
 
# val = 65 
# n = 5
# for i in range(n): 
#     for k in range(n-i): 
#         print(end=" ") 
#     for j in range(i+1): 
#         print(chr(val), end=" ") 
#     val+=1 
#     print() 

# 23. Hollow inverted pyramid of stars (n=5).  
# n = 5 
#  * * * * * 
#   *     * 
#    *   * 
#     * * 
#      * 
 
# n = 5 
# for i in range(n): 
#     for j in range(i+1): 
#         print(end=" ") 
#     for j in range(n-i): 
#         if j==0 or j==n-i-1 or i==0: 
#             print("*", end=" ") 
#         else: 
#             print(" ", end=" ") 
#     print() 

# 25. Right-aligned triangle with squares (n=5).  
#     1 
#    4 9 
#   16 25 36 
#  49 64 81 100 
# 121 144 169 196 225 

# n = 5
# num = 1 
 
# for i in range(1,n+1): 
#     for j in range(n-i): 
#         print(end=" ") 
#     for j in range(i): 
#         print(num*num, end=" ") 
#         num+=1 
#     print() 


# 29. Arrow pointing upwards (n=5).  
#    * 
#   *** 
#  ***** 
#    * 
#    * 
#    * 
#    * 
#    * 

# n = 5
# mid = n // 2

# for i in range(mid + 1):
#     for j in range(mid - i):
#         print(" ", end="")
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print()

# for i in range(n):
#     for j in range(mid):
#         print(" ", end="")
#     print("*")

# 30. Hollow diamond with numbers at boundary (n=5).  
#     1 
#    2 2 
#   3   3 
#  4     4 
# 5       5 
#  4     4 
#   3   3 
#    2 2 
#     1 

# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print(i, end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(n - 1, 0, -1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(1, 2 * i):
#         if j == 1 or j == 2 * i - 1:
#             print(i, end="")
#         else:
#             print(" ", end="")
#     print()

# Q29. Print a wave pattern (n=6). 
 
 
# *     *     * 
#  *   * *   * 
#   * *   * * 
#    *     *

# rows = int(input("enter the number of rows: "))
# col = 4*(rows-1)+1

# for i in range(rows):
#     for j in range(col):
#         if i==j or i+j == col//2 or j-i == col//2 or i+j == col-1:
#             print('*',end='')
#         else:
#             print(end=' ')
#     print()

# 16. Concentric square numbers (n=4). 
# 4 4 4 4 4 4 4 
# 4 3 3 3 3 3 4 
# 4 3 2 2 2 3 4 
# 4 3 2 1 2 3 4 
# 4 3 2 2 2 3 4 
# 4 3 3 3 3 3 4 
# 4 4 4 4 4 4 4

# n = 4
# for i in range(2*n-1):
#     for j in range(2*n-1):
#         if i==0 or j ==0 or i == 2*n-2 or j == 2*n-2:
#             print(n,end=' ')
#         elif i==1 or j==1 or i==2*n-3 or j==2*n-3:
#             print(n-1,end=' ')
#         elif i==2 or j==2 or i==2*n-4 or j==2*n-4:
#             print(n-2,end=' ')
#         elif i==3 or j==3 or i==2*n-5 or j==2*n-5:
#             print(n-3,end=' ')
#         else:
#             print(' ',end=' ')
#     print()
