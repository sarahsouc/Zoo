
from animal import Animal

class Serpent(Animal):

    def __init__(self, nom, poids, taille):
        super().__init__(nom, poids, taille)  
                   
    def se_deplacer(self):
        return "Je rampe"

