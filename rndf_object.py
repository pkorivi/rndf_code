import networkx as nx

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

class c_segment(object):
    def __init__(self,name,parent,idn):
        self.name = name
        self.lanes = []
        self.parent = parent
        self.idn = idn
    def add_lane(self,lane):
        self.lanes.append(lane)

class c_rndf(object):
    def __init__(self,name):
        self.name = name
        self.segments= []
    def add_segment(self,segment):
        self.segments.append(segment)

class exit_info(object):
    def __init__(self, line_txt, segment, lane):
        self.line_txt = line_txt
        self.segment = segment
        self.lane = lane



G = nx.Graph()
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
            #New lane is always added to the latest of the segment
            l = c_lane(it[1], rndf.segments[-1],idn = int(it[1].split('.')[-1])) #
            rndf.segments[-1].add_lane(l)
            connect_previous = False
        elif it[0] == 'exit':
            connect_previous = False
            e = exit_info(line_txt= eachLine,segment = rndf.segments[-1], lane = rndf.segments[-1].lanes[-1])
            connections.append(e) # use these exit connections later to add edges for intersections

        #else consider it as waypoint
        else :
            try:
                #New waypoint is always added to the latest lane of the latest segment
                #rndf.segments[-1].lanes[-1].add_waypoint(name=it[0],coordi=[float(it[1]),float(it[2])],parent = rndf.segments[-1].lanes[-1])
                p = c_waypoint(name = it[0],coordi = [float(it[1]),float(it[2])],parent = rndf.segments[-1].lanes[-1], idn = int(it[0].split('.')[-1]))
                rndf.segments[-1].lanes[-1].add_waypoint(p)
                #G.add_node(node_counter, name=it[0],coordi=[float(it[1]),float(it[2])])
                G.add_node(p, name=it[0])
                #TODO add the way points directly here to graph...
            except Exception as ex:
                #print 'exception'
                print index
                print it[0]
                print ex
            #G.add_node(node_counter, name=it[0],coordi=[float(it[1]),float(it[2])])
            if(connect_previous == True):
                #G.add_edge(node_counter-1,node_counter) #connect previous and current way point
                G.add_edge(p_old,p)
            connect_previous = True # Enable such that the next way point will be connected to previous
            p_old = p
            node_counter += 1 #increment node counter


#Improve this code to add exits easily without so many iterations
#Add exits to the graph

#"""
if len(connections) >0:
    for exit in connections:
        if len(exit.line_txt)>1:
            initial = 0
            final = 0
            it = exit.line_txt.split(' ')
            if it[0] == 'exit':
                for x in G.nodes():
                    if it[1] == x.name:
                        entry = x #entry node
                        break
                for x in G.nodes():
                    if it[2] == x.name:
                        exit = x #exit node
                        break
                G.add_edge(entry,exit)
                entry.parent.add_exit(c_exit(entry,exit,entry.parent))



for s in rndf.segments:
    print s.name
    for l in s.lanes:
        print l.name
        for ex in l.exits:
            print ex.entry.name, ex.exit.name


#"""

#print rndf.segments[:].lanes[:].waypoints[:]
#print rndf.segments[0].lanes[0].waypoints[0].coordi

#print G.nodes()
#print G.number_of_nodes()
#print G.number_of_edges()
#for i in range(0,node_counter):
#    print i, G.node[i] , G.neighbors(i)
"""
i =0
for n in G.nodes():
    i = i+1
    print n.name, n.idn, n.parent.idn, n.parent.parent.idn, i
    for k in  G.neighbors(n):
        print k.name
"""
#for j in G.neighbors(40):
#    print G.node[j]['name']
