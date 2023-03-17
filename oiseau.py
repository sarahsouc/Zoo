
from animal import Animal

class Oiseau(Animal):

    def __init__(self,nom, poids, taille):
        super().__init__(nom, poids, taille)
        
    
    def se_deplacer(self):
        return "Je vole"

