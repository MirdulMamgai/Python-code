#Python Program to count occurrence of a given characters in string.

n1=input("Enter a string:")
n=n1.lower()
find=input("Enter the character for which your are checking occurance:")
count=0
for i in range(len(n)):
    if(find==n[i]):
        count=count+1
    else:
        continue
print(count)