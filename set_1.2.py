"""
@author VRAJ PATEL (20CE111)
"""
#Write a Python program to remove an item from a set if it is present in the set.
print('Q2) Write a Python program to remove an item from a set if it is present in the set.'.title())
print('now implementing the following Question ...'.title(),'\n')
set = {'VRAJ','PATEL','V...','P...'}
print('This is the original set in which we are going to remove a element if it is present in the set : '.title(),set,'\n')
print("Now we will remove 'R...' if present in the set ...".title())
set.discard('R...')#this function will remove the element passed in the argument if present in set
print("the set after removing 'R...' if present in the set is : ".title(),set,'\n')
print("Now we will remove 'V...' if present in the set ...".title())
set.discard('V...')
print("the set after removing 'V...' if present in the set is : ".title(),set)
