#1. WAP to remove to find duplicates elements in list,
list1=[10,20,30,40,50,10,20,30]
list2=[]
for j in list1:
  if list1.count(j)>=2 and j not in list2:
      print(j)
      list2.append(j)
      
      
        
