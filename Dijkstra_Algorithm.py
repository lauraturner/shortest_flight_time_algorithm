import pandas as pd
import numpy as np

def find_min(remaining, dist):
    minimum = float('inf')
    min_indx = None
    for v in remaining: 
        if dist[v] < minimum:
            minimum = dist[v]
            min_indx = v
    return min_indx

start = 0
FILE_NAME = 'Dijkstra_Data_1600.txt'
num_vert = pd.read_csv(FILE_NAME, nrows=1, header=None).iat[0,0]
graph = pd.read_csv(FILE_NAME, skiprows=1, header=None, sep='\t')
graph = graph.drop(graph.columns[num_vert], axis=1)
dist = [None] * num_vert
prev = [None] * num_vert
remaining = []

for v in graph.index:
    dist[v] = float('inf')
    prev[v] = None
    remaining.append(int(v))

print(graph.index)

dist[start] = 0

while len(remaining) > 0:
    current = find_min(remaining, dist)
    remaining.remove(current)
    graph = graph.drop(current, axis=1)
    for i in graph.columns:
        if graph.at[current, i] == 0:
            continue
        est = dist[current] + graph.at[current, i]
        if est < dist[i]:
            dist[i] = est
            prev[i] = current






