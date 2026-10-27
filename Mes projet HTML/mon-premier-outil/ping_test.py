import subprocess

cible = "8.8.8.8"

resultat = subprocess.run(
    ["ping", "-n", "4", cible],
    capture_output=True,
    text=True,
    encoding="cp850",
    errors="replace",
)

print(resultat.stdout)