import networkx as nx

x = 5
y =10
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(1, name='3.2.1',coordi=[x,y], signi = 0)
G.add_node(3, name='3.2.1',coordi=[x,y], signi = 0)
#G.add_node(1, coordi=[x,y])

print G.nodes()
print G.node[3]
print G.node[1]['coordi']
print G.number_of_nodes()
