"""
@author VRAJ PATEL (20CE111)
"""
# Write a Python script to check whether a given key already exists in a dictionary.
print('Q1) Write a Python script to check whether a given key already exists in a dictionary.'.title())
print('now implementing the following Question ...'.title(),'\n')
def KeyPresentOrNot(dict, key):#This is a function which checks if the given key is present in the dictionary or not it takes the key and dictionary as arguments
    if key in dict.keys():#This line will check if the given key is present in the dictionary if it is present it will return true
        print('the given key'.title(),key,"already exists in the given dictionary".title())
        print()
    else:
        print('the given key'.title(),key,"does not exist in the given dictionary".title())
        print()
dict = {'V': 88, 'R': 888, 'A': 8888,'J':88888}
print('the given dictionary is '.title(),dict)
print()
key = 'V'
print('now checking if the key '.title(),key,'already exists in the above dictionary or not'.title())
KeyPresentOrNot(dict, key)#Calling the function created above
key = 'I'
print('now checking if the key '.title(),key,'already exists in the above dictionary or not'.title())
KeyPresentOrNot(dict, key)#Calling the function created above
