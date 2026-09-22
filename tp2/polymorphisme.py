class Habitant:
    def __init__(self, nom : str, age : int, adresse : str, animaux : dict = None):
        self.nom = nom
        self.age = age 
        self.adresse = adresse
        self.animaux = animaux if animaux is not None else {}

    def affichage_adresse (self) : 
        print(f"{self.nom} habite à {self.adresse}" )

    def compte_animal(self, animal):
        return self.animaux.get(animal, 0)

    def __str__(self):
        return f"{self.prenom} {self.nom}, {self.age} ans, habite à {self.adresse}"

    def affichage(h: Habitant):
        """Fonction qui affiche """
        print(str(h))

#en reandant la méthode abstraite on oblige chaque sous classe à l'implémenter
#ce qui garantie que le polymorphisme evite les comportements innatendus

