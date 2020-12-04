import matplotlib.pyplot as plt
import time

# Funcion para leer los datos del archivo de texto
def leer():
    datos = []
    with open("datos.txt", "r") as f:
        for i in f.readlines():
            tmp = i.split(",")
            try:
                datos.append((int(tmp[0]), int(tmp[1])))
            except:pass
        f.close()
    return datos

# Funcion para mostrar la grafica
def show():
    plt.xlim(-0.5, tamaño[0]+0.5)
    plt.ylim(-0.5, tamaño[1]+0.5)
    if(len(x) == 3):   
        labels = ('Mono', 'Silla', 'Platanos')
        sc = plt.scatter(x, y, c=range(3), cmap='cividis')
        cbar = plt.colorbar(sc, ticks=range(3))
    elif (len(x) == 2):
        labels = ('Mono', 'Platanos')
        sc = plt.scatter(x, y, c=range(2), cmap='cividis')
        cbar = plt.colorbar(sc, ticks=range(2))
    else:
        labels = ('Mono')
        sc = plt.scatter(x, y, c=range(1), cmap='cividis')
        cbar = plt.colorbar(sc, ticks=range(1))
    cbar.ax.set_yticklabels(labels)
    frame1 = plt.gca()
    frame1.axes.xaxis.set_ticklabels([])
    frame1.axes.yaxis.set_ticklabels([])
    #plt.savefig('a.png', dpi=100)
    plt.show()
    time.sleep(0.5)
    return sc

# Funcion para calcular el numero de movimientos desde la posicion hasta el destino actual
def calcular(xm, ym, x0, y0, x1, y1):
    try:
        return (abs(xm - x1) + abs(ym - y1)) + (abs(xm - x0) + abs(ym - y0))
    except:
        print()
    return None

def mover(x, y):
    minimo = 999999999999999999999999999
    ruta[x[0]+1][y[0]] = calcular(x[0] + 1, y[0], x[0], y[0], x[1], y[1])
    ruta[x[0]-1][y[0]] = calcular(x[0] - 1, y[0], x[0], y[0], x[1], y[1])
    ruta[x[0]][y[0]+1] = calcular(x[0], y[0] + 1, x[0], y[0], x[1], y[1])
    ruta[x[0]][y[0]-1] = calcular(x[0], y[0] - 1, x[0], y[0], x[1], y[1])
    ruta[x[0]+1][y[0]+1] = calcular(x[0] + 1, y[0]+1, x[0], y[0], x[1], y[1])
    ruta[x[0]-1][y[0]-1] = calcular(x[0] - 1, y[0]-1, x[0], y[0], x[1], y[1])
    ruta[x[0]-1][y[0]+1] = calcular(x[0]-1, y[0] + 1, x[0], y[0], x[1], y[1])
    ruta[x[0]+1][y[0]-1] = calcular(x[0]+1, y[0] - 1, x[0], y[0], x[1], y[1])
    for i in range(tamaño[0]+1):
        for j in range(tamaño[1]+1):
            try:
                if ruta[i][j] < minimo and ruta[i][j] is not None:
                    minimo = ruta[i][j]
                    aux = i
                    aux2 = j
            except:
                continue
    return aux, aux2

start = time.time()
movimientos = 0
datos = leer()
tamaño = datos[0]
ruta = [[None for j in range(tamaño[1] + 1)] for i in range(tamaño[0] + 1)]
del datos[0]
x = [x[0] for x in datos]
y = [x[1] for x in datos]
sc = show()

try:
    while(x[0] != x[1] or y[0] != y[1]):
        x[0], y[0] = mover(x, y)
        sc.remove()
        sc = show()
        if(x[0] == x[1] and y[0] == y[1]):
            x.pop(1)
            y.pop(1)
            ruta = [[None for j in range(tamaño[1] + 1)] for i in range(tamaño[0] + 1)]
        movimientos +=1
except:
    sc.remove()
    sc = show()
    end = time.time()
    print("Numero de movimientos - ", movimientos)
    print("Tiempo total - ", end - start)
