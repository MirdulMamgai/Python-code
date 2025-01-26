#Python program to print all non repeating character in string.

str=input("Enter a string:")
for i in range(len(str)):
    is_repeated = False
    for j in range(len(str)):
        if i != j and str[i] == str[j]:
            is_repeated = True
            break  
    if is_repeated==False:
        print(str[i], end=" ")
      
