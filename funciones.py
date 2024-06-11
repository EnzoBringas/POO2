import networkx as nx

def crearRed(relaciones):
    G = nx.Graph()
    for persona, amigo, grado in relaciones:
        G.add_edge(persona, amigo, weight=grado)
    return G

def distancia_minima_de_amistad(grafo, persona1, persona2):
    try:
        distancia = nx.shortest_path_length(grafo, source=persona1, target=persona2, weight='weight')
        if distancia == 0:
            return 0  
        elif distancia == 1:
            return "Amigo Personales"
        elif distancia == 2:
            return "conocidos"
        else:
            return "Compañeros"
    except nx.NetworkXNoPath:
        return "Desconocidos"