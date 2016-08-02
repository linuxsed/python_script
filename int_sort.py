def sort(lst,reverse=False):
    dst=[]
    for n in lst:
        for i,e in enumerate(dst):
            if not reverse:
                if n < e:
                    dst.insert(i,n)
                    break
            else:
                if n > e:
                    dst.insert(i,n)
                    break
        else:
            dst.append(n)
    return dst
    
print (sort([3,3,2,1,5,4,4,7,8,6],reverse=True))
