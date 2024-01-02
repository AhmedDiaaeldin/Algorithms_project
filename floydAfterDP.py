import math
def ShortestPath(k, i, j, D):
    if D[k][i][j] == -1:
        D[k][i][j]= min(ShortestPath(k-1, i, j, D),
                ShortestPath(k-1, i, k ,D) + ShortestPath(k-1, k, j, D))
    return D[k][i][j]

if __name__ == "__main__":
    W = [[0, 2, 9], [1, 0, 4], [ math.inf, 5, 0]]
    k = 3
    D = [[[-1 for _ in range(k)] for _ in range(k)] for _ in range(k+1)]
    D[0]=W
    for i in range(0,k):
        for j in range(0,k):
            ShortestPath(k, i, j, D)
            print(D[k][i][j])



