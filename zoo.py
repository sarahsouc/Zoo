
import random


class Zoo:

    def __init__(self, list_animal):
        self.__list_animal = list_animal
    
    @property
    def list_animal(self):
        return self.__list_animal
    
    @list_animal.setter
    def set_list_animal(self, new_list_animal):
        self.__list_animal = new_list_animal

    def ajout_animal(self, new_list_animal):
        if isinstance(new_list_animal, list):
            self.__list_animal.extend(new_list_animal)
        else:
            self.__list_animal.append(new_list_animal)
    
    def __str__(self):
        return self.__nom + ", poids=" + str(self.__poids) + ", taille=" + str(self.__taille)
    

