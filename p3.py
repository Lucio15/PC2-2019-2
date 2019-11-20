#Lucio Tuncar

alumnos = []

for i in range (3):
    alumnos.append([0]*3)
    for j in range (5):
        alumnos.append([0]*5)

for i in range (1):
    for j in range (5):
        nombre = str(input("Ingrese su nombre : "))
        alumnos.append(nombre)


for i in range (2):
    for j in range (5):
        edad = str(input("Ingrese su edad : "))
        alumnos.append(edad)

for i in range (3):
    for j in range (5):
        sexo = str(input("Ingrese su sexo : "))
        alumnos.append(sexo)


for i in range (3):
    for j in range (5):
        print (alumnos[i][j], end=" ")
    print("")