#Write a Python program to swap cases or toggle cases of a given string.

str=input("Enter a string")
for i in range(len(str)):
    if(str[i].islower()):
        print(str[i].upper(),end="")
    else:
        print(str[i].lower(),end="")