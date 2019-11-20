import random

N = int(input("Ingrese el número N : "))
while N < 2 or N > 5 :
    print("Error numero ingresado es incorrecto")
    N = int(input("Ingrese el número N : "))

matriz = []

for i in range (N):
    matriz.append([0]*N)
    for j in range (N):
        matriz [i][j] = random.randint(1,100)

for i in range (N):
    for j in range (N):
        print (matriz[i][j], end=" ")
    print("")