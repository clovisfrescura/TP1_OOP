class village :
    def __init__(self, nom) : 
        self.nom = nom
        self.habitant = []

    def ajouter_habitant_composition(self, nom, age, adresse, animaux = None):
        nouvel_habitant = habitant ( nom, age, adresse, animaux)
        self.habitant.append(nouvel_habitant)

    def ajouter_habitant_agregation(self, habitant):
        self.habitant.append(habitant)

    def afficher_habitants(self):
        for habitant in self.habitants:
            habitant.afficher_habitant()



#on peut voir que sur la fonction de composition cette derniere illustre bien le principe
#car on peut voir la relation forte, les objets sont liés
#tandis que pour la fonction d'agregation on observe bien que l'objet de la fonction
#peut etre utilise de maniere independante
