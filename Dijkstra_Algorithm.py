import pandas as pd
import numpy as np

# find the minimum current arrival time of the remaining locations
def find_min(remaining, arrival):
    minimum = float('inf')
    min_indx = None
    for v in remaining: 
        if arrival[v] < minimum:
            minimum = arrival[v]
            min_indx = v
    return min_indx

# find the path of the shortest flight to the destination
def get_path(prev, end):
    path = []
    i = end
    path.append(end)
    while prev[i] != None:
        path.append(prev[i])
        i = prev[i]
    return path

# print the results of the algorithm
def print_results(path, start, end, arrival):
    print('Optimal route from {} to {} \n'.format(start, end))
    for i in range(len(path) - 1, 0, -1):
        print('Fly from {} to {}'.format(path[i] , path[i - 1]))
    print('\nArrive at {} at time {}'.format(end, arrival[end]))

# Main algorithm to find the shortest flight
def shortest_flight(FILE_NAME, start, end):

    # get data from the text file
    locs = pd.read_csv(FILE_NAME, nrows=1, header=None).iat[0,0]
    graph = pd.read_csv(FILE_NAME, skiprows=1, header=None, sep='\t')

    # set up variables for the algorithm
    arrival = [None] * locs
    prev = [None] * locs
    remaining = []
    for v in range(0, locs):
        arrival[v] = float('inf')
        prev[v] = None
        remaining.append(int(v))
    arrival[start] = 0

    while len(remaining) > 0:
        current = find_min(remaining, arrival)
        #break if the shortest path has already been found 
        if current == end:
            break
        remaining.remove(current)
        for _, row in graph.loc[graph[0] == current].iterrows():
            if row[3] < arrival[row[1]] and arrival[current] < row[2]:
                arrival[row[1]] = row[3]
                prev[row[1]] = current

    # check to see if a path was found to the destination
    if arrival[end] == float('inf'):
        print('There is no path from {} to {}'.format(start, end))
    else:
        path = get_path(prev, end)
        print_results(path, start, end, arrival)

# Initial parameters
start = 99
end = 87
FILE_NAME = '2019_Lab_2_flights_real_data.txt'
shortest_flight(FILE_NAME, start, end)
