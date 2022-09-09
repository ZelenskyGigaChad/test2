def compteur_de_mots():
    chaine = input("Votre phrase : ")
    print(len(chaine.split(" ")), "mots")
quitter = ""
while quitter != "oui" or "OUI":
    compteur_de_mots()
    quitter = input("Voulez-vous quitter? : ")