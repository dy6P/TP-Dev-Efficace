########################################
# TP dev efficace chapitre 4           #
# implementation d'un dictionnaire     #
# python par table de hachage avec     #
# chainage interne                     #
########################################


import unittest

class Dictionnaire:
    """Implémentation d'un dictionnaire semblable au dict de Python."""
    
    TAILLE_INITIALE = 8   # taille initiale de la table
    MAX_LOAD_FACTOR = 0.66 # seuil pour décider la réallocation, on doublera alors la table

    class Entrée:
        """Classe interne au Dicionnaire pour stocker
        une clé, sa valeur associée, son hash, et si la clé a été effacée."""
        
        def __init__(self, clé, valeur, h):
            self.clé = clé       # la clé 
            self.valeur = valeur   # la valeur associée
            self.hash = h        # le hash de la clé
            self.supprimé = False # tombstone

    def __init__(self):
        self.longueur = self.TAILLE_INITIALE
        self.nb_elements = 0       # nombre d'éléments valides
        self.table = [None] * self.longueur  # initialisation de la table en elle-même

    
    def prochain_indice_sondage(self, h):
        """Génère les indices de sondage pour un hash h."""
        mask = self.longueur - 1
        perturb = h
        i = h % self.longueur
        while True:
            yield i # itérateur qui prend une valur différente à chaque appel de la fonction
            i = (5 * i + 1 + perturb) % self.longueur
            perturb = perturb // 32


    def réallocation(self):
        """Double la table si le seuil de charge est dépassé."""
        ancienne_table = self.table
        self.longueur *= 2
        self.table = [None] * self.longueur
        self.nb_elements = 0
        for entrée in ancienne_table:
            if entrée and not entrée.supprimé:
                self[entrée.clé] = entrée.valeur  # ré-insertion


    def test_reallocation(self):
        return self.nb_elements / self.longueur > self.MAX_LOAD_FACTOR


        

    def __getitem__(self, clé):
        """fonction magique python pour la recherche de dico[clé]"""
        h = hash(clé)
        for i in self.prochain_indice_sondage(h):
            #TODO
            pass
            #chercher la clé jusqu'à la première case vide



        raise KeyError(clé)

    
    def __setitem__(self, clé, valeur):
        """fonction magique python pour le comportement de dico[clé] = valeur"""
        h = hash(clé)

        #réallocation nécessaire ?
        if self.test_reallocation():
            self.réallocation()


        #TODO 
        #insérer sur le premier indice avec case vide ou tombstone

        
        

    def __delitem__(self, clé):
        """fonction magique python pour la syntaxte  del dico[clé]"""
        h = hash(clé)
        for i in self.prochain_indice_sondage(h):
            #TODO
            #chercher la clé et la supprimer
            

        raise KeyError(clé)

    def __contains__(self, clé):
        """fonction magique python pour l'opérateur in """
        try:
            _ = self[clé]
            return True
        except KeyError:
            return False

    def __len__(self):
        """fonction magique python pour la fonction len """
        return self.nb_elements

    def keys(self):
        """renvoie la liste des clés"""
        return [e.clé for e in self.table if e and not e.supprimé]

    def values(self):
        """renvoie la liste des valeurs"""
        return [e.valeur for e in self.table if e and not e.supprimé]

    def items(self):
        """renvoie les couples clé,valeur"""
        return [(e.clé, e.valeur) for e in self.table if e and not e.supprimé]


class TestDico(unittest.TestCase):
    

    def setUp(self):
        self.d = Dictionnaire()


    # Tests d’insertion et récupération
    def test_insertion_et_recuperation(self):
        self.d["a"] = 1
        self.d["b"] = 2
        self.assertEqual(self.d["a"], 1)
        self.assertEqual(self.d["b"], 2)
        self.assertEqual(len(self.d), 2)


    # Test de mise à jour de clé déjà existante
    def test_mise_a_jour(self):
        self.d["x"] = 10
        self.d["x"] = 20
        self.assertEqual(self.d["x"], 20)
        self.assertEqual(len(self.d), 1)


    # Test de suppression (avec tombstone)
    def test_suppression(self):
        self.d["k1"] = "valeur"
        del self.d["k1"]
        self.assertNotIn("k1", self.d)
        self.assertEqual(len(self.d), 0)

        # Une nouvelle insertion doit pouvoir réutiliser la tombstone
        self.d["k1"] = "nouvelle"
        self.assertIn("k1", self.d)
        self.assertEqual(self.d["k1"], "nouvelle")


    # Test de recherche d’une clé absente
    def test_cle_absente(self):
        with self.assertRaises(KeyError):
            _ = self.d["inexistante"]


    # Test de réallocation automatique
    def test_reallocation(self):
        for i in range(20):  # au-delà du facteur de charge (load factor)
            self.d[f"clé{i}"] = i
        self.assertGreater(self.d.longueur, self.d.TAILLE_INITIALE)
        for i in range(20):
            self.assertEqual(self.d[f"clé{i}"], i)

        
    # Test des méthodes keys(), values(), items()
    def test_keys_values_items(self):
        couples = {"a": 1, "b": 2, "c": 3}
        for k, v in couples.items():
            self.d[k] = v
        self.assertCountEqual(self.d.keys(), ["a", "b", "c"])
        self.assertCountEqual(self.d.values(), [1, 2, 3])
        self.assertCountEqual(self.d.items(), [("a", 1), ("b", 2), ("c", 3)])


    # Test de l’opérateur "in"
    def test_in_operator(self):
        self.d["a"] = 1
        self.assertTrue("a" in self.d)
        self.assertFalse("b" in self.d)

    
    # Test scénario complet
        """Scénario complet : insertions, suppressions, réinsertions, réallocation, vérifications."""
        d = self.d

        # insertions initiale
        for i in range(10):
            d[f"clé{i}"] = i
        self.assertEqual(len(d), 10)


        # suppression de certaines clés
        for i in range(0, 10, 2):
            del d[f"clé{i}"]
        self.assertEqual(len(d), 5)
        for i in range(0, 10, 2):
            self.assertNotIn(f"clé{i}", d)
        for i in range(1, 10, 2):
            self.assertIn(f"clé{i}", d)


        # réinsertions 
        for i in range(0, 10, 2):
            d[f"clé{i}"] = i * 100
        self.assertEqual(len(d), 10)

        # Vérifie que les valeurs mises à jour sont correctes
        for i in range(10):
            attendu = i * 100 if i % 2 == 0 else i
            self.assertEqual(d[f"clé{i}"], attendu)

        # force une réallocation (en ajoutant beaucoup d’éléments)
        for i in range(10, 50):
            d[f"clé{i}"] = i
        self.assertGreater(d.longueur, 8)  # la taille initiale était 8

        # Vérifie la cohérence après réallocation
        for i in range(50):
            attendu = i * 100 if i % 2 == 0 and i < 10 else i
            self.assertEqual(d[f"clé{i}"], attendu)

        # suppression complète
        for i in range(50):
            del d[f"clé{i}"]
        self.assertEqual(len(d), 0)

        # Réinsertion après nettoyage
        for i in range(5):
            d[f"x{i}"] = i
        self.assertEqual(len(d), 5)
        for i in range(5):
            self.assertEqual(d[f"x{i}"], i)

        # Vérifie la cohérence finale
        self.assertCountEqual(d.keys(), [f"x{i}" for i in range(5)])

if __name__ == '__main__':
    unittest.main()