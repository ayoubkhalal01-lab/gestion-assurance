from abc import ABC , abstractclassmethod

class Assurance(ABC):
    def __init__(self,numero_contrat,nom_client):
        self.numero=numero_contrat
        self.nom_client=nom_client
    def afficher_infos(self):
        print("numerp de contrat:",self.numero_contart)
        print("nom de client:",self.nom_client)
    @abstractclassmethod
    def calculer_prime(self):
        pass
o1=Assurance(34,"ayoub")
o1.afficher_infos()    

    
 
