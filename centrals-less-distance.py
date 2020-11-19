

# monta o grafo 
# recebe o array de vertices e o array de pares de conexoes (arestas)
# retorna um array representado o grafo do problema 
def mountGraph(vertices, edges):
    size = len(vertices)
    graph = [[] for x in range(size)]


    for conn in edges:
        p1 = vertices.index(conn[0])
        p2 = vertices.index(conn[1])

        graph[p1].append(p2)
        graph[p2].append(p1)

    return graph

# realiza a busca em largura no grafo
# recebe o grafo e a posicao inicial da busca
# retorna um array 
def deepSearch(graph, startPosition):

    size = len(graph)

    visitedVertices = [False for x in range(size)]
    distances = [float('inf') for x in range(size)]
    previousVertices = [None for x in range(size)]
    queue = []

    visitedVertices[startPosition] = True
    distances[startPosition] = 0
    queue.append(startPosition)

    while len(queue) > 0:
        c = queue.pop(0)
        for i in graph[c]:
            if(visitedVertices[i] == False):
                visitedVertices[i] = True
                distances[i] = distances[c]+1
                previousVertices[i] = c
                queue.append(i)

    return distances,previousVertices

# monta a rota para sair da origem e chegar no destino
# recebe a origem, o destino, um array de distancias e um array com a posicao da vertice anterior
# devolve um array com o menor percurso para o destino a partir da origem
def mountRoute(source, destination, distances, previousVertices):
    
    route = []
    route.append(destination)
    currentPosition = previousVertices[destination]
    while currentPosition != source and currentPosition != None:
        route.append(currentPosition)
        currentPosition = previousVertices[currentPosition]
    else:
        route.append(currentPosition)

    return route[::-1]
        

def main():
    c1 = 'c1'
    c2 = 'c2'
    c3 = 'c3'
    c4 = 'c4'
    c5 = 'c5'
    c6 = 'c6'

    centrals = [c1, c2, c3, c4, c5, c6]

    connections = [[c1, c2], [c1, c3], [c1, c4], [c2, c3], [c3, c4], [c3, c6], [c4, c5], [c4, c6], [c5, c6] ]

    cs = c1
    ct = c6

    csPosition = centrals.index(cs)
    ctPosition = centrals.index(ct)

    # monta o grafo
    graph = mountGraph(centrals, connections)
    # realiza a busca em largura com base no elemento cs
    distances, previousVertices = deepSearch(centrals, graph, csPosition)
    # monta a rota para chegar em ct a partir de cs
    route = mountRoute(csPosition, ctPosition, distances, previousVertices)

    print(route)

main()
