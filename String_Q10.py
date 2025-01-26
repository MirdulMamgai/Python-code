#Python program to count Occurrence Of Vowels & Consonants in a String.
str=input("Enter a string:")
countv=0
countc=0
for i in range(len(str)):
    if(str[i]=="A" or str[i]=="E" or str[i]=="I" or str[i]=="O" or str[i]=="U" or str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u"):
        countv=countv+1
    elif(str[i]==" "):
        pass
    else:
        countc=countc+1
print(countv)
print(countc)
        