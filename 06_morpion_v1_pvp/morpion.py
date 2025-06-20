case_vide = " "

plateau = [case_vide for i in range(9)]

symboles = ("❌", "⭕")
placeholder = ("1️⃣ ", "2️⃣ ", "3️⃣ ", "4️⃣ ", "5️⃣ ", "6️⃣ ", "7️⃣ ", "8️⃣ ", "9️⃣ ")

joueur = symboles[0]

def afficher_plateau():
    print(" ----+----+----")
    for i in range(9):
        print("|", plateau[i] if plateau[i] != case_vide else placeholder[i], end=" ")
        if i % 3 == 2:
            print("|")
            print(" ----+----+----")


while True:
    afficher_plateau()
    choix_joueur = 0

    while choix_joueur < 1 or choix_joueur > 9 or plateau[choix_joueur - 1] != case_vide:
        choix_joueur = int(input("Entrez une case entre 1 et 9 : "))

    plateau[choix_joueur - 1] = joueur

    if case_vide != plateau[0] == plateau[1] == plateau[2] \
    or case_vide != plateau[3] == plateau[4] == plateau[5] \
    or case_vide != plateau[6] == plateau[7] == plateau[8] \
    or case_vide != plateau[0] == plateau[3] == plateau[6] \
    or case_vide != plateau[1] == plateau[4] == plateau[7] \
    or case_vide != plateau[2] == plateau[5] == plateau[8] \
    or case_vide != plateau[0] == plateau[4] == plateau[8] \
    or case_vide != plateau[2] == plateau[4] == plateau[6]:
        print("Le joueur", joueur, "gagne la partie !")
        afficher_plateau()
        break

    joueur = symboles[1] if joueur == symboles[0] else symboles[0]
