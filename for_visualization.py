from visualiser.visualiser import Visualiser as vs
import os
# Set it to bin folder of graphviz  
os.environ["PATH"] += os.pathsep +  'C:/Program Files/Graphviz/bin/'  

from visualiser.visualiser import Visualiser as vs
import math

W = [[0, 2, 9], [1, 0, 4], [ math.inf, 5, 0]]

@vs( node_properties_kwargs={"shape":"record", "color":"#f57542", "style":"filled", "fillcolor":"grey"})
def D(k, i, j):
    if k == 0:
        return W[i][j]
    return min(D(k=k-1, i=i, j=j), D(k=k-1, i=i, j=k-1) + D(k=k-1, i=k-1, j=j))

def main():
    for i in range(0,3):
        for j in range(0,3):
            D(k=3, i=i, j=j)
    vs.make_animation("floyd2.gif", delay=0)

if __name__ == "__main__":
    main()