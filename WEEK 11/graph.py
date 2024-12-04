from edge import Edge
from heapq import heappush, heappop

class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, node1, node2, distance):
        forwardEdge = Edge(node1, node2, distance)
        reverseEdge = Edge(node2, node1, distance)

        node1.addEdge(forwardEdge)
        node2.addEdge(reverseEdge)

    def dijkstra(self, origin, destination):
        openlist = []
        origin.dist = 0
        heappush(openlist, origin)
        while(len(openlist) > 0):
            currentNode = heappop(openlist)

