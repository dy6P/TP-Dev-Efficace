########################################
# TP dev efficace chapitre 4           #
# implementation d'une table de        #
# hachage simple avec chainage         #
# interne -- version avec suppression  #
########################################

import unittest


class TableHachageSimple:
    """Table de hachage avec sondage linéaire et suppression (tombstones)."""

    # On marque les cases supprimées avec "T" pour Tombstone

    def __init__(self, N):
        self.N = N
        self.table = [None] * N
        self.nb_elements = 0

    def _hash(self, clé):
        return clé % self.N

    def inserer(self, clé):
        if self.nb_elements >= self.N:
            raise RuntimeError("Table pleine")

        # on fait la recherche en premier
        # un peu plus long mais plus simple
        if self.rechercher(clé):
            return

        h = self._hash(clé)

        for i in range(self.N):
            j = (h + i) % self.N
            if self.table[j] is None or self.table[j] == 'T':
                # case libre
                self.table[j] = clé
                self.nb_elements += 1
                return
        raise RuntimeError("Table saturée")

    def rechercher(self, clé):
        h = self._hash(clé)
        for i in range(self.N):
            j = (h + i) % self.N
            v = self.table[j]
            if v is None:
                return False
            if v == clé:
                return True
        return False

    def supprimer(self, clé):
        """Marque la case comme supprimée  avec 'T' (tombstone)."""
        h = self._hash(clé)
        for i in range(self.N):
            j = (h + i) % self.N
            v = self.table[j]
            if v is None:
                raise KeyError(clé)
            if v == clé:
                self.table[j] = 'T'
                self.nb_elements -= 1
                return
        raise KeyError(clé)


class Test_TableHachage_Avec_Suppression(unittest.TestCase):
    """Tests pour la table de hachage avec suppression et tombstones."""

    def setUp(self):
        self.t = TableHachageSimple(7)

    def test_insertion_et_recherche(self):
        self.t.inserer(10)
        self.t.inserer(20)
        self.t.inserer(5)
        self.assertTrue(self.t.rechercher(10))
        self.assertTrue(self.t.rechercher(5))
        self.assertFalse(self.t.rechercher(99))

    def test_suppression(self):
        self.t.inserer(10)
        self.t.inserer(17)  # collision (17 % 7 == 3, 10 % 7 == 3)
        self.assertTrue(self.t.rechercher(17))
        self.t.supprimer(10)
        self.assertFalse(self.t.rechercher(10))
        self.assertTrue(self.t.rechercher(17))  # doit rester accessible

    def test_reinsertion_tombstone(self):
        self.t.inserer(3)
        self.t.supprimer(3)
        self.assertFalse(self.t.rechercher(3))
        self.t.inserer(10)  # doit réutiliser la tombstone
        self.assertTrue(self.t.rechercher(10))

    def test_suppression_inexistante(self):
        with self.assertRaises(KeyError):
            self.t.supprimer(42)

    def test_table_pleine(self):
        for x in [1, 2, 3, 4, 5, 6, 7]:
            self.t.inserer(x)
        with self.assertRaises(RuntimeError):
            self.t.inserer(8)

    def test_scenario_complet(self):
        """Scénario pédagogique complet."""
        éléments = [10, 20, 30, 40, 50]
        for x in éléments:
            self.t.inserer(x)

        # Vérification
        for x in éléments:
            self.assertTrue(self.t.rechercher(x))

        # Suppressions
        for x in [20, 40]:
            self.t.supprimer(x)
            self.assertFalse(self.t.rechercher(x))

        # Réinsertion d’un élément qui entre en collision avec un tombstone
        self.t.inserer(27)  # collision avec 20 supprimé
        self.assertTrue(self.t.rechercher(27))

        # Vérification finale
        actifs = [x for x in éléments if x not in (20, 40)] + [27]
        for x in actifs:
            self.assertTrue(self.t.rechercher(x))


if __name__ == "__main__":
    unittest.main()