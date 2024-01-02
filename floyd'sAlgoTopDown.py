import math
def ShortestPath(k, i, j, W):
    if k == 0:
        return W[i][j]
    return min(ShortestPath(k-1, i, j, W),
                ShortestPath(k-1, i, k-1 ,W) + ShortestPath(k-1, k-1, j, W))

if __name__ == "__main__":
    W = [[0, 2, 9], [1, 0, 4], [ math.inf, 5, 0]]
    k = 3
    D = [[[0 for _ in range(k)] for _ in range(k)] for _ in range(k+1)]
    for i in range(0,k):
        for j in range(0,k):
            D[k][i][j] = ShortestPath(k, i, j, W)
            print(D[k][i][j])
