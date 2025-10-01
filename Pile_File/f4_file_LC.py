###########################################
# TP dev efficace semaine 1               #
# implementation file FIFO liste chaînée  #
###########################################



import unittest


class Cellule:
    def __init__(self, valeur, suivante):
        """création d'une cellule

        Args:
            valeur (quelconque): la valeur à stocker dans la cellule
            suivante (Cellule): la cellule suivante de la liste chaînée
        """
        self.valeur = valeur
        self.suivante = suivante

class File_LC:
    def __init__(self):
        """création file vide
        """
        self.entree = None #dernier maillon de la liste, où on fait les ajouts
        self.sortie = None #premier maillon de la lis
        # te, prêt à sortir

    def est_vide(self):
        """retourne True si la file est vide"""
        return self.sortie is None

    def enfiler(self, x):
        """Enfile un élément x à l'entrée de la file"""
        if self.entree is None:
            self.entree = Cellule(x, None)
            self.sortie = self.entree
        else:
            c = Cellule(x, None)
            self.entree.suivante = c
            self.entree = c

    def defiler(self):
        """Défiler un élément x à la sortie de la file"""
        if self.est_vide():
            raise Exception("La file est vide !")
        sortie = self.sortie
        self.sortie = self.sortie.suivante
        return sortie


class TestFile_LC(unittest.TestCase):

    def test_vide(self):
        f = File_LC()
        self.assertTrue(f.est_vide())
        f.enfiler(10)
        self.assertFalse(f.est_vide())

    def test_enfiler_defiler(self):
        f = File_LC()
        valeurs = [1, 2, 3, 4, 5]
        for v in valeurs:
            f.enfiler(v)
        for v in valeurs:
            cellule = f.defiler()
            self.assertEqual(cellule.valeur, v)
        with self.assertRaises(Exception):
            f.defiler()

    def test_scenario(self):
        f = File_LC()
        self.assertTrue(f.est_vide())
        f.enfiler(0)
        f.enfiler(1)
        self.assertEqual(f.defiler().valeur, 0)
        f.enfiler(2)
        f.enfiler(3)
        self.assertEqual(f.defiler().valeur, 1)
        self.assertEqual(f.defiler().valeur, 2)
        f.enfiler(4)
        f.enfiler(5)
        self.assertEqual(f.defiler().valeur, 3)
        self.assertEqual(f.defiler().valeur, 4)
        self.assertEqual(f.defiler().valeur, 5)
        self.assertTrue(f.est_vide())
        with self.assertRaises(Exception):
            f.defiler()


if __name__ == '__main__':
    unittest.main()