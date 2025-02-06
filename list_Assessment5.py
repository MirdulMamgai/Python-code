#Write a Python program to count the number of strings where the string length is 2 or more
#and the first and last character are same from a given list of strings.

list1=['a','aa','b','bb','ccb','cbc']

for i in list1:
    if len(i)>=2 and i[0]==i[-1]:
        print(i)