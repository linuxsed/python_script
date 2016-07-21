a = "aAsmr3idd4bgs7Dlsf9eAF"
b=[]
for i in a:
    if i.isdigit():
       b.append(i)

print (''.join(b))

'''使用列表解析式'''
print (''.join([ x for x in a if x.isdigit()]))
