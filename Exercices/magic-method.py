class Person : 

     #constractor
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #fonction
    def info(self):
        return f'my name is {self.name} and my age is {self.age}'
    

    #magic method
    def __str__(self):
        return f'my name is {self.name} and my age is {self.age}'

    
    def __eq__(self,other):
        if isinstance(other,Person):
            return self.name==other.name
        else:
            return False
        
    #dunder method
    def __lt__(self,other): # <
        if isinstance(other,Person): return self.age < other.age
        else:return False

    def __gt__(self,other):  # >
        if isinstance (other,Person):return self.age > other.age
        return NotImplemented

person_1,person_2,person_3=Person("abdu",18),Person('abdu',16),Person('homelaner',30)




print(person_1)

print(person_1==person_2)
print(person_1==person_1)
print(person_1=="choaib") #no isinstance 
print(person_1==person_3)


print('________________________\n')

print(person_1<person_2)
print(person_1<12)


print(person_1>person_2)
print(person_2>45)


