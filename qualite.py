

#il faudrait nommer les noms des differents parametres de la fonction pour qu'ils soient plus explicites, 
#avec des types comme int ou float par exemple pour des variables comme 
#tel que d,t,x1 etc ....

#le paramètre d n'est jamais utilisé dans le corps de la conftion 


#la fonction print est mal placé au sein de la fonction de calcul est mal placé,
#il risque d avoir un probleme avec l'effet de bord

cout_unitaire = {
    "route": 1.0,
    "herbe":1.5,
    "sable":2.0, 
}

cout_unitaire_defaut =  3.0

def cout_deplacement_propre(terrain, x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    facteur = {

        "R": cout_unitaire["route"],
        "H": cout_unitaire["herbe"],
        "S": cout_unitaire["sable"],

    }.get(terrain, cout_unitaire_defaut)

    return distance * facteur