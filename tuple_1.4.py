"""
@author VRAJ PATEL (20CE111)
"""
#Write a Python program to convert a tuple to a string.
print('Q4) Write a Python program to convert a tuple to a string.'.title())
print('now implementing the following Question ...'.title(),'\n')
def ConvertTupleToString(tup):#this is a function which will convert tuple into string it will take tuple as argument
    str = ''#this is a null string
    for item in tup:
        str = str + item#we are ititrating tuple one by one and then adding it to the null string declared at beginning
    return str
tuple = ('V', 'R', 'A', 'J')
print('this is the tuple that we are going to convert into string : '.title(),tuple)
str = ConvertTupleToString(tuple)
print('After converting the tuple into string the string is : '.title(),str)