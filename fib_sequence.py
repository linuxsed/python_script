#求菲波那切数列
# 1 1 2 3 5 8 13 21 34 55
'''用函数实现'''
def fib1(n):
    stack=[]
    if n == 0 or n == 1:
       return 1
    else:
       stack.append(1)
       stack.append(1)
       for i in range(2,n):
          stack.append(stack[i-1]+stack[i-2])
       return stack
print (fib1(8))


def fib2(n):
    count=0
    a,b =0,1
    while count < n:
      print (b)
      a,b = b,a +b
      count +=1
    return 'done'
print (fib2(5))


'''用yield生成器'''
def fib3(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
for i in fib3(5):
    print (i)

'''用递归实现'''
def fib4(n):
    if n == 0 or n == 1:
       return 1
    return fib4(n-1)+fib4(n-2)
print (fib4(5))
