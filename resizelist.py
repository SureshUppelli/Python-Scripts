list1 = []
print (list1)
i = 1
while i < 6:
    list1 = list1[:i]
    list1[i] = input ("Enter Value for list : ")
    i = i + 1
print(list1)