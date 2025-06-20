import random

def obtenir_coup(plateau, x, o, case_vide):
    lignes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]
    ]

    # 1. Gagner si on peut
    for ligne in lignes:
        vals = [plateau[i] for i in ligne]
        if vals.count(o) == 2 and vals.count(case_vide) == 1:
            return ligne[vals.index(case_vide)]

    # 2. Bloquer si besoin
    for ligne in lignes:
        vals = [plateau[i] for i in ligne]
        if vals.count(x) == 2 and vals.count(case_vide) == 1:
            return ligne[vals.index(case_vide)]

    # 3. Continuer une ligne
    for ligne in lignes:
        vals = [plateau[i] for i in ligne]
        if vals.count(o) == 1 and vals.count(case_vide) == 2:
            return ligne[vals.index(case_vide)]

    # 4. Placer au centre
    if plateau[4] == case_vide:
        return 4

    # 5. Placer dans un coin
    coins = [0, 2, 6, 8]
    coins_libres = [c for c in coins if plateau[c] == case_vide]
    if coins_libres:
        return random.choice(coins_libres)

    # 6. Place sur une case vide
    cases_libres = [i for i, val in enumerate(plateau) if val == case_vide]
    if cases_libres:
        return random.choice(cases_libres)
    else:
        return -1


if __name__ == "__main__":
    plateau = [" ", " ", " ", " ", "X", " ", " ", " ", " "]
    choix_ordi = obtenir_coup(plateau, "X", "O", " ")
    print(choix_ordi)
