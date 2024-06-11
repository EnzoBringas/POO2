import networkx as nx
import matplotlib.pyplot as plt
from funciones import crearRed, distancia_minima_de_amistad


relaciones_ejemplo = [
    ("Juan", "Pedro", 3),
    ("Pedro", "Maria", 2),
    ("Maria", "Carlos", 1),
    ("Juan", "Carlos", 3),
    ("Ana", "Maria", 2),
    ("Ana", "Carlos", 1),
    ("Enzo", "Jose", 1)
]


grafo = crearRed(relaciones_ejemplo)

nx.draw(grafo, with_labels=True)
plt.show()

print("Juan y Maria son:", distancia_minima_de_amistad(grafo, "Juan", "Maria"))
print("Juan y Enzo son:", distancia_minima_de_amistad(grafo, "Juan", "Enzo"))


