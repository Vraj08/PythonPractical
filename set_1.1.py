"""
@author VRAJ PATEL (20CE111)
"""
#Write a Python program to add member(s) in a set and clear a set.
print('Q1) Write a Python program to add member(s) in a set and clear a set.'.title())
print('now implementing the following Question ...'.title(),'\n')
set = {'VRAJ'}
print('this is the original set in which we are going to add elements : '.title(),set)
set.add("Patel")#This will add only a single element to set
print("\nNow after adding a single element 'Patel' the set now is : ".title(),set)
set.update(["V...", "P..."])#this will add the elements of list as element in the set
print("Now after adding a multiple elements 'V...','P...' the set now is : ".title(),set)
set.clear()#this will clear the set
print("Now after clearing the set now the set is : ".title(),set)
