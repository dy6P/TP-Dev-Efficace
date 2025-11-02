########################################
# TP dev efficace semaine 2            #
# TRIS                                 #
########################################


import itertools
import unittest
from collections import deque


def fusion_croissante(tab1, tab2):
    """renvoie un tableau croissant, résultat de la fusion
    des tableaux croissants tab1 et tab2

    Args:
        tab1 (list): tableaux croissant
        tab2 (list): tableaux croissant

    Returns:
        list : nouveau tableau croissant
    """

    n1, n2 = len(tab1), len(tab2)
    fusion = [None] * (n1 + n2)
    i1, i2 = 0, 0

    for i in range(n1 + n2):
        if i2 == n2 or (i1 < n1 and tab1[i1] <= tab2[i2]):
            fusion[i] = tab1[i1]
            i1 += 1
        else:
            fusion[i] = tab2[i2]
            i2 += 1
    return fusion


def tri_fusion(tab):
    """renvoie un nouveau tableau, qui est tab trié dans l'ordre croissant

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : tri de tab
    """
    n = len(tab)

    if n <= 1:
        return tab

    m = n // 2
    tab1 = tri_fusion(tab[:m])
    tab2 = tri_fusion(tab[m:])
    return fusion_croissante(tab1, tab2)


def fusion_iterative(tab):
    """renvoie un nouveau tableau, qui est tab trié dans l'ordre croissant
    version itérative de la fusion

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : tri de tab
    """
    if len(tab) == 0:
        return []

    sous_tableaux = deque([i] for i in tab)

    while (len(sous_tableaux) > 1):
        tab1 = sous_tableaux.popleft()
        tab2 = sous_tableaux.popleft()
        fusion = fusion_croissante(tab1, tab2)
        sous_tableaux.append(fusion)

    return sous_tableaux[0]


def fusion_iterative_erronee(tab):
    """idem avec une PILE au lieu de la file
    """
    if len(tab) == 0:
        return []

    sous_tableaux = deque([i] for i in tab)

    while (len(sous_tableaux) > 1):
        tab2 = sous_tableaux.popleft()
        tab1 = sous_tableaux.popleft()
        fusion = fusion_croissante(tab1, tab2)
        sous_tableaux.appendleft(fusion)  # ici l'erreur

    return sous_tableaux[0]


def sous_tableaux_monotones(tab):
    """renvoie une deque des sous-tableaux monotones qui constituent tab
    inverse les sous-tableaux décroissants

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        deque :  de list (sous-tableaux)
    """

    sous_tableaux = deque()  # contiendra les sous-tableaux monotones
    d = 0  # la plage monotone en construction va de debut à fin (inclus) si debut <= fin

    for f in range(len(tab)):

        # cas où le sous-tableau se termine
        if (f - d >= 2) and \
                not ((tab[f] >= tab[f - 1] >= tab[f - 2]) or \
                     (tab[f] <= tab[f - 1] <= tab[f - 2])):
            suite = tab[d:f]
            if len(suite) >= 2 and suite[-1] < suite[0]:
                suite.reverse()
            sous_tableaux.append(suite)
            d = f

    # cas du dernier sous tableau
    suite = tab[d:]
    if len(suite) >= 2 and suite[-1] < suite[0]:
        suite.reverse()
    sous_tableaux.append(suite)
    return sous_tableaux


def sous_tableaux_monotones2(tab):
    """renvoie une deque des sous-tableaux monotones qui constituent tab
    inverse les sous-tableaux décroissants

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        deque :  de list (sous-tableaux)
    """

    sous_tableaux = deque()  # contiendra les sous-tableaux monotones
    d = 0  # la plage monotone en construction va de debut à fin (inclus) si debut <= fin
    variation = 0  # 0 ou  1 : croissant, 0 ou -1 : décroissant

    for f in range(len(tab) + 1):

        # cas où le sous-tableau continue dans la même variation
        if f < len(tab):
            if f > d and variation >= 0 and tab[f] >= tab[f - 1]:
                variation = 1
                continue
            if f > d and variation <= 0 and tab[f] <= tab[f - 1]:
                variation = -1
                continue
            if f == d:
                continue

        # cas où le sous-tableau est terminé
        suite = tab[d:f]
        if len(suite) >= 2 and variation == -1:
            suite.reverse()
            sous_tableaux.append(suite)
            d = f
            variation = 0

    return sous_tableaux


def timsort(tab):
    """renvoie un nouveau tableau, qui est tab trié dans l'ordre croissant
    procède itérativement comme la fusion en utilisant les sous-tableaux monotones

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : tri de tab
    """
    if len(tab) == 0:
        return []

    sous_tableaux = sous_tableaux_monotones(tab)

    while (len(sous_tableaux) > 1):
        tab2 = sous_tableaux.popleft()
        tab1 = sous_tableaux.popleft()
        fusion = fusion_croissante(tab1, tab2)
        sous_tableaux.append(fusion)

    return sous_tableaux[0]


class TestFusion(unittest.TestCase):

    def test_fusion_croissante(self):

        tab0 = fusion_croissante([1, 2], [1, 2, 3])
        self.assertEqual(tab0, [1, 1, 2, 2, 3])

        tab0 = fusion_croissante([], [1, 2, 3])
        self.assertEqual(tab0, [1, 2, 3])

        tab0 = fusion_croissante([], [1, 2, 3])
        self.assertEqual(tab0, [1, 2, 3])

        tab0 = fusion_croissante([], [])
        self.assertEqual(tab0, [])

        tab0 = fusion_croissante([3, 3, 3], [2, 2])
        self.assertEqual(tab0, [2, 2, 3, 3, 3])

        tab0 = fusion_croissante([1, 2, 3, 4, 5], [6])
        self.assertEqual(tab0, [1, 2, 3, 4, 5, 6])

        tab0 = fusion_croissante([4, 5, 6], [1, 2, 3])
        self.assertEqual(tab0, [1, 2, 3, 4, 5, 6])

        # à compléter !

    def test_tri_fusion(self):
        # on va tester sur tous les ordres possibles pour N de 1 à 12
        for N in range(10):
            croissante = list(range(N))
            for p in itertools.permutations(croissante):
                a_trier = list(p)
                a_trier = tri_fusion(a_trier)
                self.assertEqual(a_trier, croissante)

    def test_tri_fusion_iteratif(self):
        # on va tester sur tous les ordres possibles pour N de 1 à 8
        for N in range(1, 8):
            croissante = list(range(N))
            for p in itertools.permutations(croissante):
                a_trier = list(p)
                a_trier = fusion_iterative(a_trier)
                self.assertEqual(a_trier, croissante)

    def test_sous_tableaux_mononotes(self):
        self.assertEqual(sous_tableaux_monotones([1, 2, 3]), deque([[1, 2, 3]]))
        self.assertEqual(sous_tableaux_monotones([3, 2, 1]), deque([[1, 2, 3]]))
        self.assertEqual(sous_tableaux_monotones([1, 2, 3, 2, 1]), deque([[1, 2, 3], [1, 2]]))
        self.assertEqual(sous_tableaux_monotones([1, 2, 3, 1, 2]), deque([[1, 2, 3], [1, 2]]))
        self.assertEqual(sous_tableaux_monotones([1, 2, 3, 2, 3, 4, 3, 2, 4, 5, 1]),
                         deque([[1, 2, 3], [2, 3, 4], [2, 3], [4, 5], [1]]))

    def test_timsort(self):
        # on va tester sur tous les ordres possibles pour N de 1 à 8
        for N in range(0, 8):
            croissante = list(range(N))
            for p in itertools.permutations(croissante):
                a_trier = list(p)
                a_trier = timsort(a_trier)
                self.assertEqual(a_trier, croissante)


if __name__ == '__main__':
    unittest.main()