#Python program to remove repeated character from string.

def remove(s):
    s=s.lower()
    new_str = ''
    for i in s:
         if i not in new_str:
            new_str=new_str+i
    return new_str

str=input("Enter a string:")
str1=remove(str)
print(str1)

