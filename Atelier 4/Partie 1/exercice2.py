import random
from exercice1 import gen_list_random_int, len_default

def random_index():
    return random.randint(0, len(list_in_which_to_choose) - 1)

def mix_list(list_to_mix: list) -> list:
    return gen_list_random_int(0, len(list_to_mix))

# Test code
lst_sorted = [i for i in range(len_default)]
print(lst_sorted)
print('Liste triée de départ', lst_sorted)
mixed_list=mix_list(lst_sorted)
print('Liste mélangée obtenue', mixed_list)
print('Liste triée de départ après appel à mixList, elle doit être inchangée', lst_sorted)
assert lst_sorted != mixed_list,"Les deux listes doivent être différentes après l'appel à mixList..."