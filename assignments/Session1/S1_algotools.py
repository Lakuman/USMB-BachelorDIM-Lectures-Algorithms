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

# SORTING SELECTIVE

# MISSING QUESTIONS 

# sort_selective function declaration
# Function able to sort a list
# @param list_in : the list to be sorted
def sort_selective(list_in):

    for i in xrange(len(list_in) -1):
        minIndex = i
        for j in xrange(i, len(list_in)):
            if list_in[j] < list_in[minIndex]:
                minIndex = j

        if minIndex != i:
            tempValue = list_in[i]
            list_in[i] = list_in[minIndex]
            list_in[minIndex] = tempValue

    return list_in

# Initialize variable
myList = [10, 15, 7, 1, 3, 3, 9]

# Display message before method call
print("List before sorting : " + str(myList))

# Call sort_selective method and display message
myList = sort_selective(myList)
print("List after sorting : " + str(myList))



# SORTING BUBBLE

# MISSING QUESTIONS 

# sort_bubble function declaration
# Function able to sort a list
# @param list_in : the list to be sorted
def sort_bubble(list_in):
    
    permutations = True

    while permutations == True:
        permutations = False
        for i in xrange(1, len(list_in)):
            if list_in[i-1] > list_in[i]:
                tempValue = list_in[i]
                list_in[i] = list_in[i-1]
                list_in[i-1] = tempValue
                permutations = True

    return list_in

# Display message before method call
print("list before sorting : " + str(myList))

# Call sort_selective method and display messageb
myList = sort_bubble(myList)
print("list after sorting : " + str(myList))

    
    
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





    



