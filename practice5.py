# chapter9   class
from collections import OrderedDict
from module1 import ElecCarModel2
from module1 import ElecCarModel
from module import CarModel
print('******   chapter9    ******')

# 9.1 creat a new class

''' for python 2.7   must assign a object

    class classname(object):
        ....
        ....

'''


class CarMotion():
    def __init__(self, s, yaw):
        self.s = s
        self.yaw = yaw

    def rrotate(self):
        self.yaw = self.yaw - 90

    def lrotate(self):
        self.yaw += 90

    def runforward(self, s_dot):
        self.s += s_dot


sx11 = CarMotion(11, 20)
print(sx11.s, sx11.yaw)
sx11.rrotate()
print(sx11.s, sx11.yaw)
sx11.lrotate()
print(sx11.s, sx11.yaw)
sx11.runforward(20)
print(sx11.s, sx11.yaw)

# 9.3 class inherit

# father class


class CarModel():
    def __init__(self, brand, procedure_data):
        self.brand = brand
        self.procedure_time = procedure_data
        self.odometers = 0

    def print_all(self):
        print('brand:'+self.brand.title())
        print('procedure:'+self.procedure_time.title())
        print('odometers:'+str(self.odometers))


boral = CarModel('greey', '2019.01.01')
boral.print_all()

# child class & import class

'''
class ElecCarModel(CarModel):
    def __init__(self, brand, procedure_data, bq):
        super().__init__(brand, procedure_data)
        self.battery_quantity = bq

    def battery_charge(self, bq):
        self.battery_quantity += bq

    def battery_print(self):
        print('battery:'+str(self.battery_quantity)+'%')

class BatteryClass():
    def __init__(self, quantity):
        self.quantity = 0

    def printQuantity(self):
        print('battery:'+str(self.quantity)+'%')


class ElecCarModel2(CarModel):
    def __init__(self, brand, procedure_data):
        super().__init__(brand, procedure_data)
        self.battert_Quantity = BatteryClass(60)

    def print_all(self):
        super().print_all()
        print('battery:'+str(self.battert_Quantity.quantity)+'%')
'''

boralGE = ElecCarModel('greey', '20190101', 58)
print(boralGE.battery_quantity)
boralGE.print_all()
boralGE.battery_print()

boralGe2 = ElecCarModel2('greey', '20190101')
boralGe2.battert_Quantity.printQuantity()
boralGe2.print_all()

# import class


paperpoint = OrderedDict()
paperpoint['zhangsan'] = 90
paperpoint['lisi'] = 99
paperpoint['xiaoming'] = 60
print(paperpoint)

for v, k in paperpoint.items():
    # print(v.title())
    print(v.title() + ' get ' + str(k) + ' points')
