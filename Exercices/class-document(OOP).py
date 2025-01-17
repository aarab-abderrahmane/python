from rich.console import Console 
from abc import ABC , abstractmethod

# class abstraite
class Document(ABC):
    def __init__(self,id_,titre,auteur,annee_publication):

        self.id=id(id_)
        self.titre=titre
        self.auteur=auteur
        self.annee_publication=annee_publication

        if self.annee_publication < 1990 : 
             raise ValueError("l'annee de publication doit etre superieur ou egale a 1990.")

    @abstractmethod

    def afficher_details(self):
        pass 
    

    def modifier_details(self,titre=None,auteur=None,annee_publication=None):

        for item in (titre,auteur,annee_publication):
            if titre is not None: self.titre=titre
            if auteur is not None : self.auteur=auteur
            if annee_publication is not None : self.annee_publication=annee_publication

        Console().print("[green]Details updated successfully![/green]")
        
    def __str__(self):
            return f'\t__ ID : {self.id}\n\t__ titre : {self.titre}\n\t__ auteur : {self.auteur}\n\t__ annee_publication : {self.annee_publication}'


#class herite de document 

class Livre(Document) : 

    def __init__(self,id_,titre,auteur,annee_publication,isbn,nombre_pages):

        super().__init__(id_,titre,auteur,annee_publication)
        self.isbn=isbn
        self.nombre_pages=nombre_pages

    def afficher_details(self):
        
        return f"{super().__str__()}\n\t__ ISBN : {self.isbn}\n\t__ Nombre de pages : {self.nombre_pages}"

    def __str__(self):
         
        return self.afficher_details()

class Revue(Document):
    def __init__(self,id_,titre,auteur,annee_publication,numero,frequence):
        super().__init__(id_,titre,auteur,annee_publication)   
        self.numero=numero
        self.frequence=frequence

    def afficher_details(self):
        return f"{super().__str__()}\n\t__ Numero : {self.numero}\n\t__ Frequence : {self.frequence}"  

    def __str__(self):
        return self.afficher_details()        



try : 
    revue=Revue(
        id_=1,
        titre="Science",
        auteur='Jane',
        annee_publication=2022,
        numero=15,
        frequence="Mensuelle"
    )

    print(revue,'\n\n')


    livre=Livre(
        id_=1,
        titre="en",
        auteur="abdu",
        annee_publication=2025,
        isbn="nothing",
        nombre_pages=100
    )

    print(livre)
    

except ValueError as e : 
    print(e)



