factoriel = 1
n = int(input("Saisir la valeur de n: "))
for i in range(1, n+1):
    factoriel = factoriel * i
print("Le factoriel de n est : ", factoriel)