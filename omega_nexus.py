
import json
import os
import random
import time
from datetime import datetime

# ============================================================
# OMEGA NEXUS v1.0
# Un laboratoire interactif de programmation et de cybersécurité
# Bibliothèques utilisées : Python standard uniquement
# ============================================================

SAVE_FILE = "omega_nexus_save.json"
VERSION = "1.0"

MISSIONS = [


    {
        "id": "PY01",
        "title": "La boucle mystérieuse",
        "category": "Python",
        "question": "Quel résultat affiche : print(sum(range(5))) ?",
        "choices": ["5", "10", "15", "Erreur"],
        "answer": 1,
        "explanation": "range(5) produit 0, 1, 2, 3, 4. Leur somme vaut 10.",
        "xp": 25,
    }, ]
{
        "id": "PY02",
        "title": "Le détecteur de nombres",
        "category": "Python",
        "question": "Quel opérateur teste si un nombre est pair ?",
        "choices": ["/", "//", "%", "**"],
        "answer": 2,
        "explanation": "n % 2 == 0 teste si le reste de la division par 2 est nul.",
        "xp": 25,
}
{
        "id": "PY03",
        "title": "La liste secrète",
        "category": "Python",
        "question": "Que vaut len(['A', 'B', 'C']) ?",
        "choices": ["2", "3", "4", "0"],
        "answer": 1,
        "explanation": "len() renvoie le nombre d'éléments : ici, trois.",
        "xp": 25,
          },
{
        "id": "SEC01",
        "title": "Le mot de passe suspect",
        "category": "Cybersécurité",
        "question": "Quel est le meilleur réflexe face à un lien suspect ?",
        "choices": [
            "Cliquer immédiatement",
            "Entrer son mot de passe",
            "Vérifier la source sans ouvrir le lien",
            "Envoyer le lien à tous ses contacts",
        ],
        "answer": 2,
        "explanation": "Vérifie l'expéditeur et le domaine. N'entre jamais tes identifiants sur une page douteuse.",
        "xp": 30,
    },


{
        "id": "SEC02":   
        "title": "Le principe du moindre privilège",
        "category": "Cybersécurité",
        "question": "Que signifie le moindre privilège ?",
        "choices": [
            "Donner tous les droits à chaque utilisateur",
            "Accorder seulement les droits nécessaires",
            "Désactiver tous les comptes",
            "Partager les mots de passe",
        ],
        "answer": 1,
        "explanation": "Chaque utilisateur ou programme ne reçoit que les permissions nécessaires à sa mission.",
        "xp": 30,
},
{
        "LOG01",
        "title": "Le raisonnement",
        "category": "Logique",
        "question": "Complète la suite : 2, 4, 8, 16, ...",
        "choices": ["18", "24", "30", "32"],
        "answer": 3,
        "explanation": "Chaque terme est multiplié par 2. Le terme suivant est 32.",
        "xp": 20,
    },



def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nAppuie sur Entrée pour continuer...")


def slow_print(message, delay=0.015):
    """Affiche progressivement un message."""
    for character in message:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


def default_data():
    return {
        "player": "",
        "xp": 0,
        "completed": [],
        "attempts": 0,
        "correct": 0,
        "created": datetime.now().strftime("%Y-%m-%d"),
        "achievements": [],
    }


def load_data():
    if not os.path.exists(SAVE_FILE):
        return default_data()

    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        defaults = default_data()
        defaults.update(data)

        # Vérifications élémentaires de la sauvegarde.
        if not isinstance(defaults["completed"], list):
            defaults["completed"] = []
        if not isinstance(defaults["achievements"], list):
            defaults["achievements"] = []

        return defaults

    except (json.JSONDecodeError, OSError):
        print("Sauvegarde illisible. Création d'une nouvelle progression.")
        return default_data()


def save_data(data):
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except OSError as error:
        print(f"Impossible de sauvegarder : {error}")


def level_from_xp(xp):
    return xp // 100 + 1


def level_title(level):
    if level >= 10:
        return "Architecte OMEGA"
    if level >= 7:
        return "Ingénieur système"
    if level >= 5:
        return "Analyste confirmé"
    if level >= 3:
        return "Explorateur technique"
    return "Recrue du laboratoire"


def progress_bar(value, maximum, width=24):
    if maximum <= 0:
        ratio = 0
    else:
        ratio = min(value / maximum, 1)

    filled = int(width * ratio)
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def award_xp(data, amount):
    old_level = level_from_xp(data["xp"])
    data["xp"] += amount
    new_level = level_from_xp(data["xp"])

    print(f"\n+{amount} XP")

    if new_level > old_level:
        print(f"\n*** NIVEAU SUPERIEUR : {new_level} ! ***")
        print(f"Titre : {level_title(new_level)}")

    check_achievements(data)
    save_data(data)


def check_achievements(data):
    achievements = {
        "first_mission": (
            len(data["completed"]) >= 1,
            "Premier contact : terminer une mission",
        ),
        "five_missions": (
            len(data["completed"]) >= 5,
            "Persévérance : terminer cinq missions",
        ),
        "ten_correct": (
            data["correct"] >= 10,
            "Esprit analytique : réussir dix questions",
        ),
        "level_five": (
            level_from_xp(data["xp"]) >= 5,
            "Progression : atteindre le niveau 5",
        ),
    }

    for key, (condition, description) in achievements.items():
        if condition and key not in data["achievements"]:
            data["achievements"].append(key)
            print(f"\n[SUCCES DEBLOQUE] {description}")


def create_profile(data):
    clear_screen()
    print("=" * 54)
    print("             CREATION DU PROFIL")
    print("=" * 54)

    if data["player"]:
        print(f"Profil actuel : {data['player']}")
        choice = input("Changer de nom ? (o/n) : ").strip().lower()
        if choice != "o":
            return

    while True:
        name = input("Choisis ton nom de code : ").strip()

        if 2 <= len(name) <= 24:
            data["player"] = name
            save_data(data)
            print(f"\nBienvenue dans OMEGA NEXUS, {name}.")
            break

        print("Le nom doit contenir entre 2 et 24 caractères.")

    pause()


def show_header(data):
    name = data["player"] or "Recrue"
    level = level_from_xp(data["xp"])

    print("=" * 60)
    print("                  OMEGA NEXUS")
    print("           LABORATOIRE TECHNIQUE LOCAL")
    print("=" * 60)
    print(f" Opérateur : {name}")
    print(f" Niveau    : {level} | {level_title(level)}")
    print(f" XP        : {data['xp']}")
    print("=" * 60)


def show_dashboard(data):
    clear_screen()
    show_header(data)

    total = len(MISSIONS)
    completed = len(data["completed"])
    next_level_xp = level_from_xp(data["xp"]) * 100
    current_level_start = (level_from_xp(data["xp"]) - 1) * 100

    print("\n                 TABLEAU DE BORD")
    print("-" * 60)
    print(f" Missions terminées : {completed}/{total}")
    print(f" Questions tentées  : {data['attempts']}")
    print(f" Réponses correctes : {data['correct']}")
    print(
        f" Progression niveau : "
        f"{progress_bar(data['xp'] - current_level_start, 100)}"
    )
    print(f" XP prochain niveau : {next_level_xp - data['xp']}")
    print(f" Profil créé le     : {data['created']}")
    print("\n Succès débloqués :")

    if data["achievements"]:
        for achievement in data["achievements"]:
            print(f"  * {achievement}")
    else:
        print("  Aucun pour le moment.")

    pause()


def mission_menu(data):
    while True:
        clear_screen()
        show_header(data)

        print("\n                 CENTRE DE MISSIONS")
        print("-" * 60)

        for index, mission in enumerate(MISSIONS, start=1):
            status = (
                "TERMINEE"
                if mission["id"] in data["completed"]
                else "A FAIRE"
            )
            print(
                f"{index}. [{mission['category']}] "
                f"{mission['title']} | {mission['xp']} XP | {status}"
            )

        print("\n0. Retour au menu principal")

        choice = input("\nSélectionne une mission : ").strip()

        if choice == "0":
            return

        if not choice.isdigit() or not 1 <= int(choice) <= len(MISSIONS):
            print("Choix invalide.")
            time.sleep(1)
            continue

        mission = MISSIONS[int(choice) - 1]

        if mission["id"] in data["completed"]:
            print("Cette mission est déjà terminée.")
            pause()
            continue

        run_mission(data, mission)


def run_mission(data, mission):
    clear_screen()
    print(f"MISSION : {mission['title']}")
    print(f"Catégorie : {mission['category']}")
    print("-" * 60)
    print(mission["question"])
    print()

    for index, option in enumerate(mission["choices"], start=1):
        print(f"{index}. {option}")

    choice = input("\nTa réponse : ").strip()

    if not choice.isdigit() or not 1 <= int(choice) <= len(mission["choices"]):
        print("Réponse invalide. Mission non comptabilisée.")
        pause()
        return

    data["attempts"] += 1
    selected = int(choice) - 1

    if selected == mission["answer"]:
        print("\nCORRECT !")
        data["correct"] += 1
        data["completed"].append(mission["id"])
        award_xp(data, mission["xp"])
    else:
        print("\nINCORRECT.")
        print("La mission reste disponible. Réessaie après avoir étudié.")

    print(f"\nExplication : {mission['explanation']}")
    save_data(data)
    pause()


def virtual_terminal():
    """Terminal simulé : aucune commande système n'est exécutée."""
    virtual_files = {
        "readme.txt": "Bienvenue dans le laboratoire OMEGA.",
        "mission.txt": "Objectif : apprendre, tester, comprendre.",
        "secret.txt": "La connaissance exige de la pratique.",
    }

    current_dir = "/omega"
    history = []

    clear_screen()
    print("OMEGA VIRTUAL TERMINAL")
    print("Terminal simulé : les commandes sont locales au programme.")
    print("Tape 'help' pour afficher les commandes disponibles.")

    while True:
        command = input(f"\noperator@omega:{current_dir}$ ").strip()

        if not command:
            continue

        history.append(command)
        parts = command.split()
        action = parts[0].lower()
        argument = " ".join(parts[1:])

        if action in ("exit", "quit"):
            print("Fermeture du terminal virtuel.")
            break

        elif action == "help":
            print("""
Commandes disponibles :
  help       : afficher l'aide
  whoami     : afficher l'opérateur
  pwd        : afficher le dossier simulé
  ls         : lister les fichiers simulés
  cat NOM    : lire un fichier simulé
  echo TEXTE : afficher un texte
  date       : afficher la date locale
  history    : afficher les commandes saisies
  clear      : effacer l'écran
  exit       : quitter le terminal
""")

        elif action == "whoami":
            print("operator")

        elif action == "pwd":
            print(current_dir)

        elif action == "ls":
            for filename in virtual_files:
                print(filename)

        elif action == "cat":
            if argument in virtual_files:
                print(virtual_files[argument])
            else:
                print("Fichier simulé introuvable.")

        elif action == "echo":
            print(argument)

        elif action == "date":
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        elif action == "history":
            for index, item in enumerate(history, start=1):
                print(f"{index}. {item}")

        elif action == "clear":
            clear_screen()

        else:
            print("Commande inconnue. Tape 'help'.")

    pause()


def security_lab():
    clear_screen()
    print("=" * 60)
    print("               LABORATOIRE SECURITE")
    print("=" * 60)
    print("Environnement pédagogique fictif.")
    print("Aucun appareil externe n'est contacté.")
    print("\nChoisis une expérience :")
    print("1. Analyser la robustesse d'un mot de passe fictif")
    print("2. Comprendre le hachage SHA-256")
    print("3. Simuler une vérification d'accès")
    print("0. Retour")

    choice = input("\nTon choix : ").strip()

    if choice == "1":
        password = input("Entre un mot de passe fictif : ")

        score = 0
        if len(password) >= 12:
            score += 1
        if any(c.islower() for c in password) and any(
            c.isupper() for c in password
        ):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(not c.isalnum() for c in password):
            score += 1

        print("\nAnalyse pédagogique :")
        print(f"Longueur : {len(password)} caractères")
        print(f"Critères satisfaits : {score}/4")

        if score <= 1:
            print("Conseil : augmente la longueur et utilise une phrase unique.")
        elif score <= 3:
            print("Résultat intermédiaire. Privilégie une longue phrase unique.")
        else:
            print("Plusieurs critères sont présents. Cela ne garantit pas la sécurité.")

        print(
            "Ne saisis jamais un véritable mot de passe personnel "
            "dans cet exercice."
        )

    elif choice == "2":
        import hashlib

        message = input("Entre un texte de démonstration : ")
        digest = hashlib.sha256(message.encode("utf-8")).hexdigest()

        print("\nTexte : ", message)
        print("SHA-256 : ", digest)
        print("\nUn hachage est une empreinte, pas un chiffrement réversible.")
        print("Un hachage rapide seul ne suffit pas à stocker des mots de passe.")

    elif choice == "3":
        correct_code = "OMEGA-42"
        entered = input("Code fictif requis : ")

        if entered == correct_code:
            print("Accès simulé accordé.")
        else:
            print("Accès simulé refusé.")

        print("Ce contrôle est uniquement une démonstration locale.")

    elif choice == "0":
        return

    else:
        print("Option inconnue.")

    pause()


def logic_challenge():
    clear_screen()
    print("=" * 60)
    print("                  DEFIS DE LOGIQUE")
    print("=" * 60)

    challenges = [
        {
            "question": "Suite : 3, 6, 12, 24, ...",
            "answer": "48",
            "explanation": "Chaque terme est multiplié par 2.",
        },
        {
            "question": "Combien vaut 7 * 3 - 5 ?",
            "answer": "16",
            "explanation": "La multiplication vient avant la soustraction : 21 - 5.",
        },
        {
            "question": "Combien de fois s'exécute range(3) ?",
            "answer": "3",
            "explanation": "Les valeurs sont 0, 1 et 2.",
        },
        {
            "question": "Quel est le résultat de 17 % 5 ?",
            "answer": "2",
            "explanation": "17 = 3 * 5 + 2. Le reste est 2.",
        },
    ]

    challenge = random.choice(challenges)
    print(challenge["question"])

    answer = input("Réponse : ").strip()

    if answer == challenge["answer"]:
        print("Bien joué ! Raisonnement correct.")
    else:
        print(f"Pas tout à fait. Réponse attendue : {challenge['answer']}")

    print("Explication :", challenge["explanation"])
    pause()


def about():
    clear_screen()
    print("OMEGA NEXUS")
    print(f"Version : {VERSION}")
    print("Type : application pédagogique en ligne de commande")
    print("Langage : Python")
    print("Dépendances externes : aucune")
    print("Réseau : aucune connexion réseau initiée par ce programme")
    print(f"Sauvegarde : {os.path.abspath(SAVE_FILE)}")
    print("\nCe projet est un point de départ modifiable.")
    pause()


def main():
    data = load_data()

    if not data["player"]:
        create_profile(data)

    while True:
        clear_screen()
        show_header(data)

        print("""
1. Tableau de bord et statistiques
2. Centre de missions
3. Terminal virtuel
4. Laboratoire de cybersécurité
5. Défi de logique aléatoire
6. Créer ou modifier mon profil
7. À propos du projet
0. Quitter
""")

        choice = input("Sélectionne une option : ").strip()

        if choice == "1":
            show_dashboard(data)
        elif choice == "2":
            mission_menu(data)
        elif choice == "3":
            virtual_terminal()
        elif choice == "4":
            security_lab()
        elif choice == "5":
            logic_challenge()
        elif choice == "6":
            create_profile(data)
        elif choice == "7":
            about()
        elif choice == "0":
            save_data(data)
            print("\nProgression sauvegardée. À bientôt, opérateur.")
            break
        else:
            print("Option invalide.")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterruption demandée. Relance le programme pour continuer.")
