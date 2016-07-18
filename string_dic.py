a = "aAsmr3idd4bgs7Dlsf9eAF"
a = a.lower() 
print (dict([(x,a.count(x)) for x in set(a)]))
