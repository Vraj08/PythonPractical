"""
@author VRAJ PATEL (20CE111)
"""
#Write a Python script to add a key to a dictionary.
print('Q4) Write a Python script to add a key to a dictionary.'.title())
print('now implementing the following Question ...'.title(),'\n')
dict = {'V':88, 'R':888,'A':8888}
print('this is the dictionary in which we are going to add a new key'.title(),dict)
dict.update({'J':88888})#This will add/merge this dictionary given in the argumment to the dict
print('the dictionary after adding new key is : '.title(),dict)