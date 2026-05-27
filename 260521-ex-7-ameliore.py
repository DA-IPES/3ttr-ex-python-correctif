# ce code est une proposition d'implémentation
# l'énoncé a été laissé volontairement assez ouvert dans la version bonus pour laisser place à votre créativité
niveau_difficulte = ["Débutant", "Moyen", "Difficile", "Dark Souls"]
difficulte_choisie = ""


def selection_difficulte():
    difficulte_choisie = input("Choisissez votre difficulté")

    if difficulte_choisie not in niveau_difficulte:
        print(
            f"Veuillez entrer une difficulté parmis les difficultés suivantes : {' '.join(niveau_difficulte)} \n"
        )
        return ""
    else:
        print("Bienvenue !")
        return difficulte_choisie


# une boucle while est plus adaptée ici, sinon, on aurait aussi pu faire un for avec une range(2) pour 2 essais maximum
while difficulte_choisie not in niveau_difficulte:
    difficulte_choisie = selection_difficulte()
