import numpy as np

FILE_NAME = "A2_test.txt"
GRAPH = np.loadtxt(FILE_NAME, skiprows=1) 
vertexes = len(GRAPH[0])
for vertex in GRAPH: 
