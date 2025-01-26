#Take a string from user & find the count of vowel in the given string

str=input("Enter a string:")
count=0
for i in range(len(str)):
    if(str[i]=="A" or str[i]=="E" or str[i]=="I" or str[i]=="O" or str[i]=="U" or str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u"):
        count=count+1
print(count)