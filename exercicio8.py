# Exercício 8
    # Complexidade: O(n²)
    # Justificativa:
    # Neste tem uma comparação e troca de elementos.


def ordenacao_bolha(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print(ordenacao_bolha([5,3,8,2]))