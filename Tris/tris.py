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
    fusion = [None]*(n1+n2)    # tableau final
    i1, i2 = 0, 0  #prochains indices à insérer

    for i in range(n1+n2):
        if (n2 == i2) or (i1 < n1 and tab1[i1] < tab2[i2]):
            #insertion depuis le tableau 1
            fusion[i] = tab1[i1]
            i1 += 1
        else:
            #insertion depuis le tableau 2
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



def fusion_iterative(tab):
    """renvoie un nouveau tableau, qui est tab trié dans l'ordre croissant
    version itérative de la fusion

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : tri de tab
    """
    pass

def sous_tableaux_monotones(tab):
    """renvoie une liste des sous-tableaux monotones qui constituent tab
    
    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : liste de list (sous-tableaux)
    """

    pass

def timsort(tab):
    """renvoie un nouveau tableau, qui est tab trié dans l'ordre croissant
    procède itérativement comme la fusion en utilisant les sous-tableaux monotones

    Args:
        tab (list): un tableau d'éléments comparables

    Returns:
        list : tri de tab
    """

    pass


class TestFusion(unittest.TestCase):

    def test_fusion_croissante(self):

        tab0 = fusion_croissante([1,2],[1,2,3])
        tab1 = fusion_croissante([],[1,2,3])
        tab2 = fusion_croissante([1,2],[])
        tab3 = fusion_croissante([],[])
        tab4 = fusion_croissante([6,8,9],[1,2,3])
        tab5 = fusion_croissante([8,9],[1,2,3])
        print(tab0, tab1, tab2, tab3, tab4, tab5)
        self.assertEqual(tab0,[1,1,2,2,3])
        self.assertEqual(tab1,[1,2,3])
        self.assertEqual(tab2,[1,2])
        self.assertEqual(tab3,[])
        self.assertEqual(tab4,[1,2,3,6,8,9])
        self.assertEqual(tab5,[1,2,3,8,9])
            
    def test_tri_fusion(self):
        #on va tester sur tous les ordres possibles pour N de 1 à 8
        for N in range(8):
            croissante = list(range(N))
            for p in itertools.permutations(croissante):
                a_trier = list(p)
                a_trier = tri_fusion(a_trier)
                self.assertEqual(a_trier, croissante)

if __name__ == '__main__':
    unittest.main()
    