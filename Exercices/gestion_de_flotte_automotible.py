from abc import ABC ,abstractmethod

class Vehicule(ABC):
    def __init__(self,nom_client,matricule,capacite):
        self.nom_client = nom_client
        self.matricule = matricule
        self._capacite = capacite
    
    @abstractmethod
    def Calculer_efficiency(self):
        raise NotImplementedError("La méthode calculer_efficiency() doit être redéfinie dans la sous-classe.")


    def ajuster_capacite(self,valeur):
        self._capacite = max(0,self._capacite+valeur)

    def __str__(self):
        return f'Client : {self.nom_client}  | Matricule : {self.matricule}  | Capicite : {self._capacite} kg'


    def __eq__(self,x):
        if isinstance(x , Vehicule):
            if x.matricule == self.matricule : return True
            else: return False
        
        else : return False
    
    #Decorateurs
    @property
    def capacite(self):
        return self._capacite

    @capacite.setter
    def capacite(self,valeur):
        if valeur < 0 : raise CapaciteError()

        self._capacite = valeur


class Voiture(Vehicule):
    def __init__(self,nom_client,matricule,capacite,consomation):
        super().__init__(nom_client,matricule,capacite)
        self.consomation = consomation
    
    def Calculer_efficiency(self):
        return f't l’autonomie du véhicule en fonction du carburant disponible : {100/self.consomation if self.consomation > 0 else float('inf')}'
    
    


class Camion(Vehicule):
        def __init__(self, nom_client, matricule, capacite,charge_max,consomation):
             super().__init__(nom_client, matricule, capacite)
             self.charge_max=charge_max
             self.consomation = consomation
        
        def Calculer_efficiency(self,charge):
            if charge > self.charge_max : return'0'
            return f'e la distance pouvant être parcourue en fonction de la charge transportée : {100/((1+charge/self.charge_max)*self.consomation)}'
        
             
class CapaciteError(Exception):
    def __init__(self, message="La capacite ne peut pas etre negative."):
        super().__init__(message)


v_1 = Voiture("XYZ Logistics", "123-ABC", 500, 6.5)

print(Voiture.__str__(v_1))
print(v_1)


try : 
    v_1.capacite = -100

except CapaciteError as e : 
    print(e)



try:
    v_2 = Vehicule("Test Client", "999-XYZ", 1000)  
    print(v_2.calculer_efficiency())  
except NotImplementedError as e:
    print(f"Erreur détectée : {e}")