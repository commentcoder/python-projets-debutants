def fibonacci(n):
    compteur = 0
    a = 0
    b = 1

    while compteur < n:
        print(a)
        temp = a
        a = b
        b = temp + b
        compteur = compteur + 1

n = int(input("Combien de termes ? "))
fibonacci(n)
