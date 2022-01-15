"""
@author VRAJ PATEL (20CE111)
"""
#Write a Python script to concatenate following dictionaries to create a new one.
print('Q5) Write a Python script to concatenate following dictionaries to create a new one.'.title())
print('now implementing the following Question ...'.title(),'\n')
dic1={'V':8, 'R':88}
print('The dictionary 1 is : '.title(),dic1)
dic2={'A':888, 'J':8888}
print('the dictionary 2 is : '.title(),dic2)
dic3={'I':88888,'H':888888}
print('the dictionary 3 is : '.title(),dic3)
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)#this will add all the elements from all the dictionaries to empty dictionary dict4
print('the dictionary 4 after concatenating all the above three dictionaries is : '.title(),dic4)