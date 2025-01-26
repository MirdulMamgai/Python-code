#Python program to count alphabets, digits and special characters.

str=input("Enter a string")
counta=0
countd=0
countsc=0
for i in range(len(str)):
    if str[i].isalpha():
        counta=counta+1
    elif str[i].isdigit():
        countd=countd+1
    else:
        countsc=countsc+1
print(counta)
print(countd)
print(countsc)
    