import random
from exercice1 import gen_list_random_int

def choose_element_list(list_in_which_to_choose: list) -> int:
    randomIndex = random.randint(0, len(list_in_which_to_choose) - 1)
    return list_in_which_to_choose[randomIndex]

# Test code
lst_sorted = gen_list_random_int(len = 11)
print('Liste de départ', lst_sorted)
e1 = choose_element_list(lst_sorted)
print('A la première exécution', e1, 'a été sélectionné')
e2 = choose_element_list(lst_sorted)
print('A la deuxième exécution', e2, 'a été sélectionné')
assert e1 != e2, "Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"