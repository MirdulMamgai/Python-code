# Write a Python program to print all unique values in a dictionary.
# Original List: [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII':
# 'S005'}, {'V': 'S009'},
# Unique Values: {'S009', 'S002', 'S007', 'S005', 'S001'}
List= [{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII':
'S005'}, {'V': 'S009'},{'VIII': 'S007'}]
d1=set()
for i in List:
    for j in i.values():
        d1.add(j)
print(d1)


