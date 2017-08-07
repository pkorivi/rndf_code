## RNDF Parser 

Code to parse RNDF files and extract information to an rndf object then build a graph connecting all the way points with
weighted edges. 

Currently shortest path between source node and destination node are displayed. Different weights can be added to turns, moving straight etc.

The objects for way points, exits, lanes and segments are bu directional with reference to parents. Thus it will be easy to find the neighboring lanes to current lane, or neighboring points to a way point if needed. 


## Installation

This code needs (networkx libarary)[https://networkx.github.io/documentation/networkx-1.10/overview.html]. The documentation has 
steps to install and how to use different functions. 

