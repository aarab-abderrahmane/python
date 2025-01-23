from abc import ABC , abstractmethod
import re


class NetworkComponenet(ABC):

    @abstractmethod
    def info(self):
        "information sur le composant reseau"
        pass

    @abstractmethod
    def fonctionner(self):
        "le role du composnat reseau"
        pass


class IPv4(NetworkComponenet):
    def __init__(self,adresse):
        self.adresse=adresse
    

    def info(self):
        return f'Adresse IPv4 : {self.adresse}'
    
    def fonctionner(self):
        return "gestion des adresses IPv4"
    
    def isValidIPv4(self):
        pattern=r"^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
       
        """
        25[0-5]:

        Matches numbers from 250 to 255.

        2[0-4][0-9]:

        Matches numbers from 200 to 249.

        [0-1]?[0-9][0-9]?:

        Matches numbers from 0 to 199.

        \.:

        Matches a literal dot (.), which separates the octets.

        ^ and $:

        ^ asserts the start of the string.

        $ asserts the end of the string.

        These ensure the entire string is matched, not just a part of it.

        {} : repeat

        | : or

        syntaxe : r"^ ... $"
        """
        return re.match(pattern,self.adresse) is not None

    def getClasse(self):
        if not self.isValidIPv4():
            raise ValueError('adreesee IPv4 invalide.')
        
        premier_octet = int(self.adresse.split(".")[0])

        if 1<=premier_octet<=126 : return "A"
        elif 128<=premier_octet<=233 : return "B"
        elif 244 <= premier_octet <=239 : return "C"
        elif 240 <= premier_octet <= 255 : return "E"

        else : return None 

    def getMasque(self):

        classe=self.getClasse()
        if classe =="A" : return "255.0.0.0"
        elif classe =="B" : return "255.255.0.0"
        elif classe =="C" : return "255.255.255.0"
        else : return "Non applicable pour les clasees D et E"

    def getIdReseau(self):
        if not self.isValidIPv4() : 
            raise ValueError('Adresse Ipv4 invalide.')

        octets = self.adresse.split('.')
        masque= self.getMasque().split(".")
        id_reseau = [str(int(octets)& int(m)) for octet , m in zip(octets,masque)]
        return '.' .join (id_reseau)
    
        """
        If octets = ["192", "168", "1", "1"] and masque = ["255", "255", "255", "0"], then:

        192 & 255 = 11000000	&	11111111	=	11000000  = 192

        168 & 255 = 168

        1 & 255 = 1

        1 & 0 = 0

        So, id_reseau = ["192", "168", "1", "0"].


        """
    

    def getHost(self): 

        if not self.isValidIPv4() : 
            raise ValueError('Adresse Ipv4 invalide .')
        
        octets=self.adresse.split('.')
        masque=self.getMasque().split('.')
        id_host =  [str(int(octets & ~ int(m))) for octet , m in zip(octets,masque)]
        return ".".join(id_host)
    
    """
    & : AND  

    ~ : NOT 

    ~ 10 =  ~11110110 = 00001001
    """
    def getNbrofHots(self):
        masque=self.getMasque()
        if masque in ['Non applicable pour les classes D et E']:
            return 0
        bits_hote = sum(bin(255-int(octet)).count('1') for octet in masque.split('.'))
        return (2 ** bits_hote) - 2 
        
        """
        bin(255) ---> 11111111.count('1') --> 8  --> 8 bit

        Usable Hosts:
        Subnetting reserves 2 addresses:
        1 for the network address.
        1 for the broadcast address.            

        2 ** n - (1+1)


        """