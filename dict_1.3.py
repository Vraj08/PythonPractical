"""
@author VRAJ PATEL (20CE111)
"""
#Write a Python program to sum all the items in a dictionary.
print('Q3) Write a Python program to sum all the items in a dictionary.'.title())
print('now implementing the following Question ...'.title(),'\n')
dict = {'V': 88, 'R': 888, 'A': 8888,'J':88888}
print('The given dictionary of which we are going to find sum is : '.title(),dict)
values = dict.values()#This command will extract all the values from the dictionary
print("Sum of all items in the above dictionary is :", sum(values))#This line will sum all the values and print them
