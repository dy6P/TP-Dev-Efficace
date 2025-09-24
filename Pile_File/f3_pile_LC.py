##########################################
# TP dev efficace semaine 1              #
# implementation pile par liste chaînée  #
##########################################



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



class Pile:
    def __init__(self):
        """création d'une pile vide
        """
        self.sommet = None #le haut de la pile

    def est_vide(self):
        """retourne True si la pile est vide"""
        return self.sommet is None

    def empiler(self, x):
        """Empile une valeur x au sommet de la pile"""
        c = Cellule(x, self.sommet)
        self.sommet = c

    def depiler(self):
        """Dépile retourne la dernière valeur qui a été empilé"""
        if self.est_vide():
            raise Exception("La pile est vide !")
        v = self.sommet.suivante
        self.sommet = v
        return v


class TestPile(unittest.TestCase):

    def test_vide(self):
        p1 = Pile()
        p2 = Pile()
        p1.empiler(5)
        self.assertTrue(p2.est_vide())
        self.assertFalse(p1.est_vide())

    def test_depiler(self):
        p = Pile()
        for n in range(10):
            with self.assertRaises(BaseException):
                p.depiler()
            for i in range(n // 2):
                p.empiler(i)
            for i in range(n // 2):
                self.assertEqual(p.depiler(), n // 2 - 1 - i)

    def test_scenario_complet(self):
        p = Pile()
        self.assertTrue(p.est_vide())
        for i in range(5):
            p.empiler(i)
        with self.assertRaises(BaseException):
            p.empiler(0)
        self.assertEqual(p.depiler(), 4)
        self.assertEqual(p.depiler(), 3)
        self.assertEqual(p.depiler(), 2)
        p.empiler(5)
        p.empiler(6)
        self.assertEqual(p.depiler(), 6)
        self.assertEqual(p.depiler(), 5)
        self.assertEqual(p.depiler(), 1)
        self.assertEqual(p.depiler(), 0)
        with self.assertRaises(BaseException):
            p.depiler()


if __name__ == '__main__':
    unittest.main()

