'''Version1.1.0'''
a= [1, 2, 1, 3, 2, 5]
new_list=[]
for i in a:
    if a.count(i) == 1:
       new_list.append(i)
print (new_list)
'''Version1.1.1'''
a= [1, 2, 1, 3, 2, 5]
new_list=[]
for i in a:
    if i not in new_list:
       new_list.append(i)
    else:
       new_list.remove(i)
print (new_list)
