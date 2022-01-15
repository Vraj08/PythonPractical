"""
@author VRAJ PATEL (20CE111)
"""
#Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
#most common from list
def commonelementfinder(list):#this is a function which will take list/tuple as argument and then it will convert them to set and return  the most common element in them
    return max(set(list), key = list.count)#i have used this function to find common element and count function to count the frequency of the common element
print('Q5) Write a Python program to find the most common elements and their counts from list, tuple, dictionary.'.title())
print('now implementing the following Question ...'.title(),'\n')
LIST = [8, 4, 8, 4, 44, 88,8,8,888,444,444,8888,8,4,8,8,4]
a=commonelementfinder(LIST)
print('This is the list from which we are going to find most common element and its count : '.title(),LIST,'\nThe most common element from the above list is : '.title(),a,'and it occurs '.title(),LIST.count(a),'times in the list'.title(),'\n')
#most common from tuple
TUP = (888, 4, 88, 4, 4,4,4,8,888,444,444,8888,8,4,4,8,4)
a=commonelementfinder(TUP)
print('This is the tuple from which we are going to find most common element and its count : '.title(),TUP,'\nThe most common element from the above tuple is : '.title(),a,'and it occurs '.title(),TUP.count(a),'times in the Tuple'.title(),'\n')
#most common from dictionary
DICT={1:88,2:22,3:33,4:88,5:88,6:44,7:34,8:88}
LiST=list(DICT.values())
a=commonelementfinder(LiST)
print('This is the Dictionary from which we are going to find most common element and its count : '.title(),DICT,'\nThe most common element from the above dictionary is : '.title(),a,'and it occurs '.title(),LiST.count(a),'times in the Dictonary'.title())
