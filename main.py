import networkx as nx 
import matplotlib.pyplot as plt
from bfs_iter import bfs_iterative
from dfs_rec import dfs_recursive
from dijkstra import dijkstra

    
graph = {
'A': {'B': 5, 'C': 10},
'B': {'A': 5, 'D': 3},
'C': {'A': 10, 'D': 2},
'D': {'B': 3, 'C': 2, 'E': 4},
'E': {'D': 4}
}

G = nx.Graph(graph)

G.add_nodes_from(["A", "B", "C", "D", "E"])
G.add_edge("A", "B", weight=5)
G.add_edge("A", "C", weight=10)
G.add_edge("B", "D", weight=3)
G.add_edge("C", "D", weight=2)
G.add_edge("D", "E", weight=4)

# Загальна кількість вузлів графа
num_nodes = G.number_of_nodes()
print("Загальна кількість вузлів графа:", num_nodes)

# Загальна кількість ребер графа
num_edges = G.number_of_edges()
print("Загальна кількість ребер графа:", num_edges)

# Ступінь кожного вузла графа
node_degrees = dict(G.degree())
print("Ступінь кожного вузла графа:", node_degrees)

#Найкоротший шлях
print(dijkstra(graph, 'A'))


bfs_iterative(G, 'A')
print("")
dfs_recursive(G, 'A')

plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=16, font_weight="bold")
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
