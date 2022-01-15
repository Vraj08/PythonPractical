"""
@author VRAJ PATEL (20CE111)
"""
#Write a Python program to create an intersection, Union, difference of sets.
print('Q3) Write a Python program to create an intersection, Union, difference of sets.'.title())
print('now implementing the following Question ...'.title(),'\n')
A = {8, 88, 888, 8888, 88888}
B = {8, 88, 444, 4444, 44444}
print('This is the set a '.title(),A,'\nThis is the set b '.title(),B,'\n')
print("Union of A and B is :".title(), A | B)# this operator | will given union of two sets
print("Intersection of A and B is :".title(), A & B)# this operator & will given union of two sets
print("Difference of A and B is :".title(), A - B,'\n\n')# this operator - will given union of two sets
