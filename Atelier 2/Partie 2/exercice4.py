def val_max(lst):
    """ Cherche la valeur maximale de la liste
    Args:
        L de type liste
    Returns :
        La valeur maximale de la liste (int)
    """
    max_val = lst[0]
    for i in lst:
        if max_val < i:
            max_val = i    
    return max_val

def nb_occurrences(L, e):
    """ Cherche le nombre d'occurences de la valeur dans la liste
    Args:
        L de type liste : les valeurs de f(x)
        e la valeur
    Returns :
        H de type liste : l'histogramme
    """
    ct = 0
    for i in L:
        if e == i:
            ct += 1
    return ct

def histo(F):
    max_val = val_max(F) + 1
    H = [0] * max_val
    for i in range(max_val):
        H[i] = nb_occurrences(F, i)
    return H

print(histo([0, 2, 2, 2, 4, 4, 4, 7]))

