## WAY Point Extraction
### Lab Map
1- Download the Lab_map_600x400.png
2- Write a .yaml file to describe the map (http://wiki.ros.org/map_server)
3- Run the map_server (http://wiki.ros.org/map_server)
5- open the map in Rviz and show the map
4- Write a node to subscribe to clicked_points
5- click on the center of street (map) continuously and save the list of
the points.
6-  Save these points in the RNDF file format.
7- save them in a file.

For a 2 way map, parallel points to the center line on the lane can be extracted using "parallel_lines.py", 
edit : get_parallel_pts(xar, yar, -0.175) # use +0.175 for parallel points on other side.
       pts = #for number of points in the file. 

"plot.py" can be used to plot the values and check on map

## RNDF Graph Creation 

"rndf_graph.py" is the file for parsing the data from the the rndf_file.txt and converting it to a graph. The edges are weighted with distance between the points. 
  
nx.shortest_path() can be used for finding the shortest path between nodes.

## Installation

This code needs (networkx libarary)[https://networkx.github.io/documentation/networkx-1.10/overview.html]. The documentation has 
steps to install and how to use different functions. 

