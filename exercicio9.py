# Exercício 9
    # Complexidade: 
    # Justificativa:
    # Achei mais complicada essa lógica de loop para matrizes


def produto_de_matrizes(A, B, n):
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

A=[[1,2],[3,4]]
B=[[5,6],[7,8]]

print(produto_de_matrizes(A,B,2))