from graph import GraphAdjList, GraphAdjMatrix


# graph number : (nodes count,start node), list of graph nodes and edges
graphSamples = {
   "Graph1": [(6, 1), [(1, 2, 2),(1, 4, 1),(1, 5, 4),(2, 3, 3),(2, 4, 3),(2, 6, 7),(3, 4, 5),(3, 6, 8),(4, 5, 9)]],
   "Graph2": [(9, 0), [(0, 1, 4),(0, 7, 8),(1, 2, 8),(1, 7, 11),(2, 3, 7),(2, 5, 4),(2, 8, 2),(3, 4, 9),(3, 5, 14),
                (4, 5, 10),(5, 6, 2),(6, 7, 1),(6, 8, 6),(7, 8, 7)]],
   "Graph3": [(7, 1), [(1, 2, 28),(1, 6, 10),(2, 3, 16),(2, 7, 14),(3, 4, 12),(4, 5, 22),(4, 7, 18),(5, 6, 25),
                (5, 7, 24)]]
}


if __name__ == "__main__":
    for item in graphSamples.items():
        print(item[0])
        print("Adjacency List")
        g = GraphAdjList(item[1][0][0], item[1][0][1])
        for e in item[1][1]:
            g.add_edge(e[0], e[1], e[2])
        g.kruskals_mst()
        print("Adjacency Matrix")
        g = GraphAdjMatrix(item[1][0][0], item[1][0][1])
        for e in item[1][1]:
            g.add_edge(e[0], e[1], e[2])
        g.kruskals_mst()