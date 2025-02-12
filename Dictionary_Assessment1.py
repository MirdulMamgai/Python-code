#Write a Python program to combine two dictionary adding values for
# common keys. Go to the editor
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1={"a":100,
#     "b":200,
#     "c":300}
# d2={"a":300,
#     "b":200,
#     "d":400}
# result={}

# for i,j in d1.items():
#     result[i]=j
# for i,j in d2.items():
#     if i in result:
#         result[i]+=j
#     else:
#         result[i]=j
# print(result)

from collections import Counter
d1={"a":100,
    "b":200,
    "c":300}
d2={"a":300,
    "b":200,
    "d":400}
result=Counter(d1)+Counter(d2)
print(result)
    

