from exercice3 import choose_element_list, lst_sorted

def extract_elements_list(list_in_which_to_choose: list, int_nbr_of_element_to_extract: int) -> list:
    lastElements = list_in_which_to_choose
    randomValuesList = []
    for _ in range(int_nbr_of_element_to_extract):
        randomValue = choose_element_list(lastElements)
        randomValuesList.append(randomValue)
        lastElements.remove(randomValue)
    return randomValuesList

# Test de votre code
print('Liste de départ', lst_sorted)
sublist = extract_elements_list(lst_sorted, 5)
print('La sous liste extraite est', sublist)
print('Liste de départ après appel de la fonction est', lst_sorted)


