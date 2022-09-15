def agencer(nbEmplacements = int, lstObjets = list):
    if (nbEmplacements * 2 < len(lstObjets)):
        return "ERREUR: Il y a plus d'objets que d'emplacements disponibles"
    if (len(lstObjets)%2 == 0):
        for i in lstObjets:
            

agencer(4, [1, 2, 2, 3, 4, 5, 5])