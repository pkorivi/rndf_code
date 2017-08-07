#!/usr/bin/python2

import networkx as nx
import matplotlib.pyplot as plt

#Different weights for straight edge and turning edge.
#This can be modified for path such that to optimize distance or time
straight_weight = 1
turn_weight = 1 # This makes the car to choose longer path over turns
left_turn_weight = 5
right_turn_weight = 2

########
# RNDF Strucurure
#######

class c_waypoint(object):
    def __init__(self,name,coordi,parent, idn):
        self.name = name
        self.coordi = coordi
        self.parent = parent
        self.idn = idn
        #If unique id for every waypoint is needed ?
        #self.uid = id(self)
    def __str__(self):
        return '{}'.format(self.name)

class c_exit(object):
    def __init__(self, entry, exit, parent):
        self.entry = entry
        self.exit = exit
        self.parent = parent


class c_lane(object):
    def __init__(self,name,parent,idn):
        self.name = name
        self.parent = parent
        self.idn = idn
        self.waypoints = []
        self.exits = []
    def add_waypoint(self,waypoint):
        self.waypoints.append(waypoint)
    def add_exit(self,exit):
        self.exits.append(exit)
    def __str__(self):
        return '{}'.format(self.name)

class c_segment(object):
    def __init__(self,name,parent,idn):
        self.name = name
        self.lanes = []
        self.parent = parent
        self.idn = idn
    def add_lane(self,lane):
        self.lanes.append(lane)
    def __str__(self):
        return '{}'.format(self.name)

class c_rndf(object):
    def __init__(self,name):
        self.name = name
        self.segments= []
    def add_segment(self,segment):
        self.segments.append(segment)
    def __str__(self):
        return '{}'.format(self.name)

#########
# Creating Graph
########

G = nx.DiGraph()
connections = []
stops = [] # later remove from list and update here again
connect_previous = False #make it true when a waypoint is encountered
#pullData = open('rndf_1_way_loop.txt',"r").read()
pullData = open('rndf_2_way_road.txt',"r").read()
dataArray = pullData.split('\n')
node_counter = 0
index = 0

rndf = c_rndf("RNDF_object")
for eachLine in dataArray:
    index += 1
    if len(eachLine)>1:
        it = eachLine.split(' ')
        #if any of these key words are encountered make connect previous false # it[0] == 'segment' or  #  it[0] == 'lane' or
        if  (it[0] == '/*' or it[0] == 'RNDF_name' or it[0] == 'num_segments' or it[0] == 'num_zones' \
            or it[0] == 'format_version' or it[0] == 'creation_date' or  it[0] == 'num_lanes' \
            or it[0] == 'segment_name' or it[0] == 'num_waypoints' or it[0] == 'lane_width' \
            or it[0] == 'left_boundary' or it[0] == 'right_boundary'  or it[0] == 'stop' or it[0] == 'end_lane' or it[0] == 'end_segment'\
            or it[0] == 'end_file' or it[0] == '</html>' ) :
            #Donot connect to previous way point
            connect_previous = False

        elif it[0] == 'segment':
            #create a segment and set parent as the rndf object
            s = c_segment(it[1],rndf, idn = int(it[1]))
            rndf.add_segment(s)
            connect_previous = False

        elif it[0] == 'lane':
            #New lane's parent is the latest of the segment in process
            l = c_lane(it[1], rndf.segments[-1],idn = int(it[1].split('.')[-1])) #
            rndf.segments[-1].add_lane(l)
            connect_previous = False

        elif it[0] == 'exit':
            connect_previous = False
            connections.append(eachLine)

        #else consider it as waypoint
        else :
            try:
                #New waypoint's parent is the latest line of the latest segment in consideration
                #rndf.segments[-1].lanes[-1].add_waypoint(name=it[0],coordi=[float(it[1]),float(it[2])],parent = rndf.segments[-1].lanes[-1])
                p = c_waypoint(name = it[0],coordi = [float(it[1]),float(it[2])],parent = rndf.segments[-1].lanes[-1], idn = int(it[0].split('.')[-1]))
                #add waypoint to the lane
                rndf.segments[-1].lanes[-1].add_waypoint(p)
                #add waypoint to the graph
                G.add_node(p, name=it[0])
            except Exception as ex:
                #print 'exception'
                print index
                print it[0]
                print ex

            if(connect_previous == True):
                #G.add_edge(node_counter-1,node_counter) #connect previous and current way point
                G.add_edge(p_old,p, weight = straight_weight)
            connect_previous = True # Enable such that the next way point will be connected to previous
            p_old = p
            node_counter += 1 #increment node counter


#Improve this code to add exits easily without so many iterations

#Add exits to the graph
#"""
if len(connections) >0:
    for txt in connections:
        if len(txt)>1:
            it = txt.split(' ')
            if it[0] == 'exit':
                for x in G.nodes():
                    if it[1] == x.name:
                        initial = x #entry node
                        break
                for x in G.nodes():
                    if it[2] == x.name:
                        final = x #exit node
                        break
                #add edge in graph
                G.add_edge(initial,final, weight = turn_weight)
                #weight = left_turn_weight if it[3]=='l' else right_turn_weight (#TODO use this weight to differentiate between left and right turns)
                # add the exit to the lane of the entry point with the lane as parent to exit
                initial.parent.add_exit(c_exit(entry = initial,exit = final, parent = initial.parent))



###Find the shortest path
# The indexes start from 0 and the names start from 1, check indexes and refer to map for points
s = rndf.segments[0].lanes[0].waypoints[0]
d = rndf.segments[1].lanes[1].waypoints[4]
path =  nx.shortest_path(G,source=s,target=d, weight= 'weight')
print s.name, d.name
for ob in path:
    print ob.name,ob.coordi



## Visulization
"""
#graph_pos = nx.shell_layout(G)
graph_pos = nx.fruchterman_reingold_layout(G)
nx.draw_networkx_nodes(G, graph_pos, node_size=1000, node_color='blue', alpha=0.3)
nx.draw_networkx_edges(G, graph_pos)
nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')
plt.show()
"""

##Code to print exits
"""
for s in rndf.segments:
    print s.name
    for l in s.lanes:
        print l.name
        for ex in l.exits:
            print ex.entry.name, ex.exit.name
"""

# code to print way points and it's neighbors
"""
i =0
for n in G.nodes():
    i = i+1
    print n.name, n.idn, n.parent.idn, n.parent.parent.idn, i
    for k in  G.neighbors(n):
        print k.name
"""

#print G.nodes()
#print G.number_of_nodes()
#print G.number_of_edges()
