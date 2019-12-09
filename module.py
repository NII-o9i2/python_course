def studing():
    print("studing ...")


def overprint(no):
    for i in range(1, no+1):
        print('bye bye')


def function3():
    print('this is function3')

def function4():
    print('this is function4')



class CarModel():
    def __init__(self, brand, procedure_data):
        self.brand = brand
        self.procedure_time = procedure_data
        self.odometers = 0

    def print_all(self):
        print('brand:'+self.brand.title())
        print('procedure:'+self.procedure_time.title())
        print('odometers:'+str(self.odometers))



