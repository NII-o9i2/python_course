# Chapter 2
print("hello world")

message = "Hello Freetech!"
print(message)

# single quotes same as double quotes
message = "I am double quotes"
message1 = 'I am single quotes'
print(message)
print(message1)

# capital and small letter
print(message.title())

print(message.upper())
print(message.lower())

# string add
corp = 'Freetech'
name = 'xiaotong feng'
print(corp + '  This is ' + name.title())

#tab and enter
print('\t' + name.title())
print('\n end')

print("\t" + name.title())
print("\n end")

# delete blank in the begin and end
message = ' i am NII '
print(message.rstrip())
print(message.lstrip())
print(message.strip())

print(2 + 3)
# 2 to the power of 3
print(2 ** 3)

age = 25
print('happy ' + str(age) + ' birthday!')

# chapter3 list
# list
self_driving = ['perception', 'planning', 'control']
print(self_driving)
print(self_driving[0])

# -1 means the last one
print(self_driving[-1])

# modify , add , delete list
self_driving[0] = 'perception1'
print(self_driving)

self_driving.append('stop')
print(self_driving)

self_driving.insert(1, 'new insert')
print(self_driving)

del self_driving[1]
print('after delete')
print(self_driving)

# pop function
list_pop = self_driving.pop(-1)
print(list_pop)
print(self_driving)

# remove
self_driving.remove('control')
print(self_driving)

# sort list
car_brand = ['bwm', 'audi', 'toyota', 'subaru']
car_brand.sort()
print(car_brand)

car_brand = ['bwm', 'audi', 'toyota', 'subaru']
print(sorted(car_brand))
print(car_brand)


car_brand.reverse()
print(car_brand)
print(len(car_brand))

# chapter4 list operation
# traverse list
print('******   chapter4    ******')

internet_corpname = ['baidu', 'alibaba', 'tencent', '360', 'xiaomi']
for name in internet_corpname:
    print(name)
    print('\tis a great company!')
print("It's over")

# number list   range(i,j) contain i to j-1
for value in range(2, 10):
    print(value)

# range() to a list
numlist = list(range(2, 10))
print(numlist)

numlist = list(range(2, 11, 3))
print(numlist)

print(max(numlist), min(numlist), sum(numlist))

# list analysis
list_a = [value**2 for value in range(1, 4)]
print(list_a)

# list section
top3_internet_corp = internet_corpname[0:3]
print(top3_internet_corp)

last3_internet_corp = internet_corpname[-3:]
print(last3_internet_corp)

# copy list

print('\n')
print(internet_corpname)
new_internet_corpname = internet_corpname[:]
new_internet_corpname.append('netease')
internet_corpname.append('yahoo')

print(new_internet_corpname)
print(internet_corpname)

# wrong case  if without [:] then newlist is not a copy
print(internet_corpname)
new_internet_corpname = internet_corpname
new_internet_corpname.append('netease')
internet_corpname.append('yahoo')

print(new_internet_corpname)
print(internet_corpname)

# dimension means a list which can not be modified
dimension = (200, 50)
print(dimension[0], dimension[1])
dimension = (300, 100)
print(dimension[0], dimension[1])

# chapter5   if - else
print('******   chapter5    ******')
for value in range(1, 10):
    if value == 3:
        print('find it')
    else:
        print("*")

for value in range(1, 10):
    if value != 3:
        print('no')
    else:
        print("*")

for value in range(1, 100):
    if value % 7 == 0 and value % 5 == 0:
        print(value)
# check list

print('xiaomi' in internet_corpname)
print('google' in internet_corpname)

salary_threshold = [9000, 13000, 20000, 25000]
salary_set = 23000
if salary_set <= salary_threshold[0]:
    print("5%")
elif salary_set <= salary_threshold[1]:
    print('10%')
elif salary_set <= salary_threshold[2]:
    print('20%')
else:
    print('30%')
# check empty
empty_list = []
if empty_list:
    print('not empty')
else:
    print('empty')

# chapter6   dictionary
print('******   chapter6    ******')
