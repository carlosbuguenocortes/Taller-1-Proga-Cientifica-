from loaders.cargador_wikipedia import CargadorWikipedia
from utilidades.reporte_basico import ReporteBasicoWikipedia


def main():
    cargador = CargadorWikipedia()
    grafo = cargador.cargar_grafo()
    reporte = ReporteBasicoWikipedia()
    archivos_reporte = reporte.generar(grafo)
    reporte.imprimir_en_consola(grafo)

    print()
    print("Archivos generados:")
    print(archivos_reporte["texto"])

    print()
    
    # elegir nodos con conexiones reales
    origen = grafo.top_por_grado_entrada(1)[0].id_articulo
    destino = grafo.top_por_grado_salida(1)[0].id_articulo

    print("\nNodo origen:", origen)
    print("Nodo destino:", destino)

    # BFS con camino
    print("\n--- BFS ---")
    recorrido_bfs = grafo.bfs(origen)
    print("Primeros 10 nodos BFS:", recorrido_bfs[:10])

    # DFS con camino
    print("\n--- DFS ---")
    camino_dfs = grafo.dfs(origen, destino)

    if camino_dfs:
        print("Camino DFS:", camino_dfs[:10])
    else:
        print("No hay camino DFS")
    # CAMINO usando tu BFS modificado
    print("\n--- CAMINO ENTRE NODOS ---")
    camino = grafo.bfs(origen, destino)

    if camino:
        print("Camino encontrado:", camino[:10])
    else:
        print("No hay camino")

    print("\n--- PAGERANK ---")
    ranking = grafo.pagerank(iteraciones=10)

    top = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

    for i, (id_articulo, valor) in enumerate(top[:10]):
        articulo = grafo.obtener_articulo(id_articulo)
        print(f"{i+1}. {articulo.nombre} -> {valor}")
    
    with open("pagerank.txt", "w", encoding="utf-8") as f:
        for id_articulo, valor in top[:50]:
            articulo = grafo.obtener_articulo(id_articulo)
            f.write(f"{articulo.nombre} -> {valor}\n")

    print()
    print("Archivos generados:")
    print(archivos_reporte["texto"])
    print("pagerank.txt")

if __name__ == "__main__":
    main()



