

from animal import Animal
from serpent import Serpent
from oiseau import Oiseau
from zoo import Zoo

#Instancier la class Animal
animal = Animal("définir nom",50,100)
print(animal)

print("print attribut poids",animal.poids)
print("print attribut taille",animal.taille)
print("Déplacement animal:", animal.se_deplacer())

# Instancier la class Serpent
serpent = Serpent("serpent",40,20)
serpent1 = Serpent("serpent1",60,30)
serpent2 = Serpent("serpent2",60,120)
print("print attribut taille serpent", serpent.poids)
print("print attribut taille serpent", serpent.taille)
print("Déplacement Serpent:", serpent.se_deplacer())


# Instancier la class oiseau
oiseau = Oiseau("oiseau",12,120)
oiseau1 = Oiseau("oiseau1",30,50)
oiseau2 = Oiseau("oiseau2",25,80)
print("print attribut taille oiseau",oiseau.poids)
print("print attribut taille oiseau",oiseau.taille)
print("Déplacement Oiseau:", oiseau.se_deplacer())

#Encapsulation_private (protéger attributs)
# Puis accéder et modifier les attributs protégés
# getters(renvoie valeur)_setters(modifie valeur)

#liste de départ
list_animal_initial = [serpent, oiseau, oiseau1, serpent2]
#Définir liste animal
list_animal = [serpent, oiseau, oiseau1, serpent2]

#Créer instance zoo
zoo = Zoo(list_animal)

#Aficher la liste animal
print("Liste de départ",zoo.list_animal)

#Modifier ma liste animal en ajoutant la nouvelle liste
new_list_animal = [serpent1, oiseau2]
zoo.ajout_animal(new_list_animal)


#Afficher la nouvelle liste
print("nouvelle liste1", zoo.list_animal)

#Ajout d'un animal
zoo.ajout_animal(oiseau1)
#Afficher la nouvelle liste
print("nouvelle liste oiseau", zoo.list_animal)


#Remplacer la liste modifiée par la liste de départ
zoo.set_list_animal= list_animal_initial

#Afficher la liste de départ
print("liste de départ", zoo.list_animal)
print([mon_animal.__str__() for mon_animal in zoo.list_animal])










       

