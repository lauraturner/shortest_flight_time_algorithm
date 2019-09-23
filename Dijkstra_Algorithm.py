import pandas as pd
import os.path

FILE_NAME = 'Dijkstra_Data_6.txt'
num_vert = pd.read_csv(FILE_NAME, nrows=1, header=None).iat[0,0]
graph = pd.read_csv(FILE_NAME, skiprows=1, header=None)

