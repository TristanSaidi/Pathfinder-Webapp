from main import *
from tile import *

tilelist = initialize(28,60)
calculateDistancesfrom(12,8)

tile1adjacencylist = tilelist[1].getadjacencylist()

shortestpath = getDijkstraPathTo(20,20)

#print("Tile 1 Adjacency List: \n")
#for current in tile1adjacencylist:
#    xcoordinate = current.getx()
#    ycoordinate = current.gety()
#    print("(",xcoordinate, ", ", ycoordinate,")")
#
#print("")

print("Shortest Path: \n")

for current in shortestpath:
    xcoordinate = current.getx()
    ycoordinate = current.gety()
    print("(",xcoordinate, ", ", ycoordinate,")")