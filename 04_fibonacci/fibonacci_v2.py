def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=("\n" if i == n - 1 else " "))
        a, b = b, a + b


if __name__ == "__main__":
    nb_termes = input("Combien de termes voulez-vous ? ")

    if nb_termes.isdigit():
        nb_termes = int(nb_termes)
        fibonacci(nb_termes)
else:
    print("Veuillez entrer un nombre")
