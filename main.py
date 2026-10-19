 nom =input("donne ton nom !!")
age = int(input("donne ton age !!"))
"""
Ce programme n'es que partiellement compléte car j'ai pas encore appris  le reste des notion.21
"""
# cette fonction vas s'exécuté en lisant le nombre entré par l'utilisateur.
if age < 21:
 print("il n'as pas encore l'age pour lire python !!")

elif age == 21:
 print("dans ce cas il est temp de commencer la lecture !! ")

else:
 print("mais qu'es-ce qu'il faisais tout ce temp pour enfin commencer a lire")

 for n in range(1,16):
  resultat = age * n
  print(f"{age} * {n} = {resultat}")

n = 1
somme = 0
while n <= age:
 somme = somme + n
 n = n + 1
print("la somme est: , somme")