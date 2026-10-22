# ce programme est d'un ennuie monumentale
"""

"""
nombre1 = float(input("Entre le premier nombre : "))
operation = input("Choisis une opération (+, -, *, /) : ")
nombre2 = float(input("Entre le deuxième nombre : "))

if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    if nombre2 != 0:
        resultat = nombre1 / nombre2
    else:
        resultat = "Impossible de diviser par zéro"

if operation in ["+", "-", "*", "/"]:
    print("Résultat :", resultat)
else:
    print("Opération invalide")
