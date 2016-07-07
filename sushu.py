def sushu(num):                            
    res=True
    for x in range(2,num-1):
        if num %x ==0:
            res=False
        return res
print ([ x for x in range(100) if sushu(x)])
