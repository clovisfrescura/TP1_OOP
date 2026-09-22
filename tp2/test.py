import unittest
from heritage import Adulte, Enfant
from village import Village

#test question 1 : pour testhabitant

class TestHabitant(unittest.TestCase):
    """Tests pour la classe Habitant (via Adulte, car Habitant est abstraite) et l'encapsulation"""

    def setUp(self):
        self.adulte = Adulte("Dupont", "Marie", 35, "Rue A")

    def test_compte_animal_present(self):
        """Cas usuel : l'habitant possède l'animal demandé"""
        self.adulte.set_animaux({"vaches": 3})
        self.assertEqual(self.adulte.compte_animal("vaches"), 3)

    def test_compte_animal_absent(self):
        """Cas limite : l'animal n'est pas possédé, doit renvoyer 0"""
        self.assertEqual(self.adulte.compte_animal("moutons"), 0)

    def test_age_setter_valide(self):
        """Cas usuel : affectation d'un âge valide"""
        self.adulte.age = 40
        self.assertEqual(self.adulte.age, 40)

    def test_age_setter_invalide(self):
        """Cas limite : âge négatif, doit lever ValueError"""
        with self.assertRaises(ValueError):
            self.adulte.age = -5

#test question 2 : pour testvillage

class TestVillage(unittest.TestCase):
    """Tests pour la classe Village """

    def setUp(self):
        self.village = Village("PyTown")

    def test_ajouter_habitant_composition(self):
        """Cas usuel : le village crée et possède son propre habitant"""
        self.village.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})
        habitants = self.village.get_habitants()

        self.assertEqual(len(habitants), 1)
        self.assertEqual(habitants[0].get_nom(), "Aldric")

    def test_ajouter_habitant_agregation(self):
        
        elise = Adulte("Martin", "Elise", 28, "Rue B")
        autre_village = Village("VillageVoisin")

        self.village.ajouter_habitant_agregation(elise)
        autre_village.ajouter_habitant_agregation(elise)

        self.assertIn(elise, self.village.get_habitants())
        self.assertIn(elise, autre_village.get_habitants())

#test question 3 : pour testheritage

class TestHeritage(unittest.TestCase):
    """Tests pour l'héritage Adulte / Enfant et le calcul de la retraite"""

    def test_calcul_retraite_adulte(self):
        """Cas usuel : un adulte de 35 ans a 27 ans avant la retraite 62 - 35)"""
        adulte = Adulte("Dupont", "Marie", 35, "Rue A")
        self.assertEqual(
            adulte.calcul_nombre_annee_avant_retraite(),27)

    def test_calcul_retraite_enfant(self):
        """Cas usuel : un enfant ne peut pas calculer sa retraite (message d'erreur attendu)"""
        enfant = Enfant("Martin", "Lucas", 12, "Rue B")
        self.assertIn("enfant", enfant.calcul_nombre_annee_avant_retraite() )

    def test_enfant_age_invalide(self):
        """Cas limite : un Enfant de 20 ans (>= 18) doit lever une ValueError à la création"""
        with self.assertRaises(ValueError):
            Enfant("Oups", "Test", 20, "Rue C")


if __name__ == "__main__":
    unittest.main(verbosity=2)
