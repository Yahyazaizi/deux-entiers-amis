
def somme_diviseurs(nombre):
    somme = 0
    for diviseur in range(1, nombre // 2 + 1):
        if nombre % diviseur == 0:
            somme += diviseur
    return somme


M = int(input("Entrez le premier entier M : "))
N = int(input("Entrez le deuxième entier N : "))


somme_diviseurs_M = somme_diviseurs(M)
somme_diviseurs_N = somme_diviseurs(N)


sont_amis = somme_diviseurs_M == N and somme_diviseurs_N == M


if sont_amis:
    print(f"{M} et {N} ne sont pas des nombres amis.")
else:
    print(f"{M} et {N} sont des nombres amis.")
   
