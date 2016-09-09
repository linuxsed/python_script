blacklist=[]
while True:
    for _ in range(0,3):
        user = input('Please you input you name:')
        with open('/root/1.txt') as f:
            a=f.readline().strip().split(':')
            if user == a[0]:
                password = input ('Pleas you input you password:')
                if password == a[1]:
                    print ('you login sucess')
                    break
                print ('you input password Error')
            else:
                    if user != a[0]:
                        print ('you input username is error')
    else:
        blacklist.append(user)
        print ('user is lock')
        print (blacklist)
        break
    break
