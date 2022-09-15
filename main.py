from math import sqrt

def discriminant(a, b, c) -> int:
    """ Calculer le discriminant
    Args:
        a (int) : coefficient quadratique de type entier
        b (int) : coefficient linéaire de type entier
        c (int) : constante de type entier
    Returns:
        Le discriminant
    """
    return b*b - 4*a*c

def racine_unique(a, b) -> str:
    """ Affiche la solution
    Args:
        a (int) : coefficient quadratique
        b (int) : coefficient linéaire
    Returns:
        La solution
    """
    return "x = {}".format(-b/(2*a))

def racine_double(a, b, delta, num) -> str:
    """ Calcule les deux racines de l'équation
    Args:
        a (int) : coefficient quadratique
        b (int) : coefficient linéaire
        delta : discriminant
        num le numéro de la solution
    Returns:
        Une des racines parmi les deux racines
    """
    solution = "x{} = ".format(num + 1)
    if (num==1):
        solution += (-b + sqrt(delta))/(2*a)
    else:
        solution += (-b - sqrt(delta))/(2*a)
    return solution

def str_equation(a, b, c) -> str:
    """ Affiche l'équation
    Args:
        a (int) : coefficient quadratique de type entier
        b (int) : coefficient linéaire de type entier
        c (int) : constante de type entier
    Returns:
        L'équation
    """
    return "{}x^2 + {}x + {} = 0".format(a, b, c)


def solution_equation(a, b, c) -> str:
    """ envoie la ou les solutions
    Param:
        a le  coefficient quadratique de type entier
        b le coefficient linéaire de type entier
        c la constante de type entier
    Return:
        La ou les solutions de l'équation
    """
    delta = discriminant(a, b, c)
    if delta < 0:
        solution = "Pas de racine réelle"
    elif delta == 0:
        solution = "Une racine unique :\n" + racine_unique(a, b)
    else:
        solution = "Deux racines : \n"
        for num in range(2):
            print(num)
            solution += racine_double(a, b, delta, num) + "\n"   
    return "Solution de l'équation " + str_equation(a, b, c) + "\n" + solution


def equation(a, b, c):
    """ Affiche la ou les solutions de l'équation
    Param:
        a le  coefficient quadratique de type entier
        b le coefficient linéaire de type entier
        c la constante de type entier
    """
    print(solution_equation(a, b, c))

        
def new_equation():
    """ Demande à l'utilisateur d'entrer les valeurs nécessaires à la
    résolution de l'équation
    """
    value_a = int(input("Entrez la valeur de a: "))
    value_b = int(input("Entrez la valeur de b: "))
    value_c = int(input("Entrez la valeur de c: "))
    equation(value_a, value_b, value_c)

new_equation()




#1 Les entrées : types
#2 les pre-conditions : les caract des entrées
#3 les sorties
#4 les post conditions que doivent vérifier les sorties

"""
paramètre formel pour la fonction
paramètre effectif pour l'appel

python est permissif

littral : pas de variable assignée à la valeur

effets de bord

tout est objet
les var ne contiennetn pas une valeur mais 
contineenet une ref (adrrese mem ou id) vers un objet

objets immutables
fnoction id represente id interne (adr mem) d'une var qulst son type
compteur de référence objet
"""