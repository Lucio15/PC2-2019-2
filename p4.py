import random

pares =  0

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



for i in range (N):
    for j in range (N):
        if matriz [i][j] % 2 == 0 :
            pares = pares + 1

print("La cantidad de números pares en la matriz es : ",pares)