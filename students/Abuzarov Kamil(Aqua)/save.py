 from animals import *
p = Dog("Шарик", 5)
p.gettingOlder()
print( p.name + ":", p.age, "лет")
pets = [ Cat("Мурка", 3), p ]
for p in pets:
  p.say()

from animals import * 
pets = [Cat("Мурзик", 3), 
        Dog("Шарик", 5) ]
for p in pets:
  p.say()
  p.run()
