def separer(L):
    """ Fonction qui dans une liste range à gauche les nombres positifs,
    à droite les nombres négatifs et au milieu les cases nulles
    Args:
        L de type de liste
    Return:
        new_list de type liste
    """
    # Ranger les nombres positifs trouvés
    positifs = []
    # Ranger les valueurs nulles trouvés
    nul = []
    # Ranger les nombres négatifs trouvés
    negatifs = []
    for i in L:
        if i < 0:
            negatifs.append(i)
        elif i > 0:
            positifs.append(i)
        else:
            nul.append(i)
    new_list = negatifs + nul + positifs
    return new_list

LSEP = [-5, -8, 8, -6, 12, 0, 0, -32, 2, 3, -84]
print(separer(LSEP))