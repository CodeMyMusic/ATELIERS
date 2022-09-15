#Liste qui va servir de test avec seulement des entiers
L = [20, 13, 15, 35, 32]
print(L)

def somme_boucle_basee_indices(L):
    """ Somme avec une boucle basée sur les indices
    Args:
        L de type liste
    Returns :
        La somme (int)
    """
    somme = int()
    for i in range(len(L)):
        somme += L[i]
    return somme

print("Somme avec une boucle basée sur les indices:", somme_boucle_basee_indices(L))

def somme_boucle_basee_elements(L):
    """ Calcule une somme avec une boucle basée sur les éléments
    Args:
        L de type liste
    Returns :
        La somme (int)
    """
    somme = int()
    for i in L:
        somme += i
    return somme

print("Somme avec une boucle basée sur les éléments:", somme_boucle_basee_elements(L))


def somme_boucle_while(L):
    """ Somme avec while
    Args:
        L de type liste
    Returns :
        La somme (int)
    """
    somme = int()
    n = 0
    while n < len(L):
        somme += L[n]
        n+=1
    return somme

print("Somme avec une boucle while:", somme_boucle_while(L))


"""
def test_excercice1():
    print("TEST SOMME")
    #texte liste vide
    print("Test liste vide:", somme([]))
    #test somme 11111
    S = [1, 10, 100, 1000, 10000]
    print("Test somme 11111 :", somme(S))

test_excercice1()
"""

def moyenne(L):
    """ Calcule la moyenne des valeurs de la liste
    Args:
        L de type liste
    Returns :
        La moyenne (float)
    """
    if len(L) == 0:
        return 0
    else:
        return somme_boucle_basee_elements(L) / len(L)

print("Moyenne des valeurs de la liste:", moyenne(L))


def nb_sup_boucle_basee_sur_indices(L, e):
    """ Calcule le nombre de valeurs strictement supérieures à e avec une boucle basée sur les indices
    Args:
        L de type liste
    Returns :
        Le nombre de valeurs supérieures à e (int)
    """
    ct = 0
    for i in range(len(L)):
        if L[i] > e:
            ct += 1
    return ct


def nb_sup_boucle_basee_elements(L, e):
    """ Calcule le nombre de valeurs strictement supérieures à e avec une boucle basée sur les éléments
    Args:
        L de type liste
    Returns :
        Le nombre de valeurs supérieures à e (int)
    """
    ct = 0
    for i in L:
        if i > e:
            ct += 1
    return ct

print("Nombres de valeurs de la liste stictement supérieures à 15:")
print("- avec boucle basée sur les indices:", nb_sup_boucle_basee_sur_indices(L, 15))
print("- avec boucle basée sur les éléments:", nb_sup_boucle_basee_elements(L, 15))

def moy_sup(L, e):
    """ Calcule la moyenne des valeurs stictement supérieures à e
    Args:
        L de type liste
    Returns :
        La moyenne des valeurs strictement supérieures à e (float)
    """
    #Tableau qui récupère les valeurs supérieures à e
    values_greater = []
    for i in L:
        if i > e:
            values_greater.append(i)
    return moyenne(values_greater)

print("Moyennes des valeurs de la liste strictement supérieures à 15:", moy_sup(L, 15))

def val_max(L):
    """ Cherche la valeur maximale de la liste
    Args:
        L de type liste
    Returns :
        La valeur maximale de la liste (int)
    """
    max_val = L[0]
    for i in range(len(L)-1):
        if (max_val - L[i+1]) < 0:
            max_val = L[i+1]    
    return max_val


def ind_max(L):
    """ Cherche l'index de la valeur maximale de la liste
    Args:
        L de type liste
    Returns :
        L'index de la valeur maximale de la liste (int)
    """
    max_val = val_max(L)
    for i in range(len(L)):
        if L[i] == max_val:
            return i

print("Valeur maximale de la liste:", val_max(L), "\nIndice de cette valeur maximale:", ind_max(L))   