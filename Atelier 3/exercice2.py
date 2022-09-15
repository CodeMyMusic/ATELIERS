def mots_Nlettres(lst_mot: list, n: int):
    isSameLen = []
    for i in lst_mot:
        if n == len(i):
            isSameLen.append(i)
    return isSameLen

lst_mot = ["winner", "cuistre", "coccolithophoridés", "fructifier", 
"antagoniste", "éperluette", "curé", "critère", "essart", "virulent", "cuisson", "looser",
"proie", "autiste", "cratère"]

print(mots_Nlettres(lst_mot, 5))

def commence_par(mot, prefixe):
    i = 0
    isPrefixe = True
    while (isPrefixe == True) and (i < len(prefixe)):
        if mot[i] == prefixe[i]:
            i += 1
        else:
            isPrefixe = False
    return isPrefixe

print(commence_par('balivernes', 'bal'))

def termine_par(mot, suffixe):
    i = len(suffixe) - 1
    isSuffixe = True
    while (isSuffixe == True) and i >= 0:
        if mot[i + len(mot) - len(suffixe)] == suffixe[i]:
            i -= 1
        else:
            isSuffixe = False
    return isSuffixe

print(termine_par('le vicompte', 'compte'))

def commencent_par(lst_mot, prefixe):
    arePrefixe = []
    for i in lst_mot:
        if (commence_par(i, prefixe)):
            arePrefixe.append(i)
    return arePrefixe

def terminent_par(lst_mot, suffixe):
    areSuffixe = []
    for i in lst_mot:
        if (termine_par(i, suffixe)):
            areSuffixe.append(i)
    return areSuffixe

print(commencent_par(lst_mot, 'cu'))
print(terminent_par(lst_mot, 'er'))

def liste_mots(lst_mot, prefixe, suffixe, n):
    lst_valid = commencent_par(lst_mot, prefixe)
    lst_valid = terminent_par(lst_valid, suffixe)
    lst_valid = mots_Nlettres(lst_valid, n)
    return lst_valid

print(liste_mots(lst_mot, 'cr', 'ère', 7))

def dictionaire(fichier):
    f = open(fichier, 'r')
    line = f.readline()
    print("** Contenu du fichier **")
    while line != "":
        print(line)
        line = f.readline()
    print("** fin **")

dictionaire('littre.txt')



