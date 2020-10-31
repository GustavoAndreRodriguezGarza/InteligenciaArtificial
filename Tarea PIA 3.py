import random
from itertools import product

# Funcion que determina si el valor aleatorio que se quiere dar ya ha sido asignado
def asignar(valor, aux):
    if valor not in aux:
        return valor
    else:
        return None

# Funcion que realiza el algoritmo Hill Climbing
def HillClimbing(puzzle, solucion):
    puzzle1 = [[None for i in range(3)] for j in range(3)]
    puzzle2 = [[None for i in range(3)] for j in range(3)]
    puzzle3 = [[None for i in range(3)] for j in range(3)]
    puzzle4 = [[None for i in range(3)] for j in range(3)]
    for x, y in product(range(3), repeat = 2):
        puzzle1[x][y] = puzzle[x][y]
        puzzle2[x][y] = puzzle[x][y]
        puzzle3[x][y] = puzzle[x][y]
        puzzle4[x][y] = puzzle[x][y]
    lista = [puzzle1, puzzle2, puzzle3, puzzle4]
    estados = [0, 0, 0, 0]
    # Se encuentra la posicion de la casilla vacia
    for i, j in product(range(3), repeat = 2):
        if puzzle[i][j] == 0:
            break
    # Se generan los diferentes resultados posibles al mover las piezas
    if i > 0:
        puzzle1[i-1][j], puzzle1[i][j] = puzzle1[i][j], puzzle1[i-1][j]
        lista[0] = puzzle1.copy()
    if i < 2:
        puzzle2[i+1][j], puzzle2[i][j] = puzzle2[i][j], puzzle2[i+1][j]
        lista[1] = puzzle2.copy()
    if j > 0:
        puzzle3[i][j-1], puzzle3[i][j] = puzzle3[i][j], puzzle3[i][j-1]
        lista[2] = puzzle3.copy()
    if j < 2:
        puzzle4[i][j+1], puzzle4[i][j] = puzzle4[i][j], puzzle4[i][j+1]
        lista[3] = puzzle4.copy()
    # Se calcula cual de los resultados da una mejor solucion hasta ahora
    for x, y in product(range(3), repeat = 2):
        if puzzle1[x][y] == solucion[x][y]:
            estados[0] +=1
        if puzzle2[x][y] == solucion[x][y]:
            estados[1] +=1
        if puzzle3[x][y] == solucion[x][y]:
            estados[2] +=1
        if puzzle4[x][y] == solucion[x][y]:
            estados[3] +=1
    j = 0
    M = []
    maximo = max(estados)
    # Funcion utilizada para aleatorizar la solcuon que se enviara en caso de que haya empate
    for i in estados:
        if i == maximo:
            M.append(j)
        j +=1
    w = estados[random.choice(M)]
    return lista[w], maximo

aux = []
estado = 0
puzzle = [[None for i in range(3)] for j in range(3)]
solucion = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# Se asignan los valores al puzzle
for x, y in product(range(3), repeat = 2):
    while puzzle[x][y] is None:
        puzzle[x][y] = asignar(random.randint(0, 8), aux)
    if puzzle[x][y] == solucion[x][y]:
        estado+=1
    aux.append(puzzle[x][y])
# Ciclo donde se iterara el algoritmo gasta encontrar la solucion optima
while estado != 9:
    puzzle, estado = HillClimbing(puzzle, solucion)
print("Solucion: ", puzzle)
