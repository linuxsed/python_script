zone = {
    '江苏' : {
        '苏州' : ['沧浪','相城','平江','吴中','昆山'],
        '南京' : ['白下','秦淮','浦口','栖霞','江宁'],
        '无锡' : ['崇安','南长','北塘','锡山','江阴']
    },
    '安徽' : {
        '合肥' : ['蜀山','庐阳','包河','经开','新站'],
        '芜湖' : ['镜湖','鸠江','无为','三山','南陵'],
        '蚌埠' : ['蚌山','龙子湖','淮上','怀远','固镇']
    }
}
while True:  
    print('省'.center(50,'#'))
    zone_list = list(zone.keys())
    for i in zone_list:
        print (zone_list.index(i)+1,i)
    id = input("请输入省编号,或输入q(quit)退出：")
    if id.isdigit():
        first_id = int(id)
        pro_name = zone_list[first_id-1]
        city_name = list(zone[pro_name].keys())
        while True:
            print ('市'.center(50,'#'))
            for i in city_name:
                print (city_name.index(i)+1,i)
            city_id =input("请输入市编号,或输入b(back)返回上级菜单，或输入q(quit)退出：")
            if city_id.isdigit():
                second_id = int(id)
                city_list = city_name[second_id-1]
                town_list = zone[pro_name][city_list]
                while True:
                    print ('县'.center(50,'#'))
                    for i in town_list:
                        print (town_list.index(i)+1,i)
                    id = input("输入b(back)返回上级菜单，或输入q(quit)退出：") 
                    if id == 'b' or id == 'back':
                        break
                    elif id == 'q' or id =='quit':
                        print ('quit11111')
                        exit()
                    else:
                        print ('你输入{0}不合法，请重新输入'.format(id))
            elif city_id == 'q' or city_id == 'quit':
                print ('quit')
                exit()
            elif city_id == 'b' or city_id =='back':
                break
            else:
                print ('你输入{0}不合法，请重新输入'.format(city_id))
    elif id == 'q' or id == 'quit':
        break
    else:
        print('你输入不合法，请重新输入')
