FILENAME = "contacts.txt"

# 1. Afficher les contacts qui se trouvent dans le fichier
def afficher_contacts(contacts):
    if not contacts:
        print("Auncun contact.")
        return

    print(f"\nVos {len(contacts)} contacts :")
    for i, (nom, telephone) in enumerate(contacts, 1):
        print(f"{i}. {nom} - {telephone}")


def charger_contacts():
    contacts = []

    try:
        with open(FILENAME, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                if ligne:
                    nom, telephone = ligne.split(";")
                    contacts.append([nom, telephone])
            print(f"\n{len(contacts)} contact(s) chargés")
    except FileNotFoundError:
        print("Nouveau fichier de contacts")

    return contacts


# 2. Créer des contacts
def ajouter_contact(contacts):
    print("\nAjouter un contact :")
    nom = input("Nom : ").strip()
    telephone = input("Téléphone : ").strip()

    if nom and telephone:
        contacts.append([nom, telephone])
        print(f"{nom} ajouté !")
    else:
        print("Nom et téléphone obligatoires")


# 3. Sauver les contacts et quitter le programme
def sauvegarder_contacts(contacts):
    with open(FILENAME, "w", encoding="utf-8") as fichier:
        for nom, telephone in contacts:
            fichier.write(f"{nom};{telephone}\n")
    print(f"{len(contacts)} contacts enregistrés")


def menu():
    print("=== GESTIONNAIRE DE CONTACTS ===")

    contacts = charger_contacts()

    while True:
        print("\n Que voulez-vous faire ?")
        print("1. Voir les contacts")
        print("2. Ajouter un contact")
        print("3. Sauver et quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            afficher_contacts(contacts)
        elif choix == "2":
            ajouter_contact(contacts)
        elif choix == "3":
            sauvegarder_contacts(contacts)
            print("Au revoir !")
            break
        else:
            print("Choix invalide")


if __name__ == "__main__":
    menu()
