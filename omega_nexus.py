import json
import os
import random
import time
import hashlib
import platform
import socket
import getpass
from datetime import datetime

# ============================================================
# OMEGA NEXUS v1.0
# LABORATOIRE INTERACTIF DE PROGRAMMATION ET CYBERSÉCURITÉ
# Python Standard Library uniquement
# ============================================================

VERSION = "1.0"
SAVE_FILE = "omega_nexus_save.json"

# ============================================================
# CONFIGURATION
# ============================================================

class Config:
    NAME = "OMEGA NEXUS"
    VERSION = VERSION
    AUTHOR = "OMEGA SYSTEMS"
    MAX_HISTORY = 100


# ============================================================
# COULEURS TERMINAL
# ============================================================

class Colors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    PURPLE = "\033[95m"
    BOLD = "\033[1m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(Colors.CYAN + Colors.BOLD)
    print("""
     ██████╗ ███╗   ███╗███████╗ ██████╗  █████╗
    ██╔═══██╗████╗ ████║██╔════╝██╔════╝ ██╔══██╗
    ██║   ██║██╔████╔██║█████╗  ██║  ███╗███████║
    ██║   ██║██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║
    ╚██████╔╝██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║
     ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝

             N E X U S   v1.0
    """)
    print(Colors.RESET)


# ============================================================
# DONNÉES DU SYSTÈME
# ============================================================

class Database:

    def __init__(self):
        self.data = {
            "username": getpass.getuser(),
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "level": 1,
            "xp": 0,
            "missions_completed": 0,
            "history": [],
            "notes": [],
            "password_hashes": []
        }

        self.load()

    def load(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r", encoding="utf-8") as file:
                    saved = json.load(file)
                    self.data.update(saved)
            except (json.JSONDecodeError, OSError):
                print(Colors.RED + "[!] Impossible de charger la sauvegarde.")

    def save(self):
        try:
            with open(SAVE_FILE, "w", encoding="utf-8") as file:
                json.dump(self.data, file, indent=4, ensure_ascii=False)
        except OSError:
            print(Colors.RED + "[!] Erreur de sauvegarde.")

    def add_history(self, action):
        self.data["history"].append({
            "action": action,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        self.data["history"] = self.data["history"][-Config.MAX_HISTORY:]
        self.save()

    def add_xp(self, amount):
        self.data["xp"] += amount

        while self.data["xp"] >= self.data["level"] * 100:
            self.data["xp"] -= self.data["level"] * 100
            self.data["level"] += 1
            print(Colors.GREEN + "\n[+] NIVEAU SUPÉRIEUR !")

        self.save()


db = Database()


# ============================================================
# OUTILS GÉNÉRAUX
# ============================================================

def pause():
    input("\nAppuie sur Entrée pour continuer...")


def header(title):
    clear()
    banner()
    print(Colors.YELLOW + f"=== {title} ===\n" + Colors.RESET)


def success(message):
    print(Colors.GREEN + "[+] " + message + Colors.RESET)


def error(message):
    print(Colors.RED + "[-] " + message + Colors.RESET)


def information(message):
    print(Colors.CYAN + "[i] " + message + Colors.RESET)


def ask(prompt):
    return input(Colors.YELLOW + prompt + Colors.RESET)


# ============================================================
# MODULE 1 : PROFIL SYSTÈME
# ============================================================

def system_information():

    header("INFORMATIONS SYSTÈME")

    print("Utilisateur :", getpass.getuser())
    print("Système :", platform.system())
    print("Version :", platform.version())
    print("Architecture :", platform.machine())
    print("Processeur :", platform.processor())
    print("Python :", platform.python_version())
    print("Nom de machine :", platform.node())
    print("Date :", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    db.add_history("Consultation des informations système")
    db.add_xp(5)

    pause()


# ============================================================
# MODULE 2 : GÉNÉRATEUR DE MOTS DE PASSE
# ============================================================

def password_generator():

    header("GÉNÉRATEUR DE MOTS DE PASSE")

    try:
        length = int(ask("Longueur du mot de passe : "))

        if not 8 <= length <= 128:
            error("La longueur doit être comprise entre 8 et 128.")
            pause()
            return

        characters = (
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "0123456789"
            "!@#$%^&*()-_=+"
        )

        password = "".join(
            random.SystemRandom().choices(characters, k=length)
        )

        print("\nMot de passe généré :")
        print(Colors.GREEN + Colors.BOLD + password + Colors.RESET)

        db.add_history("Génération d'un mot de passe")
        db.add_xp(10)

    except ValueError:
        error("Veuillez entrer un nombre valide.")

    pause()


# ============================================================
# MODULE 3 : ANALYSEUR DE MOT DE PASSE
# ============================================================

def password_analyzer():

    header("ANALYSEUR DE MOT DE PASSE")

    password = ask("Mot de passe à analyser : ")

    if not password:
        error("Mot de passe vide.")
        pause()
        return

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(not c.isalnum() for c in password):
        score += 1

    levels = {
        0: "TRÈS FAIBLE",
        1: "TRÈS FAIBLE",
        2: "FAIBLE",
        3: "MOYEN",
        4: "BON",
        5: "FORT",
        6: "TRÈS FORT"
    }

    print("\nRésultat :", levels[score])
    print("Score :", score, "/ 6")

    if len(password) < 12:
        information("Utilise au moins 12 caractères.")

    if not any(c.isdigit() for c in password):
        information("Ajoute des chiffres.")

    if not any(not c.isalnum() for c in password):
        information("Ajoute des caractères spéciaux.")

    db.add_history("Analyse de mot de passe")
    db.add_xp(10)

    pause()


# ============================================================
# MODULE 4 : GÉNÉRATEUR DE HASH
# ============================================================

def hash_generator():

    header("GÉNÉRATEUR DE HASH")

    text = ask("Texte à hacher : ")

    if not text:
        error("Aucun texte fourni.")
        pause()
        return

    encoded = text.encode("utf-8")

    algorithms = {
        "MD5": hashlib.md5(encoded).hexdigest(),
        "SHA1": hashlib.sha1(encoded).hexdigest(),
        "SHA256": hashlib.sha256(encoded).hexdigest(),
        "SHA512": hashlib.sha512(encoded).hexdigest()
    }

    for name, result in algorithms.items():
        print(f"\n{name} : {result}")

    information("SHA-256 et SHA-512 sont préférables pour les empreintes modernes.")

    db.add_history("Génération de hash")
    db.add_xp(10)

    pause()


# ============================================================
# MODULE 5 : VÉRIFICATEUR DE HASH
# ============================================================

def hash_verifier():

    header("VÉRIFICATEUR DE HASH SHA-256")

    original = ask("Texte original : ")
    expected = ask("Hash SHA-256 attendu : ")

    calculated = hashlib.sha256(
        original.encode("utf-8")
    ).hexdigest()

    if hashlib.sha256(expected.encode()).digest() == hashlib.sha256(calculated.encode()).digest():
        success("Comparaison effectuée.")

    if calculated.lower() == expected.strip().lower():
        success("Le hash correspond.")
    else:
        error("Le hash ne correspond pas.")

    db.add_history("Vérification de hash")
    db.add_xp(10)

    pause()


# ============================================================
# MODULE 6 : OUTILS RÉSEAU
# ============================================================

def network_information():

    header("INFORMATIONS RÉSEAU")

    hostname = socket.gethostname()

    print("Nom de machine :", hostname)

    try:
        addresses = socket.getaddrinfo(hostname, None)

        unique_addresses = set()

        for address in addresses:
            unique_addresses.add(address[4][0])

        print("\nAdresses IP locales :")

        for ip in unique_addresses:
            print("-", ip)

    except socket.gaierror:
        error("Impossible de récupérer les adresses réseau.")

    db.add_history("Consultation réseau")
    db.add_xp(10)

    pause()


# ============================================================
# MODULE 7 : VÉRIFICATION DE PORTS LOCAUX
# ============================================================

def port_scanner():

    header("SCANNER DE PORTS")

    target = ask("Adresse IP ou nom de machine : ")

    if target.lower() in ("localhost", "127.0.0.1", "::1"):
        target = "127.0.0.1"

    try:
        ip = socket.gethostbyname(target)

        print(f"\nCible : {ip}")

        ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

        for port in ports:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))

            if result == 0:
                success(f"Port {port} : OUVERT")
            else:
                print(f"Port {port} : fermé ou filtré")

            sock.close()

        db.add_history(f"Scan de ports : {target}")
        db.add_xp(15)

    except socket.gaierror:
        error("Adresse invalide ou introuvable.")

    except OSError as exc:
        error(f"Erreur réseau : {exc}")

    pause()


# ============================================================
# MODULE 8 : CALCULATRICE SCIENTIFIQUE
# ============================================================

def calculator():

    header("CALCULATRICE SCIENTIFIQUE")

    print("""
    1. Addition
    2. Soustraction
    3. Multiplication
    4. Division
    5. Puissance
    6. Racine carrée
    """)

    choice = ask("Choix : ")

    try:

        if choice == "6":
            number = float(ask("Nombre : "))

            if number < 0:
                error("Impossible de calculer la racine carrée réelle.")
            else:
                success(f"Résultat : {number ** 0.5}")

        else:
            a = float(ask("Premier nombre : "))
            b = float(ask("Deuxième nombre : "))

            if choice == "1":
                result = a + b

            elif choice == "2":
                result = a - b

            elif choice == "3":
                result = a * b

            elif choice == "4":
                if b == 0:
                    error("Division par zéro impossible.")
                    pause()
                    return
                result = a / b

            elif choice == "5":
                result = a ** b

            else:
                error("Option inconnue.")
                pause()
                return

            success(f"Résultat : {result}")

        db.add_history("Calcul scientifique")
        db.add_xp(5)

    except ValueError:
        error("Entrée numérique invalide.")

    except OverflowError:
        error("Résultat trop grand.")

    pause()


# ============================================================
# MODULE 9 : NOTES PERSONNELLES
# ============================================================

def notes_manager():

    while True:

        header("GESTIONNAIRE DE NOTES")

        print("""
        1. Ajouter une note
        2. Afficher les notes
        3. Supprimer une note
        0. Retour
        """)

        choice = ask("Choix : ")

        if choice == "1":

            note = ask("Contenu de la note : ")

            if note.strip():
                db.data["notes"].append({
                    "content": note,
                    "date": datetime.now().strftime("%d/%m/%Y %H:%M")
                })

                db.save()
                success("Note enregistrée.")
                db.add_xp(5)

        elif choice == "2":

            if not db.data["notes"]:
                information("Aucune note enregistrée.")

            for index, note in enumerate(db.data["notes"], 1):
                print(f"{index}. {note['content']}")
                print("   Date :", note["date"])

            pause()

        elif choice == "3":

            if not db.data["notes"]:
                information("Aucune note à supprimer.")
                pause()
                continue

            for index, note in enumerate(db.data["notes"], 1):
                print(f"{index}. {note['content']}")

            try:
                number = int(ask("Numéro de la note : "))

                if 1 <= number <= len(db.data["notes"]):
                    db.data["notes"].pop(number - 1)
                    db.save()
                    success("Note supprimée.")
                else:
                    error("Numéro invalide.")

            except ValueError:
                error("Entrée invalide.")

            pause()

        elif choice == "0":
            break

        else:
            error("Option inconnue.")
            pause()


# ============================================================
# MODULE 10 : HISTORIQUE
# ============================================================

def history():

    header("HISTORIQUE DES ACTIVITÉS")

    activities = db.data["history"]

    if not activities:
        information("Aucune activité enregistrée.")

    else:
        for activity in activities[-20:]:
            print(f"[{activity['date']}] {activity['action']}")

    pause()


# ============================================================
# MODULE 11 : TABLEAU DE BORD
# ============================================================

def dashboard():

    header("TABLEAU DE BORD")

    print("Utilisateur :", db.data["username"])
    print("Niveau :", db.data["level"])
    print("XP :", db.data["xp"])
    print("Missions terminées :", db.data["missions_completed"])
    print("Notes enregistrées :", len(db.data["notes"]))
    print("Activités :", len(db.data["history"]))

    required = db.data["level"] * 100

    print(f"\nProgression : {db.data['xp']} / {required} XP")

    percentage = min(100, int(db.data["xp"] / required * 100))

    print("[" + "#" * (percentage // 5) + "-" * (20 - percentage // 5) + "]")
    print(f"{percentage}%")

    pause()


# ============================================================
# MODULE 12 : LABORATOIRE PÉDAGOGIQUE
# ============================================================

def cyber_lab():

    while True:

        header("LABORATOIRE CYBERSÉCURITÉ")

        print("""
        1. Comprendre le hachage
        2. Comprendre les ports réseau
        3. Comprendre les mots de passe
        4. Comprendre le phishing
        5. Comprendre le chiffrement
        0. Retour
        """)

        choice = ask("Choix : ")

        lessons = {
            "1": (
                "HACHAGE",
                "Le hachage transforme une donnée en empreinte.\n"
                "Il est conçu pour être difficilement réversible.\n"
                "Exemple : SHA-256."
            ),
            "2": (
                "PORTS RÉSEAU",
                "Un port identifie un service sur une machine.\n"
                "HTTP utilise généralement le port 80.\n"
                "HTTPS utilise généralement le port 443.\n"
                "SSH utilise généralement le port 22."
            ),
            "3": (
                "SÉCURITÉ DES MOTS DE PASSE",
                "Un bon mot de passe doit être long et unique.\n"
                "Un gestionnaire de mots de passe est recommandé.\n"
                "Les systèmes modernes utilisent Argon2id, scrypt ou bcrypt."
            ),
            "4": (
                "PHISHING",
                "Le phishing est une technique d'ingénierie sociale.\n"
                "L'attaquant cherche à tromper une victime.\n"
                "Vérifie toujours les liens et l'identité de l'expéditeur."
            ),
            "5": (
                "CHIFFREMENT",
                "Le chiffrement protège la confidentialité des données.\n"
                "AES est un algorithme de chiffrement symétrique.\n"
                "RSA est un algorithme cryptographique asymétrique."
            )
        }

        if choice in lessons:

            title, content = lessons[choice]

            print("\n" + Colors.CYAN + title + Colors.RESET)
            print(content)

            db.add_xp(5)
            db.add_history(f"Leçon : {title}")

            pause()

        elif choice == "0":
            break

        else:
            error("Option inconnue.")
            pause()


# ============================================================
# MODULE 13 : MINI-JEU DE LOGIQUE
# ============================================================

def logic_game():

    header("DÉFI DE LOGIQUE")

    secret = random.randint(1, 100)
    attempts = 0

    print("Devine le nombre secret entre 1 et 100.")

    while True:

        try:
            guess = int(ask("Ta réponse : "))
            attempts += 1

            if guess < secret:
                information("Trop petit.")

            elif guess > secret:
                information("Trop grand.")

            else:
                success(f"Trouvé en {attempts} tentative(s) !")
                db.add_xp(max(5, 30 - attempts))
                db.data["missions_completed"] += 1
                db.save()
                db.add_history("Défi de logique réussi")
                break

        except ValueError:
            error("Entre un nombre entier.")

    pause()


# ============================================================
# MODULE 14 : VÉRIFICATION DE FICHIERS
# ============================================================

def file_hash():

    header("EMPREINTE D'UN FICHIER")

    path = ask("Chemin du fichier : ")

    if not os.path.isfile(path):
        error("Fichier introuvable.")
        pause()
        return

    try:
        digest = hashlib.sha256()

        with open(path, "rb") as file:

            for chunk in iter(lambda: file.read(4096), b""):
                digest.update(chunk)

        print("\nSHA-256 :")
        print(Colors.GREEN + digest.hexdigest() + Colors.RESET)

        success("Empreinte calculée.")

        db.add_xp(10)
        db.add_history("Calcul d'empreinte de fichier")

    except OSError as exc:
        error(str(exc))

    pause()


# ============================================================
# MENU PRINCIPAL
# ============================================================

def main():

    while True:

        header("CENTRE DE COMMANDE")

        print(f"Utilisateur : {db.data['username']}")
        print(f"Niveau : {db.data['level']} | XP : {db.data['xp']}")

        print("""
        [01] Informations système
        [02] Générateur de mots de passe
        [03] Analyseur de mots de passe
        [04] Générateur de hash
        [05] Vérificateur de hash
        [06] Informations réseau
        [07] Scanner de ports
        [08] Calculatrice scientifique
        [09] Gestionnaire de notes
        [10] Historique des activités
        [11] Tableau de bord
        [12] Laboratoire cybersécurité
        [13] Défi de logique
        [14] Empreinte de fichier

        [00] Quitter OMEGA NEXUS
        """)

        choice = ask("OMEGA NEXUS > ")

        modules = {
            "1": system_information,
            "01": system_information,
            "2": password_generator,
            "02": password_generator,
            "3": password_analyzer,
            "03": password_analyzer,
            "4": hash_generator,
            "04": hash_generator,
            "5": hash_verifier,
            "05": hash_verifier,
            "6": network_information,
            "06": network_information,
            "7": port_scanner,
            "07": port_scanner,
            "8": calculator,
            "08": calculator,
            "9": notes_manager,
            "09": notes_manager,
            "10": history,
            "11": dashboard,
            "12": cyber_lab,
            "13": logic_game,
            "14": file_hash
        }

        if choice in modules:

            try:
                modules[choice]()

            except KeyboardInterrupt:
                print("\n")
                information("Opération interrompue.")

            except Exception as exc:
                error(f"Erreur inattendue : {exc}")
                pause()

        elif choice in ("0", "00"):

            db.save()

            print(Colors.GREEN + """
            =====================================
                  OMEGA NEXUS v1.0
                  SESSION TERMINÉE
            =====================================
            """ + Colors.RESET)

            break

        else:
            error("Commande inconnue.")
            time.sleep(1)


# ============================================================
# DÉMARRAGE
# ============================================================

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\nOMEGA NEXUS : arrêt demandé.")
        db.save()