########################################
# TP dev efficace chapitre 4           #
# implementation d'une table de        #
# hachage simple avec chainage         #
# interne -- version sans suppression  #
########################################


import unittest


class TableHachageSimple:
    """Table de hachage avec sondage linéaire, sans suppression."""

    def __init__(self, N):
        self.N = N                      # taille fixe de la table
        self.table = [None] * N         # cases vides initialement
        self.nb_elements = 0

    def _hash(self, clé):
        """Fonction de hachage très simple."""
        return clé % self.N

    def inserer(self, clé):
        """Insère une clé (entier) dans la table."""
        pass

    def rechercher(self, clé):
        """Renvoie True si clé présente."""
        pass






    
class Test_Hachage(unittest.TestCase):
    """Tests pour la table de hachage simple sans suppression."""

    def setUp(self):
        self.t = TableHachageSimple(5)

    def test_insertion_et_recherche(self):
        self.t.inserer(10)
        self.t.inserer(15)
        self.t.inserer(20)
        self.assertTrue(self.t.rechercher(10))
        self.assertTrue(self.t.rechercher(15))
        self.assertTrue(self.t.rechercher(20))
        self.assertFalse(self.t.rechercher(99))

    def test_pas_de_double_insertion(self):
        self.t.inserer(10)
        self.t.inserer(10)
        self.assertEqual(self.t.nb_elements, 1)

    def test_table_pleine(self):
        for x in [1, 2, 3, 4, 5]:
            self.t.inserer(x)
        with self.assertRaises(RuntimeError):
            self.t.inserer(6)



if __name__ == "__main__":
    unittest.main()

