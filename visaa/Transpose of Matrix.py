n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
transpose_matrix=[[matrix[j][i] for j in range(n)] for i in range(n)]

for r in transpose_matrix:
    print(*r)
