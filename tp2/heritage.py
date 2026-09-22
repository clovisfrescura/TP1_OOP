from abc import ABC, abstractmethod

class Habitant:
    def __init__(self, nom : str, age : int, adresse : str, animaux : dict = None):
        self.__nom = nom
        self.__age = age 
        self.__adresse = adresse
        self.__animaux = animaux if animaux is not None else {}

    #accesseur pour la fonction

    def get_nom (self) -> str : 
        return self.__nom

    def get_age(self) -> int :
        return self.__age

    def get_adresse(self) :
        self.__adresse

    def get_animaux ( self ) :
        self.__animaux 

    #mutateur pour la fonction

    def set_nom (self, nom):
        self.__nom = nom

    def set_age(self, age):
        self.__age = age

    def set_adresse(self, adresse):
        self.__adresse = adresse

    def set_animaux(self, animaux):
        self.__animaux = animaux

    def affichage_adresse (self) : 
            print(f"{self.__nom} habite à {self.__adresse}" )
    
    def compte_animal(self, animal):
        return self.__animaux.get(animal, 0)

    @property
    def age(self, age):
        return self.__age

    @age.setter
    def age(self, valeur):
        if valeur < 0 or valeur > 130 :
            raise ValueError(" l'age doit etre compris entre 0 et 130") 
        self.__age = valeur 

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self) : 

class Adulte(Habitant):
    def __init__(self, nom, prenom, age):
        if age < 18:
            raise ValueError("Un adulte doit avoir au moins 18 ans")
        super().__init__(nom, prenom, age)

    def calcul_nombre_annee_avant_retraite(self):
        age_retraite = 62
        if self.age >= age_retraite:
            return "Déjà à la retraite"
        else:
            return age_retraite - self.age

class Enfant(Habitant):
    def __init__(self, nom, prenom, age):
        if age >= 18:
            raise ValueError("Un enfant doit avoir moins de 18 ans")
    super().__init__(nom, prenom, age)

    def calcul_nombre_annee_avant_retraite(self):
        return "Erreur: Un enfant ne peut pas calculer sa retraite"