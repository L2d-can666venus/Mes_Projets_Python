name = input("please enter your name: ")
age = int(input("please enter your age: "))
if age < 18:
    print(f"{name}, you are a minor.")
elif age >= 18 and age < 21:
    print(f"{name}, you are major.")
else:
    print(f"{name}, you are an adult.")

    v = 5
    S = 0
    while v <= age:
        S = S + v
        v = v + 1
    print(f"{name}, the sum of numbers from 5 to {age} is {S}.")

    for i in range(1, 11):
        resultat = age * i
        print(f"{name}, {age} times {i} is {resultat}.")
    name_girlfriend = input("please enter your girlfriend's name: ")
    age_girlfriend = int(input(f"please enter {name_girlfriend}'s age: "))
    tail = age - age_girlfriend
    if tail > 0:
        print(f"{name}, you are older than {name_girlfriend} by {tail} years.")
    elif tail < 0:
        print(f"{name}, you are younger than {name_girlfriend} by {-tail} years.")  
    else:
        print(f"{name}, you and {name_girlfriend} are the same age.")
    love = input(f"Do you love {name_girlfriend}? (yes/no): ")
    if love.lower() == "yes":
        print(f"{name}, you love {name_girlfriend}.")
    else:
        print(f"{name}, you do not love {name_girlfriend}.")

venus = input("please enter your favorite prenom: ")
print(f"{name}, your favorite prenom is {venus}.")
print("my favorite prenom is bintou because it is the name of the goddess of love and beauty in Roman mythology and she is my grlfriend. I love her because she is beautiful, kind, and caring. I want to spend the rest of my life with her and make her happy. I will always cherish and respect her, and I will never let anyone hurt her. She is my everything, and I am grateful to have her in my life.")