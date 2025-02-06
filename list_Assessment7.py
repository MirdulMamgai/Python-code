#7. Write a Python program to find the list of words that are longer than given words
list=["anu","shayam","ramaa"]
min=4
for i in list:
    if(len(i)>min):
        print(i)
