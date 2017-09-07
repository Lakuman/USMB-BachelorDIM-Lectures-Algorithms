# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

"""
## @author : Adrien Roussel, LISTIC Lab, IUT Annecy le vieux
# @brief : a set of generic function for data management

# a variable
a=1 # default type : int

# an empty list
mylist = []

# a fileled list 

mylist2=[1,2,3]

#append to a list
mylist.append(10)

# a buggy list
mybuggylist=[1, 'a', "Hi"]

# operators

b=a+2
mylist_sum=mylist + mylist2
"""


def average_above_zero(input_list):
        
    #init critical variable
    positive_values_sum = 0
    positive_values_counter = 0
        
    #compute the average of positive elements of a list
    
    for item in input_list:
        if item > 0:
            positive_values_sum +=item
            positive_values_counter+=1
        elif item==0:
            print('This value is null '+str(item))
        else:
            print('This value is negative '+str(item))
            
    #compute the final average
    average = float(positive_values_sum)/float(positive_values_counter)
    print('positive elements average is '+str(average))
    return float(average)
    
#the input list
mylist=[1,2,3,4,-7]
result = average_above_zero(mylist)
message = 'The average of positiv sample of (list_values) is (res)'.format(list_values=mylist, res=result)
print(message)

