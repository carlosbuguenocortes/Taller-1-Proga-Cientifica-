from pathlib import Path

from modelos.grafo import GrafoWikipedia


class CargadorWikipedia:
    """Carga desde el dataset los datos necesarios para construir el grafo."""

    def __init__(self, ruta_dataset=None):
        if ruta_dataset is None:
            self.ruta_dataset = Path(__file__).resolve().parent.parent.parent / "dataset"
        else:
            self.ruta_dataset = Path(ruta_dataset)

    def cargar_nombres_articulos(self):
        ruta = self.ruta_dataset / "wiki-topcats_pagenames.txt"
        nombres = {}

        with open(ruta, "r", encoding="utf-8") as archivo:
            for indice, linea in enumerate(archivo, start=1):
                nombres[indice] = linea.strip()

        return nombres

    def cargar_nombres_categorias(self):
        ruta = self.ruta_dataset / "wiki-topcats_Category_names.txt"
        categorias = {}

        with open(ruta, "r", encoding="utf-8") as archivo:
            for indice, linea in enumerate(archivo, start=1):
                categorias[indice] = linea.strip()

        return categorias

    def _leer_matriz_market(self, ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()

                if not linea or linea.startswith("%"):
                    continue

                partes = linea.split()

                if len(partes) == 3:
                    continue

                if len(partes) >= 2:
                    fila = int(partes[0])
                    columna = int(partes[1])
                    yield fila, columna

    def cargar_grafo(self):
        grafo = GrafoWikipedia()
        nombres = self.cargar_nombres_articulos()

        # limitar nodos
        limite_nodos = 5000
        nodos_validos = set()

        for id_articulo, nombre in list(nombres.items())[:limite_nodos]:
            grafo.agregar_articulo(id_articulo, nombre)
            nodos_validos.add(id_articulo)

        # cargar enlaces
        ruta_links = self.ruta_dataset / "wiki-topcats.mtx"

        for i, (origen, destino) in enumerate(self._leer_matriz_market(ruta_links)):
            if i > 5000:
                break

            # conectar nodos que existen
            if origen in nodos_validos and destino in nodos_validos:
                grafo.agregar_enlace(origen, destino)

        return grafo
