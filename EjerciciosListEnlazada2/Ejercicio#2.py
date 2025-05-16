'''Se requiere automatizar un mapa que contiene las estaciones de una ruta previamente 
establecida para una aplicación que indique, a partir de un punto de la ruta, el tiempo estimado 
para llegar a un destino determinado de la misma. '''

class Nodo:
    def __init__(self, nombre, tiempo_hasta_siguiente):
        self.nombre = nombre
        self.tiempo_hasta_siguiente = tiempo_hasta_siguiente
        self.siguiente = None
        self.anterior = None  

class Ruta:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, nombre, tiempo_hasta_siguiente):
        nuevo_nodo = Nodo(nombre, tiempo_hasta_siguiente)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual 

    def calcular_tiempo(self, inicio, destino):
        tiempo_total = self._calcular_tiempo_direccion(inicio, destino)
        if tiempo_total is not None:
            return tiempo_total
        
        tiempo_total = self._calcular_tiempo_direccion(destino, inicio)
        if tiempo_total is not None:
            return tiempo_total
        
        return None  

    def _calcular_tiempo_direccion(self, inicio, destino):
        actual = self.cabeza
        tiempo_total = 0
        encontrado_inicio = False

        while actual:
            if actual.nombre == inicio:
                encontrado_inicio = True
            if encontrado_inicio:
                tiempo_total += actual.tiempo_hasta_siguiente
                if actual.nombre == destino:
                    return tiempo_total
            actual = actual.siguiente

        return None  

def main():
    ruta = Ruta()
    ruta.agregar_nodo("Estacion A", 5)  # 5 minutos hasta la siguiente
    ruta.agregar_nodo("Estacion B", 10)  # 10 minutos hasta la siguiente
    ruta.agregar_nodo("Estacion C", 3)   # 3 minutos hasta la siguiente
    ruta.agregar_nodo("Estacion D", 7)   # 7 minutos hasta la siguiente

    print("Bienvenido al sistema de estimación de tiempo de ruta.")
    inicio = input("Ingrese la estación de inicio: ")
    destino = input("Ingrese la estación de destino: ")

    tiempo_estimado = ruta.calcular_tiempo(inicio, destino)

    if tiempo_estimado is not None:
        print(f"El tiempo estimado para llegar de {inicio} a {destino} es de {tiempo_estimado} minutos.")
    else:
        print("No se pudo encontrar la ruta entre las estaciones especificadas.")

if __name__ == "__main__":
    main()