from collections import deque

from modelos.articulo import ArticuloWikipedia


class GrafoWikipedia:
    """Representa un grafo dirigido de articulos de Wikipedia y sus enlaces."""

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, id_articulo, nombre):
        if id_articulo not in self.articulos:
          self.articulos[id_articulo] = ArticuloWikipedia(id_articulo, nombre)

    def obtener_articulo(self, id_articulo):
        return self.articulos.get(id_articulo)

    def agregar_enlace(self, id_origen, id_destino):
        if id_origen not in self.articulos or id_destino not in self.articulos:
          return

        self.articulos[id_origen].agregar_enlace_salida(id_destino)
        self.articulos[id_destino].agregar_enlace_entrada(id_origen)

    def cantidad_articulos(self):
        return len(self.articulos)        

    def cantidad_enlaces(self):
        total = 0
        for articulo in self.articulos.values():
          total += articulo.grado_salida()
        return total

    def top_por_grado_entrada(self, cantidad=10):
        lista = list(self.articulos.values())
        lista.sort(key=lambda x: x.grado_entrada(), reverse=True)
        return lista[:cantidad]

    def top_por_grado_salida(self, cantidad=10):
        lista = list(self.articulos.values())
        lista.sort(key=lambda x: x.grado_salida(), reverse=True)
        return lista[:cantidad]

    def resumen(self):
        return {
            "articulos": self.cantidad_articulos(),
            "enlaces": self.cantidad_enlaces(),
        }

    def bfs(self, id_inicio, destino=None):
        if id_inicio not in self.articulos:
            return []

        visitados = set([id_inicio])
        cola = deque([id_inicio])
        padres = {id_inicio: None}
        recorrido = []
        while cola:
            actual = cola.popleft()
            recorrido.append(actual)
            # si llegamos al destino, paramos
            if actual == destino:
                break

            for vecino in self.articulos[actual].enlaces_salida:
                if vecino not in visitados:
                    visitados.add(vecino)
                    padres[vecino] = actual
                    cola.append(vecino)

        # si se pidió un destino → devolver camino
        if destino is not None:
            if destino not in padres:
                return []

            camino = []
            actual = destino

            while actual is not None:
                camino.append(actual)
                actual = padres[actual]

            camino.reverse()
            return camino

        # si no se pide destino -> devolver recorrido completo
        return recorrido

    def dfs(self, id_inicio, destino=None):
        if id_inicio not in self.articulos:
            return []

        visitados = set()
        pila = [(id_inicio, [id_inicio])]

        while pila:
            actual, camino = pila.pop()

            if actual == destino:
                return camino

            if actual not in visitados:
                visitados.add(actual)

                for vecino in self.articulos[actual].enlaces_salida:
                    if vecino not in visitados:
                        pila.append((vecino, camino + [vecino]))

        return []

    def encontrar_camino_simple(self, id_origen, id_destino):
        """
        TODO:
        Mejorar esta búsqueda para encontrar caminos más interesantes.
        Por ahora retorna un camino simple usando BFS.
        """
        if id_origen not in self.articulos or id_destino not in self.articulos:
            return []

        cola = deque([id_origen])
        padres = {id_origen: None}

        while cola:
            actual = cola.popleft()

            if actual == id_destino:
                break

            for vecino in self.articulos[actual].enlaces_salida:
                if vecino not in padres:
                    padres[vecino] = actual
                    cola.append(vecino)

        if id_destino not in padres:
            return []

        camino = []
        actual = id_destino

        while actual is not None:
            camino.append(actual)
            actual = padres[actual]

        camino.reverse()
        return camino

    def pagerank(self, iteraciones=20, damping=0.85):
        """
        TODO:
        Este método puede servir como base para la versión final.
        Puede validarlo, modificarlo o reimplementarlo.
        """
        cantidad_nodos = self.cantidad_articulos()
        if cantidad_nodos == 0:
            return {}

        puntajes = {}
        valor_inicial = 1.0 / cantidad_nodos

        for id_articulo in self.articulos:
            puntajes[id_articulo] = valor_inicial

        for _ in range(iteraciones):
            nuevos_puntajes = {}

            for id_articulo in self.articulos:
                nuevos_puntajes[id_articulo] = (1.0 - damping) / cantidad_nodos

            for id_articulo, articulo in self.articulos.items():
                if articulo.grado_salida() == 0:
                    continue

                aporte = puntajes[id_articulo] / articulo.grado_salida()

                for vecino in articulo.enlaces_salida:
                    nuevos_puntajes[vecino] += damping * aporte

            puntajes = nuevos_puntajes

        return puntajes
