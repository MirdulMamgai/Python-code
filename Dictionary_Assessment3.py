# Write a Python program to create a dictionary from a string.
# Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


str='w3resource'
l1=list(str)
print(l1)
dir={}
for i in l1:
    if i in dir:
        dir[i]+=1
    else:
        dir[i]=1
print(dir)