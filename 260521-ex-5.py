age = int(input("Quel est ton age ? "))
# si je ne suis pas <13 ou >15, je suis forcément compris entre ces 2 bornes. Remarquez le symbole utilisé pour les ifs
if age < 13:
    print("Tu es trop jeune")
elif age > 150:
    print("Es-tu un extraterrestre ?!?")
else:
    print("Tu peux jouer")
