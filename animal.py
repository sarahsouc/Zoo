
class Animal:
    
    def __init__(self, nom, poids, taille):
        self.__nom = nom
        self.__poids = poids
        self.__taille = taille
    
    @property
    def poids(self):
        return self.__poids
    
    @poids.setter
    def poids(self, new_poids):
        self.__poids = new_poids
    
   
    @property
    def taille(self):
        return self.__taille
    
    @taille.setter
    def taille(self, new_taille):
        self.__taille = new_taille

    
    @property
    def nom(self):
        return self.__nom
    
    @poids.setter
    def poids(self, new_nom):
        self.__nom = new_nom
    
    def __str__(self):
        return self.__nom + ", poids=" + str(self.__poids) + ", taille=" + str(self.__taille)
        

                
    def se_deplacer(self):
        return "Cela dépend de l'animal"

    
        
    





     
        






        
