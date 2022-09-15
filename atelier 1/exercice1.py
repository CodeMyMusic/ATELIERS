import random


def comparaisonChoix(choixJoueur1, choixJoueur2, scoreJoueur1, scoreJoueur2,
                     puitGagne):
    if choixJoueur1 == choixJoueur2:
        print("Il y a égalité")
    else:
        scoreJoueur1, scoreJoueur2 = comparaisonChoixBis(
            choixJoueur1, choixJoueur2, scoreJoueur1, scoreJoueur2, puitGagne)
    return scoreJoueur1, scoreJoueur2


def comparaisonChoixBis(choix1, choix2, scoreJoueur1, scoreJoueur2, puitGagne):
    if choix1 == "puit":
        for choix in puitGagne:
            if choix1 == choix:
                scoreJoueur1 += 1
    else:
        if choix1 == 'papier' and choix2 == 'pierre':
            scoreJoueur1 += 1
        if choix1 == 'pierre' and choix2 == 'ciseaux':
            scoreJoueur1 += 1
        if choix1 == 'ciseaux' and choix2 == 'papier':
            scoreJoueur1 += 1
    return scoreJoueur1, scoreJoueur2


def partie(joueur1, joueur2):

    nombreDeManches = 0
    scoreJoueur1 = scoreJoueur2 = 0
    puitGagne = ["pierrre", "ciseaux"]

    options = ["pierre", "papier", "ciseaux"]

    def variantePuit():
        variante = input("Voulez-vous autoriser le puit ? O/N ").upper()
        if variante == 'O' or variante == 'N':
            if variante == 'O':
                options.append('puit')
                print("Le puit est désormais autorisé.")

            else:
                print("Le puit ne sera pas autorisé.")
        else:
            print("Je n'ai pas compris votre réponse.")
            variantePuit()

    variantePuit()

    def testChoixEntré():
        choix = input("{nom} faîtes votre choix : ".format(nom=joueur1))
        if choix in options:
            return choix
        else:
            print("Désolé je n'ai pas compris votre réponse.")
            testChoixEntré()

    def manche(nombreDeManches, scoreJoueur1, scoreJoueur2, puitGagne):

        nombreDeManches += 1

        ################# CHOIX ###################

        choixJoueur1 = testChoixEntré()

        if joueur2 == 'Machine':
            choixJoueur2 = random.choice(options)
        else:
            choixJoueur2 = testChoixEntré()

        ################# CHOIX ###################

        # On affiche les choix de chacun
        print("Si on récapitule :", joueur1, "a choisi", choixJoueur1, "et",
              joueur2, "a choisi", choixJoueur2, "\n")

        #SCORES
        scoreJoueur1, scoreJoueur2 = comparaisonChoix(choixJoueur1,
                                                      choixJoueur2,
                                                      scoreJoueur1,
                                                      scoreJoueur2, puitGagne)
        print("Les scores à l'issue de cette manche sont donc \n" + joueur1,
              ":", scoreJoueur1, "\n" + joueur2, ":", scoreJoueur2, "\n")

        if nombreDeManches < 4:
            manche(nombreDeManches, scoreJoueur1, scoreJoueur2, puitGagne)
        else:
            #On propose de continuer ou de s'arrêter
            nouvellePartie = input(
                "Souhaitez vous refaire une partie {} contre {} ? (O/N) ".
                format(joueur1, joueur2)).upper()
            if nouvellePartie == 'O':
                partie()
            elif nouvellePartie == 'N':
                print("Merci d'avoir joué ! A bientôt")
            if nouvellePartie != 'O' and nouvellePartie != 'N':
                print(
                    "Vous ne répondez pas à la question, une nouvelle partie est lancée"
                )
                partie()

    manche(nombreDeManches, scoreJoueur1, scoreJoueur2, puitGagne)


def joueurs():
    chxAdversaire = input(
        "Voulez-vous jouer contre l'ordinateur (O) ou contre un autre joueur (J) (Max 5 parties) ? "
    ).upper()
    if chxAdversaire == 'O' or chxAdversaire == 'J':
        if chxAdversaire == 'O':
            joueur1 = input("Quel est votre nom ? ")
            while joueur1 == "Machine":
                print("Erreur, ce nom est réservé à la machine")
                joueur1 = input("Quel est votre nom ? ")

            joueur2 = "Machine"
        else:
            joueur1 = input("Quel est le nom du premier joueur ?")
            joueur2 = input("Quel est le nom du deuxième joueur ?")
        partie(joueur1, joueur2)
    else:
        print("Je n'ai pas compris votre réponse")


joueurs()
