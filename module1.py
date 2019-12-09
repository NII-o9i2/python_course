from module import CarModel

def function1():
    print('this is function1')


def function2():
    print('this is function2')

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

