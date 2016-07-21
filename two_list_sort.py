a=[1,3,5,7,8,9]
b=[2,4,6,8,10]
c=[]
for x in a:
    while len(b) >0:
        if x > b[0]:
            c.append(b.pop(0))
        else:
            c.append(x)
            break
    if len(b) <=0:
        c.append(x)
c.extend(b)
print (c)
