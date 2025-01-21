class Converter : 
    def __init__(self,mot):
        self.mot=mot
    
    def get_base_classic(self):

        detecte=self.mot[0:2]
        base=''

        if detecte.lower() == "0b": base="Base 2"
        elif detecte.lower()=="0o" : base="Base 8"
        elif detecte.lower()=="0x" : base="Base 16"
        else : base="Base 10"

        return base
    
    def get_base(self) : 
        if self.mot.startswith(('0b','0B')): return 2
        elif self.mot.startswith(('0o','0O')) : return 8
        elif self.mot.startswith(('0x','0X')) : return 16
        else : 

            try : 
                int(self.mot)
                return 10
            
            except ValueError: return  None

    
    def Conversion_base(self,to_base:str):
        detect_base=self.get_base()
        if detect_base is None : 
            raise ValueError("le mot fourni n'est pas un nombre valide dans une base reconnue.")
        

        try :
            decimal_value=int(self.mot,detect_base)
        except :
            raise ValueError('Imporssible de convertir le mot en entier avec la base detectee')

        if to_base=="2": return bin(decimal_value)
        elif to_base=="8" : return oct(decimal_value)
        elif to_base=="10" : return str(decimal_value)
        elif to_base=="16" : return hex(decimal_value)

        else: 
            raise ValueError('La base cible specifiee est invalide.')

try : 

    nombre =  Converter("0565")
    print(nombre.get_base())
    print(nombre.Conversion_base("2"))

except ValueError  as e : 
    print(e)
    