class Vehicle :
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def display_info(self):
        return f"information : brand {self.brand} model {self.model}"


class Car(Vehicle):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model)

        self.fuel_type=fuel_type
    
    def display_info(self):
       print(f"{super().display_info()} and fuel type : {self.fuel_type}")
    

car_1=Car("dacia","2022","H")

car_1.display_info()