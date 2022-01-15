"""
@author VRAJ PATEL (20CE111)
"""
# Write a Python script to merge two Python dictionaries.
print('Q2) Write a Python script to merge two Python dictionaries.'.title())
print('now implementing the following Question ...'.title(),'\n')
dict1 = {'V': 88, 'R': 888,'A':8888,'J':88888}
dict2 = {'P': 4, 'A': 44,'T':444,'E':4444,'L':44444}
dict3={}
print('The First Dictionary is : '.title(),dict1)
print('The Second Dictionary is : '.title(),dict2)
dict3.update(dict1)#this will add dict1 to empty dict3
dict3.update(dict2)#this will add dict2 to dict3
print('The Dictionary After Merging Both First and Second dictionaries is : '.title(),dict3)

