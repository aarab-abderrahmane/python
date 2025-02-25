from abc import ABC,abstractmethod

class AdCampaign(ABC) : 
    def __init__(self,nom,budget,canal) :
        self.nom = nom 
        self._budget = budget
        self.canal = canal


    @abstractmethod
    def Calculer_portée(self):
        raise NotImplementedError('error 101.')

    # Decorators
    @property 
    def budget(self): #getter
        return self._budget
    
    @budget.setter 
    def budget(self,value):
        if value <=0 :
            raise InvalidBidgetError()
        
        self._budget = value


    def afficher_details(self):
        return f"Nom : {self.nom} , Budget : {self.budget} ,canal : {self.canal}"
    
    def __str__(self):
        return f'Compagne : {self.nom} | budget : {self.budget} | Canal : {self.canal}'


    def __eq__(self,other):
        if isinstance(other,AdCampaign):
            return self.nom == other.nom and self.budget == other.budget and self.canal == other.canal

        return False
    



class InvalidBidgetError(Exception):
    def __int__(self,message = "le budget ne peut pas etre negatif ou nul."):
        super().__init__(message)


class GoogleAdsCampaign(AdCampaign):
    def __init__(self, nom, budget, canal,cpc):
        super().__init__(nom,budget,canal)
        self.cpc = cpc

    def Calculer_portée(self):
        return self.budget / self.cpc
    
    def afficher_details(self):
        return f"{super().afficher_details()} , nombre par clic : {self.Calculer_portée()}"
    

    
class FacebookAdsCampaign(AdCampaign):
    def __init__(self,nom,budget,canal,cpm):
        super().__init__(nom,budget,canal)
        self.cpm=cpm
    
    def Calculer_portée(self):
        return f"le nombre d'inmpressions : {(self.budget / self.cpm) *1000}"
    
    def afficher_details(self):
        return f"{super().afficher_details()} ,le nombre d'impressions : {self.Calculer_portée()}"
    

class YoutubeAdsCampaign(AdCampaign):
    def __init__(self, nom, budget, canal,cpv):
        super().__init__(nom, budget, canal)
        self.cpv = cpv
    
    def Calculer_portée(self):
        return f'le nombre de vues estimees : {self.budget / self.cpv}'
    
    def afficher_details(self):
        return super().afficher_details() + f" ,le nombre de vues estimees : {self.Calculer_portée()}"