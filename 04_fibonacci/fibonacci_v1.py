nb_termes = input("Combien de termes voulez-vous ? ")

if nb_termes.isdigit():
    nb_termes = int(nb_termes)
    compteur = 0
    a = 0
    b = 1

    while compteur < nb_termes:
        print(a)

        temp = a
        a = b
        b = temp + b

        compteur = compteur + 1
else:
    print("Veuillez entrer un nombre")
