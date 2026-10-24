
import random

print("================================")
print("     JEU DU NOMBRE SECRET")
print("================================")

nombre_secret = random.randint(1, 20)
tentatives = 0
trouve = False

print("Je pense à un nombre entre 1 et 20.")

while trouve == False:
    choix = int(input("Devine le nombre : "))
    tentatives += 1

    if choix < nombre_secret:
        print("Trop petit ! Essaie encore.")

    elif choix > nombre_secret:
        print("Trop grand ! Essaie encore.")

    else:
        print("Bravo ! Tu as trouvé le nombre secret.")
        print("Nombre de tentatives :", tentatives)
        trouve = True

print("Fin du jeu. Merci d'avoir joué !")