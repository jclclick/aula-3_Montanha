# Exercício 2
    # Complexidade: O(n)
    # Justificativa:
    # O algoritmo percorre todos os elementos da lista utilizando um loop. Com ele fazendo que o número de operações cresça proporcionalmente ao tamanho da lista.


def somar_lista(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total

print(somar_lista([1,2,3,4,5]))