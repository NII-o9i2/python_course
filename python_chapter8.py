# chapter8  function
from module import function4 as f4
from module1 import function1
import module
from module import function3
print('******   chapter8    ******')


def greet_user():
    print('Hello everyone')


def greet_general(user_name):
    print('Hello ' + user_name)


def clothes_collect(size, color):
    print('size: ' + size + ' ' + 'color: ' + color)

# first argument without default valve, then argument with default value


def clothes_collect_default(color, style, size='l'):
    print('color: ' + color + ' size: ' + size + ' style: ' + style)


greet_user()

#name = input('please input your name')
name = 'NII'
greet_general(name)

# formal parameters & actual parameters
clothes_collect('xl', 'black')
clothes_collect('black', 'xl')
clothes_collect(color='black', size='xl')
clothes_collect_default('white', 'coat')
clothes_collect_default('white', 'coat', 'xl')
clothes_collect_default('white', 'coat')

# 8.3 return pattern


def business_card(name, phone_number, gender, email='', site='china'):
    ans = ''
    ans += name + ' ' + phone_number
    if gender == 'm':
        ans += ' male '
    else:
        ans += ' famale '
    if email != '':
        ans += email + ' ' + site
    else:
        ans += site
    return ans


w = business_card('NII', '123456', 'm')
print(w)
w = business_card('NII', '1456789', 'm', email='159753@gmail.com')
print(w)

# 8.3.3 return dictionary


def business_card_dic(name, phone_number, gender, email='', site='china'):
    ans = {}
    ans['name'] = name
    ans['phone'] = phone_number
    if gender == 'm':
        ans['gender'] = 'male'
    else:
        ans['gender'] = 'famale'
    ans['email'] = email
    ans['site'] = site
    return ans


w_dic = business_card_dic('NII', '1456789', 'm', email='159753@gmail.com')
print(w)

# 8.4 transport list

# 8.4.1 modify list in the function


def process_print(unprocess_list, processed_list):
    while unprocess_list != []:
        handing = unprocess_list.pop()
        processed_list.append(handing)
        print(str(handing) + ' is processing')


pre_list = ['a', 'b', 'c', 'd']
pre_list2 = list(range(1, 10))
w1 = []
w2 = []
process_print(pre_list, w1)
process_print(pre_list2, w2)
print(pre_list)

# 8.4.2 ban modify list in the function

pre_list = ['a', 'b', 'c', 'd']
process_print(pre_list[:], w2)
print(pre_list)

# 8.5.1 any number of arguments


def math_operation(kind, *mathmembers):
    if kind == 1:
        sum1 = 0
        for mathmember in mathmembers:
            sum1 += mathmember
    elif kind == 2:
        sum1 = 1
        for mathmember in mathmembers:
            sum1 = sum1 * mathmember
    return sum1


print(math_operation(1, 5, 6, 5, 4, 7, 7))
print(math_operation(2, 1, 1, 1, 1, 1, 5, 6))

print(w_dic)


def merge(number, record):
    n_record = {}
    n_record['number'] = number
    for v, k in record.items():
        n_record[v] = k
    return n_record


def merge2(number, **record):
    n_record = {}
    n_record['number'] = number
    for v, k in record.items():
        n_record[v] = k
    return n_record


record_dic = merge(2, w_dic)
print(record_dic)

record_dic2 = merge2(2, name='xiaoming', phone='18742241111')
print(record_dic2)

# 8.6 import module and function

module.studing()
module.overprint(3)

function3()
function1()

f4()
# from module import *         --- means import all functions
