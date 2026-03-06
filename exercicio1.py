# Exercício 1
    # Complexidade: O(1)
    # Justificativa:
    # A função apenas verifica o tamanho da lista e retorna o primeiro elemento. 


def verificar_primeiro(lista):
    if len(lista) == 0:
        return None
    return lista[0]

print(verificar_primeiro([10,20,30]))