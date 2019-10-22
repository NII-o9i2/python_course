
# chapter7   user input and while
print('******   chapter7    ******')

mess = input('please input something')
print(mess)

age = int(input('please input your age'))
if age > 18:
    print('you have been a adult')
else:
    print('you are still a child')

# while circulation
count = 1
while count <= 5:
    print(count)
    count += 1

password = '123456'
currentinput = input('Please input your password')
while currentinput != password:
    print('wrong!')
    currentinput = input(' Please input again')

inputcount = 0
currentinput = input('Please input password')
while currentinput != password:
    if currentinput[-1] == '#':
        currentinput = input('Please input again')
        continue
    inputcount += 1
    print(inputcount)
    if inputcount > 3:
        print('you have no chance')
        break
    currentinput = input('Please input again')

matename = ['Allen.wang', 'zed.zhang', 'connie.li', 'lily.lab']
invited_name = []
uninvited_name = matename[:]
while uninvited_name != []:
    invited_name.append(uninvited_name.pop())
    print('we have invited ' + invited_name[-1])


wedding_list = {}
peo_count = 0
while peo_count < 5:
    name = input('what is your name?')
    if name in wedding_list.keys():
        print('you have registered')
    else:
        record = {}
        money = input('Please input your cash gift sum')
        record['cash'] = int(money)
        time = input('please input what time will u arrive')
        record['time'] = time
        single_flag = input('please input if you are a single man (y/n)')
        if single_flag == 'y':
            record['single_flag'] = 'yes'
        else:
            record['single_flag'] = 'no'
        wedding_list[name] = record
    reinput_flag = input('if input continue or not?(y/n)')
    if reinput_flag == 'y':
        peo_count += 1
        continue
    else:
        break
print(wedding_list)
