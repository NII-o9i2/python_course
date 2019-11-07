# chapter10 file and abnormal
import json
with open('data\pi_digits.txt') as file_object:
   # content = file_object.read()
   # print(content.upper())
    ans = ''
    for line in file_object:
        print(line.rstrip())
        ans += line.strip()
    print(ans)
    print(len(ans))

million_pi_file = 'data\pi_million.txt'
with open(million_pi_file) as file_pi_million:
    lines = file_pi_million.readlines()

ans_str = ''
for l_str in lines:
    ans_str += l_str.strip()

print(len(ans_str))

# 10.2 write message

write_file = 'data\printlog.txt'

# r - read    w - write     a - append    r+  - read & write
with open(write_file, 'w') as file_object:
    file_object.write('I am NII. \n')
    file_object.write('Nice to see u! \n')

with open(write_file, 'a') as file_object:
    file_object.write('I am append content')

# 10.3 abnormal

try:
    a = float(input('first number'))
    b = float(input('second number'))
    try:
        print(a/b)
    except ZeroDivisionError:
        print(' u can not divide by zero!')
    else:
        print('succeed!')
except ValueError:
    print('wrong input!')


# store data    -- json

# outport data

# import json

data = [1, 5, 9, 7, 5, 3]
data2 = ['a', 'b', 'f']

file_name = 'data/testjson.json'
with open(file_name, 'w') as j_object:
    json.dump(data, j_object)
    #des = json.dump(data)
    # print(des)
    # print(type(des))
    #json.dump(data2, j_object)


# chapter11 test code
