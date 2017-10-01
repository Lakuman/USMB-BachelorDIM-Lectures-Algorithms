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
    

def max_value(input_list):

    maxi_value = input_list[0]
    for idx, item in enumerate (input_list):
        if maxi_value < item:
            maxi_value = item
            maxi_idx = idx              
    return maxi_value, maxi_idx

def reverse_table(input_list):
    lastidx = len(input_list)
    for idx in xrange(len(input_list)/2):
        lastidx -=1
        popped = input_list[idx]
        input_list[idx] = input_list[lastidx]
        input_list[lastidx]= popped
    
    
    return input_list


#Removing Whitespace
def remove_whitespace(myoldstring):

    mystring = myoldstring.replace(" ","")
    return mystring;
   
    
    
#the input list
mylist=[1,2,3,4]
result = average_above_zero(mylist)
message = 'The average of positiv sample of {list_values} is {res}'.format(list_values=mylist, res=result)
print(message)

maximum_value = max_value(mylist)
message = 'The maximum value of the list is {max_scan}'.format(max_scan = maximum_value)
print(message)

reversed_list = reverse_table(mylist)
message = 'The reversed list is {listrevers}'.format(listrevers = reversed_list)
print(message)
    
mystring = 'Hello world'
mynewsring = remove_whitespace(mystring)


    



