tc= int(input())
storing_dict = dict() #Dictionary for storing words and its occurrences as key:value
for i in range(tc):
    word = input()
    if word in storing_dict:# this will check if the word is already present in the dictonary if it is present then it will increment the value by one i.e its occurrence
        storing_dict[word] += 1
    else:# if  the word is not present in dictionary it will add the word and its occurrence as 1
        storing_dict[word] = 1
print(len(storing_dict))#This will print the no of distinct words from the input.
print(' '.join([str(storing_dict[word]) for word in storing_dict]))#This will print the items of dictonary seperated by ' '(space)


