# Exercício 3
    # Complexidade: O(log n)
    # Justificativa:
    # A cada iteração o algoritmo reduz pela metade o espaço de busca. 


def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

print(busca_binaria([1,2,3,4,5,6,7],4))