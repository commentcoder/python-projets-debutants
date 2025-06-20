import random

print("Bienvenue dans le jeu du Prix Mystère !")
print("Le but du jeu est de deviner un nombre entre 1 et 100.")

prix = random.randint(1, 100)

tentatives = 0
trouve = False

while not trouve:
    guess = int(input("Votre propostion : "))
    tentatives += 1

    if guess < prix:
        print("C'est plus 🔼")
    elif guess > prix:
        print("C'est moins 🔽")
    else:
        print("Bravo, vous avez trouvé le prix mystère ", prix, "en", tentatives, "tentatives")
        trouve = True
