#Liste désordonnée sans valeur répétitive
LIST = [1, 52, 14, 24, 6, 18, 20, 45]
#Liste croissante
LST_CROISS = [1, 5, 12, 22, 36, 58]
#Liste avec valeurs répétitives
LIST_REP = [28, 15, 15, 12, 52, 15, 35, 52, 22, 52, 15]

def position_for(L = list, e = int):
    """ Cherche l'indice de e dans la liste avec une boucle for
    Args:
        La liste (list)
        e (int)
    Returns:
        Si e n'appartient pas à la liste:
            On renvoie -1
        Sinon on renvoie e
    """
    for i in range(len(L)):
        if e == L[i]:
            return i
    #else
    return -1
        
def position_while(L = list, e = int):
    """ Cherche l'indice de e dans la liste avec une boucle while
    Args:
        La liste (list)
        e (int)
    Returns:
        Si e n'appartient pas à la liste:
            On renvoie -1
        Sinon on renvoie e
    """
    #Valeur par défaut si e n'est pas trouvé
    index = -1
    i = 0
    while i < len(L):
        if e == L[i]:
            index = i
        if i < len(L):
            i += 1
    return index


value = 18
print("Index de", value, "(avec boucle for):", position_for(LIST, value))
print("Index de", value, "(avec boucle while):", position_while(LIST, value))

def nb_occurrences(L, e):
    occurences = 0
    for i in range(len(L)):
        if e == L[i]:
            occurences += 1
    if (occurences == 0):
        return -1
    else:
        return occurences

value = 15
print("Nombre d'occurences de {} dans cette liste répétitive {} :".format(value, LIST_REP), nb_occurrences(LIST_REP, value))

def est_triee_for(L):
    est_triee = True
    #On part du principe que la liste est triée
    for i in range(len(L)-1):
        #On cherche à montrer que liste n'est pas triée
        if (L[i] > L[i + 1]):
            est_triee = False
    return est_triee

def est_triee_while(L):
    #On part du principe que la liste est triée
    est_triee = True
    i = 0
    while est_triee == True and i < len(L)-1:
        #On cherche à montrer que liste n'est pas triée
        if (L[i] > L[i + 1]):
            est_triee = False
        else:
            i += 1
    return est_triee

print("Cette liste {} est-elle triée (boucle while) ?".format(LIST), est_triee_for(LIST))
print("Cette liste {} est-elle triée (boucle while) ?".format(LIST), est_triee_while(LIST))

print("Cette liste {} est-elle triée (boucle for) ?".format(LST_CROISS), est_triee_for(LST_CROISS))
print("Cette liste {} est-elle triée (boucle while) ?".format(LST_CROISS), est_triee_while(LST_CROISS))

def position_tri(L, e):
    """ Fonction qui suppose que la liste est triée
    Recherche par dichotomie
    Args:
        La liste (list)
        e (int)
    Returns:
        Si e n'appartient pas à la liste:
            On renvoie -1
        Sinon on renvoie e
    """
    moyenne = int()
    if (len(L) > 1): 
        if (len(L)%2 == 0):
            moyenne = int(len(L)/2)
        else:
            moyenne = int((len(L)+1)/2)
    elif (L[0] == e):
        return 0
    if (e == L[moyenne]):
        return moyenne
    else:
        newSearch = []
        if (e > L[moyenne]):
            for i in range (moyenne, len(L)):
                newSearch.append(L[i])
            position_tri(newSearch, e)
        else:
            for i in range (moyenne):
                newSearch.append(L[i])
            position_tri(newSearch, e)

value = 36
print("Index de", value, ":", 
position_tri(LST_CROISS, value))

def a_repetitions(L):
    pass
    
