from rich.console import Console 
from abc import ABC , abstractmethod
import json 
import csv

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



class CD(Document):
    def __init__(self,id_,titre,auteur,annee_publication,genre_musical,duree):
        
        super().__init__(id_,titre,auteur,annee_publication)
        self.genre_musical=genre_musical
        self.duree=duree

    def afficher_details(self):
        return f'{super().__str__()}\n\t__ genre musical : {self.genre_musical}\n\t__ duree : {self.duree}'

    def __str__(self):
        return self.afficher_details()


class Bibliotheque:

    def __init__(self):
        
        self.documents=[]

    def Ajouter_Document(self,document):

        self.documents.append(document)
        Console().print(f'\n[green]le Document {document.titre} ajoute a la bibliotheque [/green]')
    
    def Supprimer_Document(self,id_):

        for item in self.documents : 
            if item.id==id_:
                self.documents.remove(item)
                Console().print(f'[green]Document avec ID {id_} supprime de la bibliotheque')
                return
        
        Console().print(f"[red]Aucun document trouve avec l'ID {id_}[/red]")
    
    def Mettre_A_Jour_Document(self,id_,titre=None,auteur=None,annee_publication=None):

        for item in self.documents:
            if item.id==id_:

                item.modifier_details(titre,auteur,annee_publication)
                print(f"Document avec ID {id} mis à jour.")
                return 
            
        print(f"Aucun document trouvé avec l'ID {id}.")            

    def Afficher_Document(self):

        if not self.documents: 
            print('la bibliotheque est vide')
        
        else: 

            for item in self.documents : 
                print('\n',item)
                print("_"*40)
    

    def Filtrer_Document(self,criters,valeur):

        resultats=[]

        if criters=="annee":     
            resultats=[doc for doc in self.documents if doc.annee_publication==valeur]
        
        if criters=="auteur": 
            resultats=[doc for doc in self.documents if doc.auteur==valeur]

        else : 
            Console().print("[red]Critère de filtre non valide. Utilisez 'annee' ou 'auteur'.[/red]")
        
        if not resultats:
            Console().print("[red]Critere de filtre non valide . Utilisez 'annee' ou 'auteur'[/red]")
        
        else : 
            for item in resultats: 
                print('resultats : \n',item)

    def Serialiser_json(self,fichier):
        data=[]

        for item in self.documents:

            item_dict={
                "id":item.id,
                "titre":item.titre,
                "auteur":item.auteur,
                "annee_publication":item.annee_publication
            }

            if isinstance(item,Livre):
               item_dict['type']="Livre"
               item_dict['isbn']=item.isbn
               item_dict['nombre_pages']=item.nombre_pages
            
            elif isinstance(item,Revue):
                item_dict['type']="Revue"
                item_dict["numero"] = item.numero
                item_dict["frequence"] = item.frequence
            elif isinstance(item, CD):
                item_dict["type"] = "CD"
                item_dict["genre_musical"] = item.genre_musical
                item_dict["duree"] = item.duree
            
            data.append(item_dict)
        
        with open(fichier,'w') as f :
            json.dump(data,f,indent=4)
        
        Console().print(f"[yellow]Données sérialisées dans {fichier} (JSON).[/yellow]")

    def serialiser_scv(self,fichier):
        data=[]

        for item in self.documents:

            item_dict={
                "id":item.id,
                "titre":item.titre,
                "auteur":item.auteur,
                "annee_publication":item.annee_publication
            }

            if isinstance(item,Livre):
               item_dict['type']="Livre"
               item_dict['isbn']=item.isbn
               item_dict['nombre_pages']=item.nombre_pages
            
            elif isinstance(item,Revue):
                item_dict['type']="Revue"
                item_dict["numero"] = item.numero
                item_dict["frequence"] = item.frequence
            elif isinstance(item, CD):
                item_dict["type"] = "CD"
                item_dict["genre_musical"] = item.genre_musical
                item_dict["duree"] = item.duree
            
            data.append(item_dict)

        with open(fichier,"w",newline="") as f : 
            writer =csv.DictWriter(f,fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print(f"Données sérialisées dans {fichier} (CSV).")


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

    print(livre,'\n\n')

    cd = CD(
        id_=3,
        titre="Best of Jazz",
        auteur="Various Artists",
        annee_publication=2020,
        genre_musical="Jazz",
        duree=60.5)
    
    print(cd)


    bibliotheque=Bibliotheque()

    bibliotheque.Ajouter_Document(revue)
    bibliotheque.Ajouter_Document(livre)

    bibliotheque.Afficher_Document()

    bibliotheque.serialiser_scv("document.json")
    

except ValueError as e : 
    print(e)



