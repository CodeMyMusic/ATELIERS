import random

len_default = 10

def gen_list_random_int(int_binf = 0, int_bsup = 10, len = len_default) -> list:
    int_nbr = []
    for _ in range(len):
        int_nbr.append(random.randint(int_binf, int_bsup - 1))
    return int_nbr

print(gen_list_random_int(2, 8))