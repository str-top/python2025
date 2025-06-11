class Auto:
 
    def __init__(self, make, model, year, mileage, price, origin_ru='Россия'):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price
        self.orign_ru = origin_ru
 
    def makeModel(self):
        print(f'{self.make} {self.model}')
 
    def getAttrValue(self, attr):
        return getattr(self, attr)
 
    def __repr__(self):
        return f'{self.make} {self.model} {self.price}'
 
    def __str__(self):
        return f'{self.make} {self.model} - Price: RUR {self.price}, Production Year: {self.year}, Mileage: {self.mileage}'
 
 
def get_list_car_names(*autos: Auto):
    return list(autos)
 
 
def sorted_by_mileage(list_autos: list):
    return sorted(list_autos, key=lambda x: x.getAttrValue("mileage"))
#####
KiaSor = Auto('Kia', 'Sorrento', 2003, 223000, 415000)
HyunSol = Auto('Hyundai', 'Solaris', 2015, 41000, 869000, 'Корея')
VolkPas = Auto('Volkswagen', 'Passat', 2012, 127000, 900000, 'Германия')
LadaPri = Auto('Lada', 'Priora', 2011, 139000, 150000)
UazPat = Auto('UAZ', 'Patriot', 2011, 150000, 345400)
 
list_cars = get_list_car_names(KiaSor, HyunSol, VolkPas, LadaPri, UazPat)
print(list_cars, sep='\n') # тут __rep
print('-' * 21)
print(*list_cars, sep='\n') # тут __str
print('-' * 21)
print(sorted_by_mileage(list_cars))
