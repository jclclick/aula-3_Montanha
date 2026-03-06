# Exercício 4
    # Complexidade: O(n²)
    # Justificativa:
    # O algoritmo parece ter loops que comparam pares de elementos. Não entendi muito bem.

def pares_com_soma(lista, alvo):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                print(lista[i], lista[j])

pares_com_soma([1,2,3,4,5],5)