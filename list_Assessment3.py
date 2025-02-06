# WAP to create a list such that new list contains alternate even and odd from given list
list1=[1,2,3,4,5,6]
even=[]
odd=[]
list2=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
i=0
j=0
while i<len(even) and j<len(odd):
    list2.append(even[i])
    list2.append(odd[j])
    i+=1
    j+=1
print(list2)