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
        






h1.age = 26
assert h1.age == 26

try:
    h1.age = -5
    assert False, "une ValueError aurait du etre levee"
except ValueError:
    pass