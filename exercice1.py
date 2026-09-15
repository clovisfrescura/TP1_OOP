
releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def afficher_releve(releves):
    for releve in releves:
        nom_capteur = releve[0]
        valeur = releve[1]
        unité = releve[2]
    return f" Capteur {nom_capteur} : {valeur} {unité}" #faire attention à ne pas mettre de print 

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

def recalibrer(releves, nom_capteur, nouvelle_taille):
    for i in range(len(releves)):
        if releves[i][0] == "laser_avant":
            releve_liste = list(releves[i]) # reconversion du tuple en liste
        releve_liste[1] = releve_liste[1] + 0.05 # modification de la taille
        releves[i] = tuple(releve_liste) # Recréation du tuple avec nouvelle taille 
    return releves

nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)

assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3
