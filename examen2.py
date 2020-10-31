import random

# Clase para representaer un grafo
class Grafo:
    # Se inicializa la clase
    def __init__(self, grafo_dict=None, directed=True):
        self.grafo_dict = grafo_dict or {}
        self.directed = directed
        if not directed:
            self.noDireccionado()
    # Se crea grafo sin direccion agregando aristas simetricas
    def crearGrafo(self):
        for a in list(self.grafo_dict.keys()):
            for (b, dist) in self.grafo_dict[a].items():
                self.grafo_dict.setdefault(b, {})[a] = dist
    # Hace enlace entre A y B con la distancia dada, tambien agrega el enlace inverso si el grafo es sin direccion
    def conectar(self, A, B, distancia=1):
        self.grafo_dict.setdefault(A, {})[B] = distancia
        if not self.directed:
            self.grafo_dict.setdefault(B, {})[A] = distancia
    # Obtiene los vecinos
    def get(self, a, b=None):
        links = self.grafo_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

def DFS(grafo, indice, colores, cerrados, resultados):
    opciones = []
    for i in resultados:
        nombre, color = i
        if nombre in grafo.get(indice):
            opciones.append(color)
    opciones = [x for x in colores if x not in opciones]
    resultados.append(tuple([indice, min(opciones)]))
    cerrados.append(indice)
    for i in grafo.get(indice):
        if(i not in [x[0] for x in resultados]):
            DFS(grafo, i, colores, cerrados, resultados)
    return resultados

def main():
    # Crea un grafo
    grafo = Grafo()
    # Crea las conecciones del grafo
    grafo.conectar('Nuevo Leon', 'Tamaulipas', random.randint(0, 100))
    grafo.conectar('Nuevo Leon', 'Coahuila', random.randint(0, 100))
    grafo.conectar('Nuevo Leon', 'San Luis Potosi', random.randint(0, 100))
    grafo.conectar('Chihuahua', 'Coahuila', random.randint(0, 100))
    grafo.conectar('Durango', 'Coahuila', random.randint(0, 100))
    grafo.conectar('Zacatecas', 'Coahuila', random.randint(0, 100))
    grafo.conectar('San Luis Potosi', 'Coahuila', random.randint(0, 100))
    grafo.conectar('Chihuahua', 'Sonora', random.randint(0, 100))
    grafo.conectar('Chihuahua', 'Sinaloa', random.randint(0, 100))
    grafo.conectar('Chihuahua', 'Durango', random.randint(0, 100))
    grafo.conectar('Baja California', 'Sonora', random.randint(0, 100))
    grafo.conectar('Sinaloa', 'Sonora', random.randint(0, 100))
    grafo.conectar('Baja California Sur', 'Sonora', random.randint(0, 100))
    grafo.conectar('Baja California', 'Baja California Sur', random.randint(0, 100))
    grafo.conectar('San Luis Potosi', 'Tamaulipas', random.randint(0, 100))
    grafo.conectar('Veracruz', 'Tamaulipas', random.randint(0, 100))
    grafo.conectar('Nayarit', 'Sinaloa', random.randint(0, 100))
    grafo.conectar('Durango', 'Sinaloa', random.randint(0, 100))
    grafo.conectar('Durango', 'Zacatecas', random.randint(0, 100))
    grafo.conectar('Durango', 'Nayarit', random.randint(0, 100))
    grafo.conectar('San Luis Potosi', 'Zacatecas', random.randint(0, 100))
    grafo.conectar('Nayarit', 'Zacatecas', random.randint(0, 100))
    grafo.conectar('Jalisco', 'Zacatecas', random.randint(0, 100))
    grafo.conectar('Aguascalientes', 'Zacatecas', random.randint(0, 100))
    grafo.conectar('San Luis Potosi', 'Guanajuato', random.randint(0, 100))
    grafo.conectar('San Luis Potosi', 'Queretaro', random.randint(0, 100))
    grafo.conectar('San Luis Potosi', 'Hidalgo', random.randint(0, 100))
    grafo.conectar('San Luis Potosi', 'Veracruz', random.randint(0, 100))
    grafo.conectar('Nayarit', 'Jalisco', random.randint(0, 100))
    grafo.conectar('Aguascalientes', 'Jalisco', random.randint(0, 100))
    grafo.conectar('Colima', 'Jalisco', random.randint(0, 100))
    grafo.conectar('Michoacan', 'Jalisco', random.randint(0, 100))
    grafo.conectar('Guanajuato', 'Jalisco', random.randint(0, 100))
    grafo.conectar('Guanajuato', 'Queretaro', random.randint(0, 100))
    grafo.conectar('Guanajuato', 'Michoacan', random.randint(0, 100))
    grafo.conectar('Guanajuato', 'Michoacan', random.randint(0, 100))
    grafo.conectar('Queretaro', 'Hidalgo', random.randint(0, 100))
    grafo.conectar('Queretaro', 'Michoacan', random.randint(0, 100))
    grafo.conectar('Queretaro', 'Estado de Mexico', random.randint(0, 100))
    grafo.conectar('Veracruz', 'Hidalgo', random.randint(0, 100))
    grafo.conectar('Puebla', 'Hidalgo', random.randint(0, 100))
    grafo.conectar('Tlaxcala', 'Hidalgo', random.randint(0, 100))
    grafo.conectar('Estado de Mexico', 'Hidalgo', random.randint(0, 100))
    grafo.conectar('Veracruz', 'Puebla', random.randint(0, 100))
    grafo.conectar('Veracruz', 'Oaxaca', random.randint(0, 100))
    grafo.conectar('Veracruz', 'Chiapas', random.randint(0, 100))
    grafo.conectar('Veracruz', 'Tabasco', random.randint(0, 100))
    grafo.conectar('Colima', 'Michoacan', random.randint(0, 100))
    grafo.conectar('Estado de Mexico', 'Michoacan', random.randint(0, 100))
    grafo.conectar('Guerrero', 'Michoacan', random.randint(0, 100))
    grafo.conectar('Estado de Mexico', 'Distrito Federal', random.randint(0, 100))
    grafo.conectar('Estado de Mexico', 'Guerrero', random.randint(0, 100))
    grafo.conectar('Estado de Mexico', 'Morelos', random.randint(0, 100))
    grafo.conectar('Estado de Mexico', 'Tlaxcala', random.randint(0, 100))
    grafo.conectar('Estado de Mexico', 'Puebla', random.randint(0, 100))
    grafo.conectar('Puebla', 'Distrito Federal', random.randint(0, 100))
    grafo.conectar('Puebla', 'Tlaxcala', random.randint(0, 100))
    grafo.conectar('Puebla', 'Guerrero', random.randint(0, 100))
    grafo.conectar('Puebla', 'Oaxaca', random.randint(0, 100))
    grafo.conectar('Oaxaca', 'Guerrero', random.randint(0, 100))
    grafo.conectar('Oaxaca', 'Chiapas', random.randint(0, 100))
    grafo.conectar('Tabasco', 'Chiapas', random.randint(0, 100))
    grafo.conectar('Tabasco', 'Campeche', random.randint(0, 100))
    grafo.conectar('Campeche', 'Quintana Roo', random.randint(0, 100))
    grafo.conectar('Campeche', 'Yucatan', random.randint(0, 100))
    grafo.conectar('Yucatan', 'Quintana Roo', random.randint(0, 100))
    # Crea grafo indireccionado, crea conexiones simetricas
    grafo.crearGrafo()
    colores = ['Azul', 'Verde', 'Naranja', 'Amarillo', 'Cafe']
    cerrados = []
    abiertos = []
    resultados = []
    # Corre algoritmo de busqueda
    resultados = DFS(grafo, 'Nuevo Leon', colores, cerrados, resultados)
    for i in resultados:
        print(i)
# Corre el main
main()
