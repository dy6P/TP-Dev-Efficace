
#1) Comprendre la classe arbre binaire

#1) Comprendre la classe arbre binaire

Valeur = str | int | float    # valeurs des noeuds

class Noeud:
    def __init__(self, valeur: Valeur , fils_gauche: "Arbre_Binaire", fils_droit: "Arbre_Binaire"):
        """Initialise le Noeud

        Args:
            valeur (Valeur): la valeur stockée dans le noeud
            fils_gauche (Arbre_Binaire): fils gauche du noeud
            fils_droit (Arbre_Binaire): fils droit du noeuf
        """
        self.valeur: Valeur  = valeur
        self.fils_gauche: "Arbre_Binaire" = fils_gauche  #(Arbre_binaire ou None)
        self.fils_droit: "Arbre_Binaire" = fils_droit    #(Arbre_binaire ou None)

Arbre_Binaire = Noeud | None


arbre1 = Noeud('A', Noeud('B', Noeud('D', Noeud('G', None, None), None), Noeud('E', Noeud('H', None, None), None)), Noeud('C', None, Noeud('F', None, Noeud('I', None, None))))
"""
         'A'
     'B'     'C'        
  'D'  'E'  . 'F'
'G' . 'H'.    .  'I'
le . signifie qu'il n'y a pas de fils
"""



#3) complétez les 3 fonctions d'affichage et testez

def affiche_ordre_prefixe(arbre: Arbre_Binaire) -> None:
    """affiche les valeurs de l'arbre dans l'ordre préfixe

    Args:
        arbre (Arbre_Binaire)
    """
    if arbre:
        print(arbre.valeur)
        affiche_ordre_prefixe(arbre.fils_gauche)
        affiche_ordre_prefixe(arbre.fils_droit)

def affiche_ordre_suffixe(arbre: Arbre_Binaire) -> None:
    """affiche les valeurs de l'arbre dans l'ordre suffixe

    Args:
        arbre (Arbre_Binaire)
    """
    if arbre:
        affiche_ordre_suffixe(arbre.fils_gauche)
        affiche_ordre_suffixe(arbre.fils_droit)
        print(arbre.valeur)

def affiche_ordre_infixe(arbre: Arbre_Binaire) -> None:
    """affiche les valeurs de l'arbre dans l'ordre infixe

    Args:
        arbre (Arbre_Binaire)
    """
    if arbre:
        affiche_ordre_infixe(arbre.fils_gauche)
        print(arbre.valeur)
        affiche_ordre_infixe(arbre.fils_droit)

#4) et le parcours en largeur ? Si vous vous en souvenez du cours de Graphes

def affiche_ordre_largeur(arbre: Arbre_Binaire) -> None:
    """affiche les valeurs de l'arbre dans l'ordre en largeur

    Args:
        arbre (Arbre_Binaire)
    """
    pass

#5) Complétez les fonctions:

def nb_noeuds(arbre: Arbre_Binaire) -> int: 
    """renvoie le nombre de noeuds dans l'arbre

    Args:
        arbre (Arbre_Binaire)

    Returns:
        int: le nombre de noeuds de l'arbre
    """
    if arbre:
        return 1 + nb_noeuds(arbre.fils_gauche) + nb_noeuds(arbre.fils_droit)
    return 0

def hauteur_arbre(arbre: Arbre_Binaire) -> int:
    """Renvoie la hauteur de l'arbre.

    Args:
        arbre (Arbre_Binaire): 

    Returns:
        int: la hauteur de l'arbre
    """
    if arbre and (arbre.fils_gauche is not None or arbre.fils_droit is not None):
        return 1 + max(hauteur_arbre(arbre.fils_gauche), hauteur_arbre(arbre.fils_droit))
    return 0

def max_valeurs_arbre(arbre: Arbre_Binaire) -> Valeur:
    """Renvoie la plus grande valeur stockée dans l'arbre

    Args:
        arbre (Arbre_Binaire)

    Raises:
        Exception: si l'arbre est vide

    Returns:
        Valeur: le maximum
    """
    if arbre is None:
        raise Exception("L'arbre est vide.")
    else:
        maxi : Valeur = arbre.valeur
        if arbre.fils_gauche is not None:
            maxi = max(maxi, max_valeurs_arbre(arbre.fils_gauche))
        if arbre.fils_droit is not None:
            maxi = max(maxi, max_valeurs_arbre(arbre.fils_droit))
        return maxi

#6) complétez cette fonction qui convertit un arbre binaire en un tableau
#reponse pour l'arbre ci-dessus [None,'A','B','C','D','E',None,'F','G',None,'H',None,None,None,None,'I']

def arbre_binaire_vers_tableau(arbre: Arbre_Binaire) -> list[Valeur | None]:
    """convertit un arbre binaire en tableau

    Args:
        arbre (Arbre_Binaire): l'arbre à convertir 

    Returns:
        list[Valeur] : le tableau correspondant
    """
    pass

#6.5) Et l'inverse ?

def tableau_vers_arbre_binaire(tab: list[Valeur | None], racine: int = 1) -> Arbre_Binaire:
    """convertit un tableau (encodant un AB) en structure Arbre_Binaire

    Args:
        tab (list[Maybe_Valeur]): tableau encodant un AB
        racine (int, optional): l'indice du tableau dans lequel écrire le noeud racine. Defaults to 1.

    Returns:
        Arbre_Binaire: correspondant au tableau
    """
    pass

################################################
# Application : expressions arithmétiques      #
################################################

"""
On stocke dans un arbre binaire des expressions comme 2 + 5*(7+5)
Les noeuds internes de l'arbre une une valeur '+' ou '-' ou '*' ou '//'
Les feuilles ont pour valeur un entier
"""
#7) Créer l'arbre binaire correspondant à 2 + 5*(1 + 10//(7-3))


#8) Ecrire une fonction qui évalue la valeur d'un arbre binaire d'expression arithmétique


#9) Si vous êtes en forme, écrivez une fonction qui parse une str comme "2 + 5*(1 + 10//(7-3))" et crée l'arbre binaire associé

affiche_ordre_prefixe(arbre1)
print("\n")
affiche_ordre_suffixe(arbre1)
print("\n")
affiche_ordre_infixe(arbre1)
print("\n")
print(nb_noeuds(arbre1))
print("\n")
print(hauteur_arbre(arbre1))
print("\n")
print(max_valeurs_arbre(arbre1))
print("\n")
print(max_valeurs_arbre(arbre1))