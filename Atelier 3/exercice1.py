def full_name(str_arg: str):
    splited_name = str_arg.split()
    full_name = splited_name[0].upper() + ' ' + splited_name[1].capitalize()
    return full_name

def une_occurence(lst, e):
    """ Cherche le nombre d'occurences de la valeur dans la liste \n
    Args:
        L de type liste : les valeurs de f(x)
        e la valeur
    Returns:
        Booléen ou entier
    """
    compteur = 0
    i = 0
    while i < len(lst) and (compteur < 2):
        if lst[i] == e:
            compteur += 1  
            pos = i
        i += 1  
    if (compteur == 1):
        return pos
    else:
        return 0

str_test = 'mouse mickey'
str_test2 = 'veron-guaitella aurèle'

print(full_name(str_test))
print(full_name(str_test2))

########################################

def extremeOccur(lst, e):
    extreme_occ = False
    for i in range(len(lst)):
        if lst[i] == e:
            extreme_occ = i
    return extreme_occ

def notInExtremity(str_arg: str, e: chr) -> bool :
    notInExtremity = False
    if 0 < e < len(str_arg)-1:
        notInExtremity = True
    return notInExtremity
            
def arobase(str_arg):
    res = (0, 2)
    pos = une_occurence(str_arg, '@')
    if pos != 0:
        if notInExtremity(str_arg, pos):
            res = (1, 'x')
    return res
            
def point(str_arg):
    res = (0, 4)
    splited = str_arg.split('@')
    for str in splited:
        if notInExtremity(str, une_occurence(str_arg, '.')):
            res = (1, 'x')
    return res

def corps(str_arg):
    pass


mail_msg = {
    (1, 'x'): "Mail valide !",
    (0, 1): "Mail invalide ! Le corps n'est pas valide.",
    (0, 2): "Mail invalide ! Il doit y avoir un et un seul arobase.",
    (0, 3): "Mail invalide ! Le domaine n'est pas valide.",
    (0, 4): "Mail invalide ! Points manquants ou invalides."
}

def is_mail(str_arg: str) -> int:
    isValid = (1, 'x')
    test = arobase(str_arg)
    if test==isValid:
        test = point(str_arg)
        if test==isValid:
            pass
    return test

mail = 'aur.ele92@univ_corse.fr'
print(
    mail + ' -> ' + mail_msg[is_mail(mail)]
)
