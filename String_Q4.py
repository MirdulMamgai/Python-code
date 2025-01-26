#Python program to check given character is vowel or consonant.

str=input("Enter a character:")
for i in range(len(str)):
    if(str[i]=="A" or str[i]=="E" or str[i]=="I" or str[i]=="O" or str[i]=="U" or str[i]=="a" or str[i]=="e" or str[i]=="i" or str[i]=="o" or str[i]=="u"):
        print("Vovel")
    else:
        print("Consonent")
