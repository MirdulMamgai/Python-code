#6. Write a Python program to remove duplicates from a list.

list1=[10,20,10,30,40,30,10]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
        print(i)