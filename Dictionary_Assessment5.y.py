# Combine two dictionary adding values for common keys
# Input: dict1 = {'a': 12, 'for': 25, 'c': 9}
# dict2 = {'python': 100, 'java': 200, 'for': 300}
# Output: {'for': 325, 'python': 100, 'java': 200}

d1={'a':12,'for':25,'c':9}
d2={'python': 100, 'java': 200, 'for': 300}
result={}
for i,j in d2.items():
    result[i]=j
for i,j in d1.items():
    if i in result:
        result[i]+=j
print(result)
