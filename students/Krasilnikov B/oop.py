class Pet:

    def __init__(self,name,animal_type,hunger,energy):
        self.name = name
        self.animal_type = animal_type
        self.hunger = hunger
        self.energy = energy
        
    def feed(self):
        if (self.hunger - 2) < 0:
            print(f'''
            ваш питомец не голоден)
            уровень его голода равен {self.hunger}    
            ''')
        else:
            self.hunger -= 2
            print(f'''
            вы покормили питомца
            уровень голода вашего питомца равен {self.hunger}
            ''')
            
    def play(self):
        if (self.hunger + 1) > 10:
            print(f'''
            ваш питомец очень голоден(
            СРОЧНО ПОКОРМИ ЕГО!!!
            уровень его голода равен {self.hunger}    
            ''')
        else:
            self.hunger += 1
            print(f'''
            ваш питомец поиграл и немного подустал
            уровень голода вашего питомца равен {self.hunger}
            ''')
            
    def sleep(self):
        self.energy += 2
        print(f'''
        энергия: {self.energy}''')
            
    def run(self):
        self.energy -= 1
        print(f'''
        энергия: {self.energy}
        ''')
            
    
    def get_status(self):
        print(f'''
        {self.animal_type} {self.name}
        (голод: {self.hunger})
        (энергия: {self.energy})
        ''')

dog = Pet('Гаврик','Песик',5,5)

dog.feed()
dog.feed()
dog.feed()
dog.feed()
dog.play()
dog.play()
dog.play()
dog.play()
dog.play()
dog.play()
dog.play()
dog.play()
dog.play()
dog.play()
dog.play()
dog.play()
dog.play()
dog.play()
dog.run()
dog.sleep()
dog.get_status()
