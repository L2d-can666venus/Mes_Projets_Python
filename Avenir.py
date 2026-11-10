import json
import os
from datetime import datetime

# ============================================================
#                  MECLISH OS v1.0
#       PERSONAL DEVELOPMENT & TECHNOLOGY SYSTEM
# ============================================================

APP_NAME = "MECLISH OS"
VERSION = "1.0"
SAVE_FILE = "meclish_data.json"


# ============================================================
#                     INITIAL DATABASE
# ============================================================

DEFAULT_DATA = {
    "profile": {
        "username": "MECLISH",
        "role": "Developer in Progress",
        "ambition": "Become an expert in programming and cybersecurity"
    },

    "roadmap": {
        "Programming": [
            "Python fundamentals",
            "Algorithms and logic",
            "Object-oriented programming",
            "Git and GitHub",
            "HTML / CSS / JavaScript",
            "Databases",
            "Web development",
            "API development",
            "Software engineering",
            "Application development",
            "Game development"
        ],

        "Cybersecurity": [
            "Linux fundamentals",
            "Kali Linux",
            "Computer networks",
            "TCP/IP and DNS",
            "Nmap",
            "Network security",
            "Web security",
            "Ethical hacking",
            "Penetration testing in authorized labs",
            "Defensive cybersecurity",
            "Digital forensics",
            "Cryptography"
        ],

        "University": [
            "General English",
            "Translation",
            "Interpretation",
            "Localization",
            "Grammar and vocabulary",
            "Academic writing",
            "Linguistics",
            "Communication skills"
        ],

        "Personal Development": [
            "Discipline",
            "Concentration",
            "Time management",
            "Independent learning",
            "Critical thinking",
            "Consistency",
            "Self-confidence"
        ]
    },

    "projects": [
        {
            "name": "Omega Nexus",
            "description": "Interactive programming and cybersecurity laboratory",
            "status": "In development"
        },
        {
            "name": "Kivora",
            "description": "Web development project",
            "status": "In development"
        },
        {
            "name": "Lunati",
            "description": "Python game project",
            "status": "Planned"
        },
        {
            "name": "Mes Projets Python",
            "description": "Personal Python development portfolio",
            "status": "Active"
        }
    ],

    "tasks": [],
    "journal": [],
    "completed": [],
    "skills": {},
    "daily_goals": []
}


# ============================================================
#                     DATABASE SYSTEM
# ============================================================

def load_data():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as file:
                saved = json.load(file)

            for key, value in DEFAULT_DATA.items():
                if key not in saved:
                    saved[key] = value

            return saved

        except (json.JSONDecodeError, OSError):
            print("[!] Database unavailable. Loading default data.")

    return DEFAULT_DATA.copy()


data = load_data()


def save_data():
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except OSError:
        print("[!] Unable to save database.")


# ============================================================
#                     INTERFACE SYSTEM
# ============================================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def header():
    print("=" * 65)
    print("                     MECLISH OS")
    print("              PERSONAL CONTROL CENTER")
    print(f"                     VERSION {VERSION}")
    print("=" * 65)


def pause():
    input("\nPress ENTER to continue...")


def section(title):
    clear()
    header()
    print(f"\n[ {title.upper()} ]\n")


# ============================================================
#                     DASHBOARD
# ============================================================

def dashboard():
    section("Dashboard")

    profile = data["profile"]

    print(f"USER              : {profile['username']}")
    print(f"ROLE              : {profile['role']}")
    print(f"AMBITION          : {profile['ambition']}")

    print("\n" + "-" * 65)

    print(f"ACTIVE TASKS      : {len(data['tasks'])}")
    print(f"COMPLETED TASKS   : {len(data['completed'])}")
    print(f"PROJECTS          : {len(data['projects'])}")
    print(f"JOURNAL ENTRIES   : {len(data['journal'])}")
    print(f"SKILLS REGISTERED : {len(data['skills'])}")

    print("\nSYSTEM STATUS: OPERATIONAL")
    print(f"CURRENT DATE: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    pause()


# ============================================================
#                     LEARNING ROADMAP
# ============================================================

def roadmap():

    categories = list(data["roadmap"].keys())

    while True:
        section("Learning Roadmap")

        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")

        print("0. Back")

        choice = input("\nSelect a category: ")

        if choice == "0":
            return

        if not choice.isdigit():
            continue

        index = int(choice) - 1

        if 0 <= index < len(categories):

            category = categories[index]

            section(category)

            for i, topic in enumerate(data["roadmap"][category], 1):
                print(f"{i}. {topic}")

            pause()


# ============================================================
#                     PROJECT MANAGER
# ============================================================

def projects():

    while True:
        section("Project Manager")

        for i, project in enumerate(data["projects"], 1):
            print(f"\n{i}. {project['name']}")
            print(f"   Description: {project['description']}")
            print(f"   Status: {project['status']}")

        print("\n1. Add project")
        print("2. Update project status")
        print("0. Back")

        choice = input("\nChoice: ")

        if choice == "0":
            return

        elif choice == "1":

            name = input("Project name: ").strip()
            description = input("Description: ").strip()

            if name:
                data["projects"].append({
                    "name": name,
                    "description": description,
                    "status": "Planned"
                })

                save_data()
                print("[+] Project created.")

            pause()

        elif choice == "2":

            number = input("Project number: ")

            if number.isdigit():

                index = int(number) - 1

                if 0 <= index < len(data["projects"]):

                    status = input(
                        "New status (Planned/Active/In development/Completed): "
                    ).strip()

                    if status:
                        data["projects"][index]["status"] = status
                        save_data()
                        print("[+] Status updated.")

            pause()


# ============================================================
#                     TASK MANAGER
# ============================================================

def task_manager():

    while True:
        section("Task Manager")

        if not data["tasks"]:
            print("No active tasks.")

        for i, task in enumerate(data["tasks"], 1):
            print(f"\n{i}. {task['title']}")
            print(f"   Priority: {task['priority']}")
            print(f"   Created: {task['date']}")

        print("\n1. Add task")
        print("2. Complete task")
        print("3. View completed tasks")
        print("0. Back")

        choice = input("\nChoice: ")

        if choice == "0":
            return

        elif choice == "1":

            title = input("Task description: ").strip()

            if not title:
                continue

            priority = input("Priority (Low/Medium/High): ").strip()

            if priority.lower() not in ["low", "medium", "high"]:
                priority = "Medium"

            data["tasks"].append({
                "title": title,
                "priority": priority,
                "date": datetime.now().strftime("%Y-%m-%d")
            })

            save_data()
            print("[+] Task added.")

            pause()

        elif choice == "2":

            if not data["tasks"]:
                pause()
                continue

            number = input("Task number: ")

            if number.isdigit():

                index = int(number) - 1

                if 0 <= index < len(data["tasks"]):

                    task = data["tasks"].pop(index)

                    task["completed_at"] = datetime.now().isoformat()

                    data["completed"].append(task)

                    save_data()

                    print("[+] Task completed.")

            pause()

        elif choice == "3":

            section("Completed Tasks")

            for task in data["completed"]:
                print(f"[DONE] {task['title']}")

            pause()


# ============================================================
#                     PERSONAL JOURNAL
# ============================================================

def journal():

    while True:
        section("Personal Journal")

        print("1. Write an entry")
        print("2. Read previous entries")
        print("0. Back")

        choice = input("\nChoice: ")

        if choice == "0":
            return

        elif choice == "1":

            section("New Journal Entry")

            content = input("Write your thoughts:\n\n").strip()

            if content:

                data["journal"].append({
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "content": content
                })

                save_data()

                print("\n[+] Entry saved.")

            pause()

        elif choice == "2":

            section("Journal History")

            if not data["journal"]:
                print("No entries available.")

            for entry in data["journal"]:
                print(f"\n[{entry['date']}]")
                print(entry["content"])
                print("-" * 45)

            pause()


# ============================================================
#                     SKILLS TRACKER
# ============================================================

def skills_tracker():

    while True:
        section("Skills Tracker")

        if not data["skills"]:
            print("No skills registered.")

        for skill, level in data["skills"].items():
            print(f"{skill}: {level}/100")

        print("\n1. Add or update skill")
        print("2. Remove skill")
        print("0. Back")

        choice = input("\nChoice: ")

        if choice == "0":
            return

        elif choice == "1":

            skill = input("Skill name: ").strip()

            if not skill:
                continue

            level = input("Level (0-100): ")

            if level.isdigit() and 0 <= int(level) <= 100:

                data["skills"][skill] = int(level)

                save_data()

                print("[+] Skill updated.")

            pause()

        elif choice == "2":

            skill = input("Skill name to remove: ").strip()

            if skill in data["skills"]:
                del data["skills"][skill]
                save_data()
                print("[+] Skill removed.")

            pause()


# ============================================================
#                     DAILY GOALS
# ============================================================

def daily_goals():

    while True:
        section("Daily Goals")

        for i, goal in enumerate(data["daily_goals"], 1):
            status = "DONE" if goal["completed"] else "PENDING"
            print(f"{i}. [{status}] {goal['title']}")

        print("\n1. Add daily goal")
        print("2. Complete daily goal")
        print("0. Back")

        choice = input("\nChoice: ")

        if choice == "0":
            return

        elif choice == "1":

            title = input("Goal: ").strip()

            if title:

                data["daily_goals"].append({
                    "title": title,
                    "completed": False,
                    "date": datetime.now().strftime("%Y-%m-%d")
                })

                save_data()

                print("[+] Goal added.")

            pause()

        elif choice == "2":

            number = input("Goal number: ")

            if number.isdigit():

                index = int(number) - 1

                if 0 <= index < len(data["daily_goals"]):

                    data["daily_goals"][index]["completed"] = True

                    save_data()

                    print("[+] Goal completed.")

            pause()


# ============================================================
#                     PROGRESS STATISTICS
# ============================================================

def statistics():

    section("Progress Statistics")

    total = len(data["tasks"]) + len(data["completed"])
    completed = len(data["completed"])

    percentage = (completed / total * 100) if total else 0

    print(f"Total tasks       : {total}")
    print(f"Completed tasks   : {completed}")
    print(f"Remaining tasks   : {len(data['tasks'])}")
    print(f"Completion rate   : {percentage:.1f}%")

    print("\nPROJECT OVERVIEW")

    for project in data["projects"]:
        print(f"{project['name']} -> {project['status']}")

    print("\nSKILLS OVERVIEW")

    for skill, level in data["skills"].items():
        print(f"{skill}: {level}%")

    pause()


# ============================================================
#                     SYSTEM SETTINGS
# ============================================================

def settings():

    section("System Settings")

    print("1. Change username")
    print("2. Change ambition")
    print("3. Save data")
    print("0. Back")

    choice = input("\nChoice: ")

    if choice == "1":

        username = input("New username: ").strip()

        if username:
            data["profile"]["username"] = username
            save_data()

    elif choice == "2":

        ambition = input("New ambition: ").strip()

        if ambition:
            data["profile"]["ambition"] = ambition
            save_data()

    elif choice == "3":

        save_data()
        print("[+] Data saved.")

    pause()


# ============================================================
#                     MAIN CONTROL CENTER
# ============================================================

def main():

    while True:

        section("Main Control Center")

        print("""
[1] Dashboard
[2] Learning Roadmap
[3] Project Manager
[4] Task Manager
[5] Personal Journal
[6] Skills Tracker
[7] Daily Goals
[8] Progress Statistics
[9] System Settings

[0] Shutdown
""")

        choice = input("MECLISH@OS > ").strip()

        if choice == "1":
            dashboard()

        elif choice == "2":
            roadmap()

        elif choice == "3":
            projects()

        elif choice == "4":
            task_manager()

        elif choice == "5":
            journal()

        elif choice == "6":
            skills_tracker()

        elif choice == "7":
            daily_goals()

        elif choice == "8":
            statistics()

        elif choice == "9":
            settings()

        elif choice == "0":

            save_data()

            clear()

            print("=" * 65)
            print("                  MECLISH OS")
            print("                  SHUTDOWN")
            print("              ALL DATA SAVED")
            print("=" * 65)

            break

        else:

            print("\n[!] Invalid command.")
            pause()


# ============================================================
#                     PROGRAM EXECUTION
# ============================================================

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:

        save_data()

        print("\n[!] Program interrupted.")
        print("[+] Data saved successfully.")