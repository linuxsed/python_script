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
'''注：如果有三个重复元素这种方法就不行了下面看Version1.1.2'''
a= [1, 2, 1, 3, 2, 5,1]
ret=[]
temp=[]
for x in a:
    if x not in temp:
       ret.append(x)
       temp.append(x)
    else:
       if x in ret:
          ret.remove(x)
print (ret)
