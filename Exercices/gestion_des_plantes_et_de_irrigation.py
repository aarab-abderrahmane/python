"""
Objectif du Projet : Gestion des Plantes et de l'Irrigation
L'objectif de ce projet est de créer un système de gestion de plantes dans une pépinière. Chaque
plante est représentée par une classe spécifique qui hérite d'une classe abstraite Plante. Le système
doit permettre de gérer des types variés de plantes, de calculer leurs besoins d'irrigation, et de
détecter automatiquement lorsqu'elles ont besoin d'eau.
1. Classe Plante (Classe Abstraite)
La classe Plante est la classe de base. Elle définit des attributs généraux communs à toutes les
plantes, ainsi qu'une méthode abstraite qui devra être implémentée dans chaque classe fille pour
calculer les besoins en irrigation.
Attributs de la classe Plante :
• nom (str) : le nom de la plante.
• type_plante (str) : le type de la plante (par exemple : Fleur, Arbre, Cactus).
• derniere_irrigation (str) : la date de la dernière irrigation au format YYYY-MMDD.
• besoin_irrigation (bool) : un attribut booléen qui indique si la plante a besoin
d'irrigation ou non.
Méthode abstraite detecter_besoin_irrigation() :
• Cette méthode doit être implémentée par chaque classe fille. Elle permet de
déterminer si la plante a besoin d'irrigation en fonction de critères spécifiques
(fréquence, taille, résistance à la sécheresse, etc.).
2. Classe Fleur (Héritage de Plante)
Les fleurs ont besoin d'être irriguées régulièrement. Leur irrigation doit être effectuée toutes les
semaines.
Attributs spécifiques :
• besoin_irrigation (bool) : un attribut qui devient True si la plante a besoin
d'irrigation (toutes les 7 jours).
Méthode detecter_besoin_irrigation() :
• Cette méthode vérifie si la dernière irrigation remonte à plus de 7 jours. Si c'est le
cas, la plante a besoin d'eau.
3. Classe Arbre (Héritage de Plante)
Les arbres ont des besoins en irrigation qui dépendent de leur taille. Les petits arbres nécessitent de
l'eau tous les 15 jours, tandis que les grands arbres peuvent avoir besoin d'irrigation tous les 30 jours.
Attributs spécifiques :
• hauteur (float) : la hauteur de l'arbre en mètres.
Méthode detecter_besoin_irrigation() :
• Cette méthode vérifie la taille de l'arbre pour déterminer si l'intervalle
d'irrigation est de 15 ou 30 jours, puis compare cette date avec la dernière
irrigation pour savoir si la plante a besoin d'eau.
4. Classe Cactus (Héritage de Plante)
Les cactus sont des plantes résistantes à la sécheresse. Ils peuvent passer de longues périodes sans
irrigation.
Attributs spécifiques :
• resistance_secheresse (int) : une échelle de 1 à 10 indiquant la résistance de la
plante à la sécheresse.
Méthode detecter_besoin_irrigation() :
• En fonction de la résistance à la sécheresse, les cactus peuvent avoir besoin
d'irrigation tous les 30 ou 60 jours.
5. Classe Pépinière (Gestion de la Liste de Plantes)
La classe Pépinière permet de gérer une liste de plantes. Elle offre des méthodes pour ajouter des
plantes et vérifier lesquelles ont besoin d'irrigation.
Attributs :
• plantes (list) : une liste contenant toutes les plantes.
Méthodes :
• ajouter_plante(plante) : permet d’ajouter une plante à la pépinière.
• Modifier / supprimer / rechercher selon plusieurs critéres
• Méthode pour afficher la liste des plantes qui ont besoin d’irrigation
• verifier_irrigation() : cette méthode parcourt toutes les plantes de la pépinière et
retourne une liste des plantes qui ont besoin d'irrigation (celles pour lesquelles
besoin_irrigation est True)
"""



from abc import ABC , abstractmethod
from rich.console import Console
from datetime import datetime

console=Console()


class Plante(ABC):
    def __init__(self,nom : str ,type_plante : str,derniere_irrigation : str):

        self.nom=nom 
        self.type_plante=type_plante
        self.derniere_irrigation=derniere_irrigation
        self.besoin_irrigation=False

    
    @abstractmethod

    
    def Detecter_besion_irrigation(self):
        pass

    def __str__(self):
        return (f'Plante : {self.nom} '
                f'\ntype : {self.type_plante}'
                f'\nDerniere irrigation : {self.derniere_irrigation}'
                f'\nBesoin d irrigation : {"Oui" if self.besoin_irrigation else "Non"}')
    


class Fleur(Plante):
    def __init__(self,nom:str,derniere_irrigation:str):
        super().__init__(nom,"Fleur",derniere_irrigation)

    
    def Detecter_besion_irrigation(self):
        date_derniere=datetime.strptime(self.derniere_irrigation,"%Y-%m-%d")
        ajourd_hui=datetime.now()
        jours_ecoules=(ajourd_hui - date_derniere).days
        self.besoin_irrigation=jours_ecoules > 7



class Arbre(Plante):
    def __init__(self,nom:str , derniere_irrigation:str , hauteur : float):
        super().__init__(nom,"Arbre",derniere_irrigation)
        self.hauteur=hauteur

    def Detecter_besion_irrigation(self):

        intervalle  = 15 if self.hauteur <=2 else 30
        date_derniere=datetime.strptime(self.derniere_irrigation,"%Y-%m-%d")
        aujourd_hui=datetime.now()
        jours_ecoules=(aujourd_hui - date_derniere).days

        self.besoin_irrigation=jours_ecoules > intervalle


class Cactus(Plante):
    def __init__(self,nom:str,derniere_irrigation:str,resistance_secheresse:int):
        super().__init__(nom,"Cactus",derniere_irrigation)
        self.resistance_sechresse=resistance_secheresse

    def Detecter_besion_irrigation(self):
        date_derniere=datetime.strptime(self.derniere_irrigation,"%Y-%m-%d")
        aujour_hui=datetime.now()
        jours_ecoules=(aujour_hui - date_derniere).days

        if self.resistance_sechresse >= 7 :  
         self.besoin_irrigation = jours_ecoules >= 60

        else : self.besoin_irrigation = jours_ecoules >= 30

class Pepiniere:
    def __init__(self):
        self.list_plante=[]
    
    def Ajouter_plante(self,plante):
        self.list_plante.append(plante)
    
    def Modifier_plante(self,nom,nouveau_nom=None,dernier_irrigation=None,type_plante=None,hauteur=None,resistance_sechresse=None):


        for plante in self.list_plante : 
            if plante.nom == nom : 
                

                if nouveau_nom is not None : 
                    plante.nom=nouveau_nom

                if dernier_irrigation is not None : 
                    plante.derniere_irrigation=datetime.strptime(dernier_irrigation,'%Y-%m-%d')
                
                if type_plante is not None : plante.type_plante=type_plante

                if hauteur is not None  and isinstance(plante,Arbre): plante.heuteur=hauteur

                if resistance_sechresse is not None and isinstance(plante,Cactus) : plante.resistance_sechresse=resistance_sechresse

    def Supprimer_plante(self,nom):
        for plante in self.list_plante : 
            if plante.nom == nom :  self.list_plante.remove(plante)
            return 
    
    def Rechercher_plante(self,nom=None,type_plante=None,besoin_irrigation=None):
        resultats=[]
        for plante  in self.list_pl : 
            correspondante = True
            if nom is not None  and plante.nom !=nom : 
                correspondante=False
            
            if type_plante is None and plante.type_plante!=type_plante : 
                correspondante=False
            
            if besoin_irrigation is not None : 
                plante.detecter_besoin_irrigation()
                if plante.detecter_besoin_irrigation != besoin_irrigation : 
                    correspondante=False

            if correspondante : 
                resultats.append(plante)
        return resultats       

    def Afficher_list_irrigation(self):
        list_=[]
        for plante in self.list_plante : 
            plante.detecter_besoin_irrigation()
            if plante.besoin_irrigation : 
                list_.append(plante)
        
        return list_
                
    def Afficher_plantes_a_irriger(self):
        plante_a_irriguer=self.Afficher_list_irrigation()
        if plante_a_irriguer : 
            for plante in plante_a_irriguer : 
                print(f' _ {plante.nom} : ({plante.type_plante})')
        
        else : 
            print("Aucun plante n'a besoin d'irrigation pour le moment.")

    def Afficher_toutes_les_plantes(self):
        if self.list_plante : 
            for plante in self.list_plante : 
                print(plante)
                print('\n')
                print('-'*40)

    def Afficher_plantes_non_irriger(self) :
        list_plantes_non_irrriguer=[]
        for plante in self.list_plante : 
            plante.detecter_besoin_irrigation()
            if not plante.detecter_besoin_irrigation() :
                list_plantes_non_irrriguer.append(plante)

        for plante in list_plantes_non_irrriguer:
            print(plante) 


try:

    fleur_1 = Fleur("m9tach", '2001-08-02')
    fleur_1.Detecter_besion_irrigation()
    print(fleur_1)
except Exception as e:
    console.print(f"[bold red]Erreur détectée :[/bold red] {e}")



