from abc import ABC , abstractmethod

class Creature(ABC):
    def __init__(self,_id:str,nom:str,age:int,power:int):
        
        self._id=id(_id)
        self.nom=nom
        self.age=age
        self.power=power
    
    @abstractmethod
    def make_sound(self) : pass

    @abstractmethod
    def attack(self):pass
    
    def __str__(self):
        return f"{self.nom} : \n type class : {self.__class__.__name__} , \n id {self._id}  ,\n Age {self.age} ,\n power  {self.power}"
    

class Animal(Creature):
    def __init__(self, _id, nom, age, power,species):
        super().__init__(_id,nom,age,power)
        self.species=species

    def make_sound(self):
        return 'how how!'
    
    def attack(self):
        return 'the animla bites'
    
    def __str__(self):
        return f'{super().__str__()} ,\n species {self.species}'
    
class MagicalCreature(Creature):
    def __init__(self, _id, nom, age, power,magic_type):
        super().__init__(_id,nom,age,power)
        self.magic_type=magic_type

    def make_sound(self):
        return 'magic voice'
    
    def attack(self):
        return 'The creature casts magic'

class Dragon(Creature):
    def __init__(self, _id, nom, age, power,wing_span):

        super().__init__(_id,nom,age,power)
        self.wing_span=wing_span
    
    def make_sound(self):
        return 'dragon voice'
    
    def attack(self):
        return 'dragon shoots'
    
    def __str__(self):
        return f'{super().__str__()} \n wing span : {self.wing_span}'


animal_1=Animal(1,"animal_1",5,5,"cow")
print(animal_1)

Dragon_1=Dragon(1,"dragon1",100,9,200)
print('\n',Dragon_1)

print(Dragon_1.make_sound())