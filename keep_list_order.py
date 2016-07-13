a= [1, 2, 1, 3, 2, 5]
new_list=[]
for i in a:
    if a.count(i) == 1:
       new_list.append(i)
print (new_list)
