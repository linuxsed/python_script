for i in range(1, 10):
    for j in range(1, i+1):
       print('{0}x{1}={2}\t'.format(i, j, i*j),end='') #end不是换行
    print() 
