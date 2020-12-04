import matplotlib.pyplot as plt
import time
from timeit import default_timer as timer

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

def DFS(x, y, visitados, cerrados):
    for w in range(7):
        xn, yn = nuevaPosicion(w, x, y)
        if (xn, yn) not in visitados and (xn, yn) not in cerrados and xn >= 0 and xn <= tamaño[0] and yn >= 0 and yn <= tamaño[1]:
            visitados.append((xn, yn))
            return xn, yn
    cerrados.append((x[0], y[0]))
    return visitados.pop(-1)

# Diccionario que regresa la nueva posicion del mono
def nuevaPosicion(posicion, x, y):
    return{
        0: (x[0]+1, y[0]),
        1: (x[0]-1, y[0]),
        2: (x[0], y[0]+1),
        3: (x[0], y[0]-1),
        4: (x[0]+1, y[0]+1),
        5: (x[0]-1, y[0]-1),
        6: (x[0]-1, y[0]+1),
        7: (x[0]+1, y[0]-1)
        }[posicion]

visitados = []
cerrados = []
movimientos = 0
start = timer()
datos = leer()
tamaño = datos[0]
del datos[0]
x = [x[0] for x in datos]
y = [x[1] for x in datos]
sc = show()
visitados.append((x[0], y[0]))

try:
    while(x[0] != x[1] or y[0] != y[1]):
        x[0], y[0] = DFS(x, y, visitados, cerrados)
        sc.remove()
        sc = show()
        if(x[0] == x[1] and y[0] == y[1]):
            x.pop(1)
            y.pop(1)
            visitados.clear()
            visitados.append((x[0], y[0]))
        movimientos += 1
except:
    sc.remove()
    sc = show()
    end = timer()
    print("Numero de movimientos - ", movimientos)
    print("Tiempo total - ", end - start)