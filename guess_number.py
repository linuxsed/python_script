'''Version1.0版本'''
'''count = 0
number = 4
while count < 3:
    new_number=input("please you input you number:")
    str_to_number=int(new_number)
    if str_to_number == number:
            print ('you guess number is right ---number is {0}'.format (str_to_number))
            break
    elif str_to_number > number:
            print ('you guess number is too big')
            count +=1
            continue                   
    elif str_to_number <   number:
            print ('you guess number is too small')
            count +=1
            continue'''

'''Version1.1版本'''
number = 4
count = 0
while count < 3:
     new_number=int(input('Please you input you number:'))
     if new_number == number:
        print ('you guess number is right ---number is {0}'.format (new_number))
        break
     elif new_number < number:
        print ('you guess number is too small')
     else:
        print ('you guess number is too big')
     count +=1
else:
     print ('you fail')


''' 使用for循环'''
number = 4 
for _ in range(0,3):
     new_number=int(input('Please you input you number:'))
     if new_number == number:
        print ('you guess number is right ---number is {0}'.format (new_number))
        break
     elif new_number < number:
        print ('you guess number is too small')
     else:
        print ('you guess number is too big')
else:
     print ('you fail')
