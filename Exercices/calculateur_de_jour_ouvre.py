# Calculateur de Jour Ouvré
# Écrire un programme qui demande une date et indique si elle tombe un jour ouvré (lundi à
# vendredi) ou le week-end (samedi et dimanche). Utilisez if-else pour afficher "Jour ouvré" ou
# "Week-end
from datetime import datetime

def verifie_jour_ouvre():
    date_str=input("entez une date 'j/m/A' : ").strip()
    try:
        date=datetime.strptime(date_str,'%d/%m/%Y')
        if date.weekday() == 6 : print("wekk-end")    #sunday:6
        else: print("jour ouvre")
    except ValueError : 
        print("format de date invalide")
        