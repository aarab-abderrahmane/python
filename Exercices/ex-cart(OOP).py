class Cart : 

    def __init__(self):

        self.listProducts=[]
    
    def AddProduct(self,product):

        for produit in self.listProducts : 

            if  produit['codep']==product['codep']:
                produit['quantite']+=1
                return 


        product['quantite']=1
        self.listProducts.append(product)
    
    def RemoveProduct(self,product):

        for produit in self.listProducts:

            if produit['codep']==product['codep']:

                self.listProducts.remove(produit)
                return 'successful'
    
            return 'this produit does not exist'
        
    def IncrementQuantite(self,product):
        for produit in self.listProducts : 

            if product['codep']==produit['codep']:

                produit["quantite"]+=1

                if produit['quantite']==0:
                    self.listProducts.remove(produit)
                    return 'the product has been removed '
                
                return 'the quantite has been changed'
            
    
    def DecrementQuantie(self,product):

        for produit in self.listProducts:

            if product['codep'] == produit['codep']:
                
                produit['quantite']-=1

                if produit['quantite']==0 : 
                    self.listProducts.remove(produit)
                    return 'the product has been removed'
                
                return 'the quantite has been changed'
    
    def TotalAmount(self):
        total=0

        for produit in self.listProducts:
                
            total+=produit['prix']*produit['quantite']
        
        return f'totale produits is : {total}'
    
    def __str__(self):

        output="codep\tintitule\tprix\tquantite\n"

        for produit in self.listProducts : 
            output+= f"{produit['codep']}\t{produit['intitule']}{'\t'*2*len({produit['intitule']})}{produit['prix']}\t{produit['quantite']}\n"

        return output
    

cart=Cart()
cart.AddProduct({"codep":100,"intitule":"ordi","prix":60000})
cart.AddProduct({"codep":100,"intitule":"scanner","prix":6000})
cart.AddProduct({"codep":800,"intitule":"ordi","prix":40000})


print(cart)
