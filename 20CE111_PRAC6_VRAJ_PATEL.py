"""
@author VRAJ(20CE111)

Repo Link : https://github.com/Vraj08/PythonPractical

AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.

Sample Input
4
bcdef
abcdefg
bcde
bcdef

Sample Output
3
2 1 1

Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each.
The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

"""
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


