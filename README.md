# Taller 1 - Análisis de Grafos de Wikipedia

## Descripción

Este proyecto implementa un sistema en Python orientado a objetos para modelar y analizar una red de artículos de Wikipedia utilizando grafos dirigidos.

Cada nodo del grafo representa un artículo y cada arista representa un enlace entre artículos.

El sistema permite:

- Construir un grafo dirigido a partir de un dataset real de Wikipedia.
- Calcular métricas estructurales.
- Realizar recorridos BFS y DFS.
- Encontrar caminos entre nodos.
- Implementar una versión simplificada de PageRank.
- Generar reportes automáticos.

---

# Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos (POO)
- Estructuras de datos:
  - Diccionarios
  - Sets
  - Colas (`deque`)
- Algoritmos de grafos:
  - BFS
  - DFS
  - PageRank

---

# Estructura del proyecto

```text
template/
│
├── dataset/
│   ├── wiki-topcats.mtx
│   ├── wiki-topcats_Categories.mtx
│   ├── wiki-topcats_pagenames.txt
│   └── wiki-topcats_Category_names.txt
│
├── results/
│   ├── reporte_basico.txt
│   └── pagerank.txt
│
├── src/
│   ├── loaders/
│   │   └── cargador_wikipedia.py
│   │
│   ├── modelos/
│   │   ├── articulo.py
│   │   └── grafo.py
│   │
│   ├── utilidades/
│   │   └── reporte_basico.py
│   │
│   └── main.py
│
└── README.md
```

---

# Funcionalidades implementadas

## Construcción del grafo

Se cargan artículos y enlaces desde el dataset de Wikipedia.

El sistema genera un subconjunto de 5000 artículos para reducir costos computacionales y facilitar el análisis.

---

## Métricas estructurales

Se calcularon:

- Cantidad de artículos
- Cantidad de enlaces
- Grado de entrada
- Grado de salida

Además se identificaron los nodos más conectados de la red.

---

## BFS y DFS

Se implementaron recorridos:

- BFS (Breadth First Search)
- DFS (Depth First Search)

Estos algoritmos permiten explorar la conectividad de la red y encontrar caminos entre artículos.

---

## PageRank

Se implementó una versión simplificada del algoritmo PageRank utilizando:

- factor de amortiguación (`damping`)
- iteraciones sucesivas

Esto permite identificar artículos más relevantes dentro de la red.

---

# Ejecución del proyecto

## Requisitos

- Python 3 instalado

Verificar instalación:

```bash
python --version
```

---

## Ejecutar

Desde la carpeta principal:

```bash
python src/main.py
```

o en algunos sistemas:

```bash
python3 src/main.py
```

---

# Resultados obtenidos

El sistema logró construir exitosamente un grafo dirigido con:

- 5000 artículos
- 2419 enlaces

Se observó que algunos artículos poseen una cantidad extremadamente alta de conexiones, especialmente relacionados con taxonomías biológicas como:

- Buprestidae
- Buprestoidea

Esto demuestra una distribución desigual de enlaces, típica de redes reales y consistente con estructuras tipo "scale-free".

El algoritmo PageRank permitió identificar nodos centrales y relevantes dentro de la red.

---

# Conclusiones

El proyecto permitió aplicar conceptos fundamentales de:

- Programación Orientada a Objetos
- Modelamiento de grafos
- Algoritmos de búsqueda
- Análisis estructural de redes

Los resultados muestran que la red de Wikipedia posee nodos altamente conectados que actúan como centros de información.

Además, se comprobó que algoritmos como BFS, DFS y PageRank son herramientas efectivas para analizar redes complejas.

---

# Integrantes

- Carlos Bugueño
- Constantino Bekios
- Vicente Moyano
