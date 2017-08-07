#!/usr/bin/python2

import networkx as nx
import matplotlib.pyplot as plt

"""

class c_waypoint(object):
    def __init__(self,name,data):
        self.name = name
        self.coordi = data
    def set_parent(self,lane):
        self.parent = lane

class c_lane(object):
    def __init__(self,name):
        self.name = name
        self.waypoints = []
    def add_waypoints(self,waypoint):
        self.waypoints.append(waypoint)
    def set_parent(self,segment):
        self.parent = segment

class c_segment(object):
    def __init__(self,name):
        self.name = name
        self.lanes = []
    def add_lanes(self,lane):
        self.lanes.append(lane)
    def set_parent(self,rndf):
        self.parent = rndf

class c_rndf(object):
    def __init__(self,name):
        self.name = name
        self.segments= []
    def add_segment(self,segment):
        self.segments.append(segment)


p1 = c_waypoint("adc", [1,2])
p2 = c_waypoint("p2", [2,4])
l1 = c_lane("l1")
s1 = c_segment("s1")

l1.add_waypoints(p1)
l1.add_waypoints(p2)

s1.add_lanes(l1)

p1.set_parent(l1)
p2.set_parent(l1)

l1.set_parent(s1)

#print p1.coordi,p2.coordi
#print l1.waypoints[0].coordi, l1.waypoints[1].coordi
#print s1.lanes[0].waypoints[0].coordi, s1.lanes[0].waypoints[1].coordi
#print p1.parent.name
#print l1.parent.name
#print (p1.parent).parent.name

"""

"""
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
"""

G = nx.DiGraph()
G.add_node(1)
G.add_node(2)
G.add_edge(1,2)
print G.nodes()

graph_pos = nx.shell_layout(G)
nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='blue', alpha=0.3)
nx.draw_networkx_edges(G, graph_pos)
nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')
plt.show()
