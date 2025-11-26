from os import name
import pandas as pd
import numpy as np
from pyparsing import col
data = np.array([1,2,3,4,5])
'''Series'''
# new = pd.Series(data,index=['a','b','c','d','e'],name='age')
# new[['a','b','c']]=10
# print(new)
# new[new>=10] = 0
# print(new)

'''DataFrame'''
# D2 = np.array([["Arpit",50,100],
#                ['Jay',70,100],
#                ['Ajay',80,100]])

# indexes = ['first','second','third']
# col = ['name','marks','total']
# n = pd.DataFrame(D2,indexes,columns=col)
# print(n)
'''homework
access the data from data frame
assigning the values in the data frame
using indexing , fancy indexing, slicing,boolean indexing
'''

'''how to load the CSV file into your panda'''
import pandas as pd 
# data = pd.read_csv('filename.csv')
