from collections import deque

# 1) Comprendre la classe arbre binaire

Valeur = str | int | float  # valeurs des noeuds


class Noeud:
    def __init__(self, valeur: Valeur, fils_gauche: "Arbre_Binaire", fils_droit: "Arbre_Binaire"):
        """Initialise le Noeud

        Args:
            valeur (Valeur): la valeur stockée dans le noeud
            fils_gauche (Arbre_Binaire): fils gauche du noeud
            fils_droit (Arbre_Binaire): fils droit du noeuf
        """
        self.valeur: Valeur = valeur
        self.fils_gauche: "Arbre_Binaire" = fils_gauche  # (Arbre_binaire ou None)
        self.fils_droit: "Arbre_Binaire" = fils_droit  # (Arbre_binaire ou None)


Arbre_Binaire = Noeud | None

# 2) Créez à la main un abre contenant les valeurs (oui c'est pénible mais faut savoir le faire)
"""
         'A'
     'B'     'C'        
  'D'  'E'  . 'F'
'G' . 'H'.    .  'I'
. .   . .        . .
le . signifie qu'il n'y a pas de fils
"""


# voir dans le main


# 3) complétez les 3 fonctions d'affichage et testez

def affiche_ordre_prefixe(arbre: Arbre_Binaire) -> None:
    """affiche les valeurs de l'arbre dans l'ordre préfixe

    Args:
        arbre (Arbre_Binaire)
    """
    if arbre is not None:
        print(arbre.valeur, end=" ")
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
        print(arbre.valeur, end=" ")


def affiche_ordre_infixe(arbre: Arbre_Binaire) -> None:
    """affiche les valeurs de l'arbre dans l'ordre infixe

    Args:
        arbre (Arbre_Binaire)
    """
    if arbre:
        affiche_ordre_infixe(arbre.fils_gauche)
        print(arbre.valeur, end=" ")
        affiche_ordre_infixe(arbre.fils_droit)


# 4) et le parcours en largeur ?

def affiche_ordre_largeur(arbre: Arbre_Binaire) -> None:
    """affiche les valeurs de l'arbre dans l'ordre en largeur

    Args:
        arbre (Arbre_Binaire)
    """
    if arbre is None:
        return
    attente: deque[Noeud] = deque()
    attente.append(arbre)
    while attente:
        courant: Noeud = attente.popleft()
        print(courant.valeur, end=" ")
        if courant.fils_gauche:
            attente.append(courant.fils_gauche)
        if courant.fils_droit:
            attente.append(courant.fils_droit)


# 5) Complétez les fonctions:

def nb_noeuds(arbre: Arbre_Binaire) -> int:
    """renvoie le nombre de noeuds dans l'arbre

    Args:
        arbre (Arbre_Binaire)

    Returns:
        int: le nombre de noeuds de l'arbre
    """
    if arbre is None:
        return 0
    else:
        return 1 + nb_noeuds(arbre.fils_gauche) + nb_noeuds(arbre.fils_droit)


def hauteur_arbre(arbre: Arbre_Binaire) -> int:
    """Renvoie la hauteur de l'arbre.

    Args:
        arbre (Arbre_Binaire): 

    Returns:
        int: la hauteur de l'arbre
    """
    if arbre is None or (arbre.fils_gauche is None and arbre.fils_droit is None):
        return 0
    else:
        return 1 + max(hauteur_arbre(arbre.fils_gauche), hauteur_arbre(arbre.fils_droit))


def max_valeurs_arbre(arbre: Arbre_Binaire) -> Valeur:
    if arbre is None:
        raise Exception("L'arbre est vide.")
    else:
        maxi: Valeur = arbre.valeur
        if arbre.fils_gauche is not None:
            maxi = max(maxi, max_valeurs_arbre(arbre.fils_gauche))
        if arbre.fils_droit is not None:
            maxi = max(maxi, max_valeurs_arbre(arbre.fils_droit))
        return maxi


# 6) complétez cette fonction qui convertit un arbre binaire en un tableau
# reponse pour l'arbre ci-dessus [None,'A','B','C','D','E',None,'F','G',None,'H',None,None,none,'I']


def arbre_binaire_vers_tableau(arbre: Arbre_Binaire) -> list[Valeur | None]:
    """convertit un arbre binaire en tableau

    Args:
        arbre (Arbre_Binaire): l'arbre à convertir 

    Returns:
        list[Valeur] : le tableau correspondant
    """

    def etape(arbre: Arbre_Binaire, tab: list[Valeur | None], i: int) -> None:
        """fonction auxiliaire, écrit dans tab le sous-arbre arbre donné en mettant sa
        racine à l'indice i

        Args:
            arbre (Arbre_Binaire): arbre (noeud)
            tab (list): le tableau dans lequel on écrit
            i (int): l'indice où commencer à écrire
        """
        if arbre:
            tab[i] = arbre.valeur
            etape(arbre.fils_gauche, tab, 2 * i)
            etape(arbre.fils_droit, tab, 2 * i + 1)

    # initialisation du tableau à la bonne taille
    tab = [None] * (2 ** (hauteur_arbre(arbre) + 1))
    etape(arbre, tab, 1)
    return tab


# abis = Arbre_binaire(1,None,Arbre_binaire(2,None,Arbre_binaire(3,None,None)))
# print("**",arbre_binaire_vers_tableau(abis))


# 6.5) Et l'inverse ?

def tableau_vers_arbre_binaire(tab: list[Valeur | None], racine: int = 1) -> Arbre_Binaire:
    """convertit un tableau (encodant un AB) en structure Arbre_Binaire

    Args:
        tab (list[Maybe_Valeur]): tableau encodant un AB
        racine (int, optional): l'indice du tableau dans lequel écrire le noeud racine. Defaults to 1.

    Returns:
        Arbre_Binaire: correspondant au tableau
    """

    if racine >= len(tab):
        return None
    elif tab[racine] is None:
        return None
    else:
        val = tab[racine]
        if isinstance(val, (str, int, float)):
            fg = tableau_vers_arbre_binaire(tab, 2 * racine)
            fd = tableau_vers_arbre_binaire(tab, 2 * racine + 1)
            return Noeud(val, fg, fd)


################################################
# Application : expressions arithmétiques      #
################################################

"""
On stocke dans un arbre binaire des expressions comme 2 + 5*(7+5)
Les noeuds internes de l'arbre une une valeur '+' ou '-' ou '*' ou '/' (division entière //)
Les feuilles contiennent des entiers.
"""
# 7) Créer l'arbre binaire correspondant à 2 + 5*(1 + 10/(7-3))

a2 = Noeud('+', Noeud(2, None, None),
           Noeud('*', Noeud(5, None, None),
                 Noeud('+', Noeud(1, None, None),
                       Noeud('/', Noeud(10, None, None),
                             Noeud('-', Noeud(7, None, None), Noeud(3, None, None))))))


# 8) Ecrire une fonction qui évalue la valeur d'un arbre binaire d'expression arithmétique

def evaluer(arbre: Arbre_Binaire) -> Valeur | None:
    # si c'est un int on renvoie la valeur directement
    if arbre is None:
        return None
    elif arbre.fils_gauche is None or arbre.fils_droit is None:
        return arbre.valeur
    else:
        val_g = evaluer(arbre.fils_gauche)
        val_d = evaluer(arbre.fils_droit)

        if val_g is None or val_d is None:
            raise Exception("Arbre mal formé :" + (str(arbre.valeur)))
        # On s'assure d'avoir deux int
        if not (isinstance(val_g, int) and isinstance(val_d, int)):
            raise Exception("Problème de valeurs non entières :" + (str(arbre.valeur)))

        if arbre.valeur == '+':
            return val_g + val_d
        if arbre.valeur == '*':
            return val_g * val_d
        if arbre.valeur == '-':
            return val_g + val_d
        if arbre.valeur == '/':
            return val_g // val_d


# 9) Si vous êtes en forme, écrivez une fonction qui parse une str comme "2 + 5*(1 + (10//(7-3)))" et crée l'arbre binaire associé
# La grammaire des expressions est
# E <- int
# E <- (E op E) avec op un des 4 opérateurs

def afficher_prefixe(arbre: Arbre_Binaire, p: int = 0) -> None:
    """affiche l'arbre en parcours prefixe avec des indentations"""
    if arbre:
        print("  " * p + str(arbre.valeur))
        afficher_prefixe(arbre.fils_gauche, p + 1)
        afficher_prefixe(arbre.fils_droit, p + 1)


def parser(s: str) -> Arbre_Binaire:
    """renvoie l'arbre binaire associé à l'expression"""
    if s == "":
        return None

    s = s.strip()

    # si c'est un entier
    if s.isdigit():
        return Noeud(int(s), None, None)
    # sinon :
    # on vire les parenthèses extérieures
    s = s[1:-1]
    # on cherche un opérateur qui n'est pas entre des parenthèses
    p = 0  # compteur de parentheses
    op = ""
    i = -1
    for i in range(len(s)):
        if s[i] == '(':
            p += 1
        elif s[i] == ')':
            p -= 1
        elif s[i] in ['+', '-', '*', '/'] and p == 0:
            op = s[i]
            break
    if op:
        s1 = s[:i].strip()
        s2 = s[i + 1:].strip()

        return Noeud(op, parser(s1), parser(s2))
    else:
        print("erreur :", s)
        raise Exception("pb de structure")


if __name__ == "__main__":
    fg = Noeud('G', None, None)
    fh = Noeud('H', None, None)
    fi = Noeud('I', None, None)

    a1 = Noeud('A', Noeud('B', Noeud('D', fg, None), Noeud('E', fh, None)), Noeud('C', None, Noeud('F', None, fi)))

    print("\nAffichage préfixe :")
    affiche_ordre_prefixe(a1)
    print("\nAffichage suffixe :")
    affiche_ordre_suffixe(a1)
    print("\nAffichage infixe :")
    affiche_ordre_infixe(a1)
    print("\nAffichage parcours en largeur")
    affiche_ordre_largeur(a1)
    print("\nNombre de noeuds :")
    print(nb_noeuds(a1))
    print("\nhauteur de l'arbre :", hauteur_arbre(a1))
    print("maxi arbre :", max_valeurs_arbre(a1), "\n")

    tab1 = arbre_binaire_vers_tableau(a1)
    print("tableau", tab1)
    print(affiche_ordre_largeur(tableau_vers_arbre_binaire(tab1)))

    print("\n\nArbre pour 2 + 5*(1 + 10/(7-3))")

    print("Préfixe :")

    afficher_prefixe(a2)

    print("résultat évaluation :", evaluer(a2))

    print("\nTest parseur")

    s2 = "((2 + 5)*(4-1))"
    print(s2, "=", evaluer(parser(s2)))

    s3 = "((((2*(2+8))+1)*3)-(10+10))"
    print(s3, "=", evaluer(parser(s3)))
