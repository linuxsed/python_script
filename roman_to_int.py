def ramon_to_int(src):
    convert_map = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    
    roman = src.upper()[::-1]
    prev = 0
    lst = []
    for x in roman:
        i = convert_map[x]
        if i < prev:
            lst.append(-1*i)
        else:
            lst.append(i)
        prev = i
    return sum(lst)
print (ramon_to_int('MCMLXXXVII'))
