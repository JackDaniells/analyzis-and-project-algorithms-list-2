import heapq

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = float('inf')
        self.visited = False  
        self.previous = None

    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight


class Graph:
    def __init__(self):
        self.vert_dict = {}

    def __iter__(self):
        return iter(self.vert_dict.values())

    def addVertex(self, node):
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def getVertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def addEdge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.addVertex(frm)
        if to not in self.vert_dict:
            self.addVertex(to)

        self.vert_dict[frm].addNeighbor(self.vert_dict[to], cost)
        self.vert_dict[to].addNeighbor(self.vert_dict[frm], cost)


def getShortestRoute(v, path):
    if v.previous:
        path.append(v.previous.id)
        getShortestRoute(v.previous, path)
    return path[::-1]


def dijkstra(aGraph, start, target):

    start.distance = 0

    unvisited_queue = [(v.distance,v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):

        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.visited = True

        for next in current.adjacent:

            if next.visited:
                continue
            new_dist = current.distance + current.adjacent[next]
            
            if new_dist < next.distance:
                next.distance = new_dist
                next.previous = current

        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)

        unvisited_queue = [(v.distance,v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
    
def main():

    g = Graph()

    g.addVertex('a')
    g.addVertex('b')
    g.addVertex('c')
    g.addVertex('d')
    g.addVertex('e')
    g.addVertex('f')

    g.addEdge('a', 'b', 7)  
    g.addEdge('a', 'c', 9)
    g.addEdge('a', 'f', 14)
    g.addEdge('b', 'c', 10)
    g.addEdge('b', 'd', 15)
    g.addEdge('c', 'd', 11)
    g.addEdge('c', 'f', 2)
    g.addEdge('d', 'e', 6)
    g.addEdge('e', 'f', 9)

    source = g.getVertex('a')
    target = g.getVertex('e')

    dijkstra(g, source, target) 

    path = getShortestRoute(target, [target.id])
    print 'The shortest path : %s' %(path)

main()