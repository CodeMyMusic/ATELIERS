import random

def placesLettre(ch: chr, mot: str) -> list:
    """ Cherche les indices des occurences dans la liste
    """
    plcsLettre = []
    for i in range(len(mot)):
        if mot[i] == ch:
            plcsLettre.append(i)
    return plcsLettre

print(placesLettre('u', 'pulluler'))

def testPlaceLettre():
    ch = input("Entrez le caractère à rechercher: ")
    mot = input("Entrez le mot: ")
    print(
        "Le caractère se trouve aux indices suivants:",
        placesLettre(ch, mot)
    )

#test_place_lettre()

##############################

def strOutput(mot: str, lpos: list) -> str:
    i = 0
    indexPos = 0
    while indexPos < len(lpos) and i < len(mot):
        if i == lpos[indexPos]:
            mot = mot[:i] + '-' + mot[i+1:]
            indexPos += 1
        i += 1
    return mot

def tri(lst: list) -> list:
    if len(lst) > 0:
        lst.sort()
        finalList = [] 
        for i in lst: 
            if i not in finalList: 
                finalList.append(i) 
    return lst

def makeNewPendu():
    mot = input("Entrez le mot: ")
    strmask = input("Entrez le ou les indices (sans espace) des lettres qui seront masquées: ")
    mask = []
    for i in strmask:
        mask.append(int(i))
    print(mask)
    mask = tri(mask)
    print(strOutput(mot, mask))

#makeNewPendu()

##############################

def hide(elmts):
    mask_chars = []
    for i in range(elmts):
        mask_chars.append(i)
    return mask_chars

pendu = [
    "|---] ",
    "| O ",
    "| T ",
    "|/ \ ",
    "|_____"
]

def runGame():
    """ Lance un pendu
    """

    # Liste de mots pour le pendu
    words_lst = ['intrinsèque', 'syncrétisme', 'idoine', 'vespéral', 
    'agnostique', 'dithyranmbique', 'irénisme']

    # Un mot au hasard est choisi
    word = random.choice(words_lst)

    # Un masque pour le mot
    word_mask = hide(len(word))

    # Nombre d'erreurs de l'utilisateur
    err = 0
    while len(word_mask) > 0 and err < 5:
        word_output = strOutput(word, word_mask)
        print(word_output)
        # L'utilisateur rentre une lettre
        lettre = input("Entrez une lettre : ").lower()
        # Nombre d'occurences de cette lettre
        occurence = placesLettre(lettre, word)
        if len(occurence) > 0: 
            for i in range(len(occurence)):
                if occurence[i] in word_mask:
                    word_mask.remove(occurence[i])

            # On affiche le nouveau rendu du mot masqué
            word_output = strOutput(word, word_mask)

            print("Vous avez trouvé", len(occurence), "lettre(s)")
        else:
            print("Non !")
            err += 1
            # On dessine
            for i in range(err):
                print(pendu[i])
    if err < 5:
        print("Félications, le mot était", word, "!")
    else:
        print("Vous avez perdu ! Le mot était", word + '.')
    

#runGame()

# fin pendu
############################

"""
i = 0
indexPos = 0
while indexPos < len(occurence) and i < len(word):

    if word_mask[i] == occurence[indexPos]:
        if word_mask[i] == 0:
            word_output = word[0] + word_output[1:]
        elif word_mask[i] == len(word_mask)-1:
            word_output = word_output[:i-1] + word[i] 
        else:
            word_output = word_output[:i] + word[i] + word_output[i+1:]
        indexPos += 1
        new_mask = hide(len(word_mask)-1)
        if i < len(word) -1:
            i += 1
    i += 1"""

########################


def build_list(fileName: str):
    file = open(fileName, 'r', encoding="UTF-8")
    content = file.readlines()
    lst_words = []
    for str in content:
        print(str)
        for str_sub in str.split('\t'):
           for str_sub_sub in str_sub.split('\n'):
                lst_words.append(str_sub_sub)
    lst_words.remove('')
    print(lst_words)
        

build_list("capitales.txt")



