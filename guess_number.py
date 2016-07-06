count = 0
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
            continue
