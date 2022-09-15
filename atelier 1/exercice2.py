import math

#Dictionnaire du prix selon le poids
PRIX_POIDS = {
    20: 1.16,
    100: 2.32,
    250: 4.00,
    500: 6.00,
    1000: 7.50,
    3000: 10.50
}

OUTREMER_1 = [
    "guyane", "guadeloupe", "gartinique", "la réunion",
    "st-pierre-et-miquelon", "st-barthélémy", "st-martin-et-Mayotte"
]

OUTREMER_2 = [
    "nouvelle-calédonie", "polynésie française", "wallis-et-Futuna", "t.a.a.f"
]

OUTREMER_ALL = OUTREMER_1 + OUTREMER_2

#Prix en fonction de la zone (OM1 ou OM2)
PRIX_ZONES = {0.05: OUTREMER_1, 0.11: OUTREMER_2}


class LettresVertes:

    def prixPourZone(self):
        """
      Ajoute un supplément dans le prix si la lettre est à destination d'outre-mer et pèse plus de 100g
      Param : aucun
      """
        prixZone = 0
        if (self.poids > 100):
            for prix, array in PRIX_ZONES.items():
                if self.outreMer in array:
                    prixZone = prix * math.ceil(self.poids / 10)

        return prixZone

    def prixPourPoids(self):
        """
        Cherche le prix correspondant au poids et renvoie le prix
        Param : aucun
        """
        if self.poids <= list(PRIX_POIDS)[0]:
            return list(PRIX_POIDS.values())[0]
        else:
            for i in range(len(list(PRIX_POIDS)) - 1, 0, -1):
                if self.poids >= list(PRIX_POIDS)[i - 1]:
                    return list(PRIX_POIDS.values())[i]

    def __init__(self, poids, outreMer, sticker):
        """
          param : 
            poids de la lettre
            destination outre-mer
            sticker pour suivi de la lettre
            prix calculé par la fonction prixPourPoids()
        """
        self.poids = poids

        self.outreMer = outreMer

        self.sticker = sticker

        self.prix = self.prixPourPoids()

        #Si l'utilisateur a entré quelque chose
        if (self.outreMer != ''):
            self.prix += self.prixPourZone()
        #Si sticker a été défini sur True
        if (self.sticker):
            self.prix += 0.5


def nouvelleLettreVerte():
    """
    
    Fonction qui demande à l'utilisateur les paramètres pour l'instanciation d'une nouvelle lettre verte

    Return :
      prix de la lettre
      
    """
    #poids de type entier, outreMer et sticker de type string

    poids = int(
        input("Indiquez le poids de la lettre en grammes (≠0, max 3000) : "))
    while poids > 3000 or poids == 0:
        poids = int(input("Indiquez le poids de la lettre : "))

    outreMer = input(
        "Indiquez, si votre lettre doit partir vers l'outre-mer, sa destination (sans fautes de frappe svp), sinon appuyez sur entrée : "
    ).lower()

    if outreMer != '':
        while outreMer not in OUTREMER_ALL:
            outreMer = input(
                "Veuillez renseigner la destination sans fautes de frappe: "
            ).lower()
    else:
        outreMer = False

    sticker = input("Voulez-vous un sticker (O) ? ").upper()

    if sticker == 'O':
        sticker = True
    else:
        sticker = False

    #Instanciation d'une lettre verte
    lettreVerte = LettresVertes(poids, outreMer, sticker)
    return "Prix: ", lettreVerte.prix


print(nouvelleLettreVerte())
