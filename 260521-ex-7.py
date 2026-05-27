niveau_difficulte = ["Débutant", "Moyen", "Difficile", "Dark Souls"]
difficulte_choisie = input("Choisissez votre difficulté")
if difficulte_choisie not in niveau_difficulte:
    print(
        f"Veuillez entrer une difficulté parmis les difficultés suivantes : {' '.join(niveau_difficulte)} \n"
    )
    difficulte_choisie = input("Choisissez votre difficulté")
    if difficulte_choisie not in niveau_difficulte:
        print("Vous ne pouvez pas jouer au jeu")
    else:
        print("Bienvenue !")
else:
    print("Bienvenue !")
