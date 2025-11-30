import random  # Librería para generar números aleatorios

# =========================
# EJERCICIO 1
# =========================
print("Ejercicio 1")
m = []  # Lista vacía que será nuestra matriz de 3x3

# Bucle para generar la matriz
for i in range(3):  # Recorre las filas (0, 1, 2)
    m.append([])  # Agrega una lista vacía para la nueva fila
    for j in range(3):  # Recorre las columnas (0, 1, 2)
        m[i].append(random.randint(1, 10))  # Agrega un número aleatorio de 1 a 10
        print(m[i][j], end="")  # Muestra el número sin salto de línea
        print("")  # Salto de línea (pero aquí provoca que imprima cada número en una línea)
        
print(m)  # Muestra la matriz completa en formato lista

# =========================
# EJERCICIO 2
# =========================
print("Ejercicio 2")
A = []  # Matriz A
B = []  # Matriz B
C = []  # Matriz C (suma de A y B)

# Pide al usuario el tamaño de la matriz (n x n)
n = int(input("Digite el tamaño de la matriz: "))

# Construcción de las matrices
for i in range(n):
    A.append([])  # Nueva fila en A
    B.append([])  # Nueva fila en B
    C.append([])  # Nueva fila en C
    for j in range(n):
        A[i].append(random.randint(1, 10))
        B[i].append(random.randint(1, 10))
        C[i].append(A[i][j] + B[i][j])  # Suma elemento por elemento

# Muestra las matrices
print("Matriz A:", A)
print("Matriz B:", B)
print("Matriz C (A+B):", C)

# =========================
# EJERCICIO 3
# =========================
print("Ejercicio 3")
A = []  # Matriz A
B = []  # Matriz B
C = []  # Matriz C (suma de A y B)
D = []  # Matriz D (resta de A y B)

# Pide tamaño de la matriz
n = int(input("Digite el tamaño de la matriz: "))

for i in range(n):
    A.append([])  # Fila en A
    B.append([])  # Fila en B
    C.append([])  # Fila en C
    D.append([])  # Fila en D
    for j in range(n):
        A[i].append(random.randint(1, 10))
        B[i].append(random.randint(1, 10))
        C[i].append(A[i][j] + B[i][j])  # Suma
        D[i].append(A[i][j] - B[i][j])  # Resta

# Muestra las matrices
print("Matriz A:", A)
print("Matriz B:", B)
print("Matriz C (A+B):", C)
print("Matriz D (A-B):", D)
