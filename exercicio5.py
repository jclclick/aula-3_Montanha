# Exercício 5
    # Complexidade: O(n²)
    # Justificativa:
    # O primeiro bloco percorre a lista uma vez (O(n)). O segundo bloco possui dois loops aninhados que resultam em O(n²). Com isso considero a complexidade final O(n²). 


def imprimir_pares_e_soma(lista):

    # Bloco 1
    for i in range(len(lista)):
        print(lista[i])

    # Bloco 2
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i], lista[j])

imprimir_pares_e_soma([1,2,3])