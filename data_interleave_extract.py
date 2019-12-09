count = 1
data = []
with open('data\planning_data_raw.txt') as file_object:
    for line in file_object:
        data.append(line)
        print(line)
        count += 1
print(count)
with open('data\planing_data_5.txt', 'w') as file_object:
    for ii in range(1, count):
        if ii % 5 == 0:
            file_object.write(data[ii])
