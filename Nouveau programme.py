"""
Mon premier programme en python qui demande un nombre a 
l'utilisateur et qui affiche mineur s'il est inférieur a 18 et 
majeur s'il est egal a 18 et enfin adulte s'il est  supérieur !!
"""
nombre = int(input("please enter your nombre"))
if nombre < 18:
    print("you are a minor.")

elif nombre >= 18 and nombre < 21:
    print("you are major")

else:
    print("you are adulte")

for i in range(1, 11):
    resultat = nombre * i
    print(f"{nombre} x {i} = {resultat}")
i = 1
somme = 0
while i <= nombre:
    somme = somme + i
    i = i + 1
print(f"la somme est: {somme}")