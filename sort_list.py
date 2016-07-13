a=[1,3,5,7,9]
b=[2,4,6,8,10]
new_list=[]
for i in a+b:
    new_list.append(i)
    new_list.sort()
print (new_list)
