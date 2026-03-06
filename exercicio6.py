# Exercício 6
    # Complexidade: O(log n)
    # Justificativa:
    # A variável i dobra de valor a cada iteração. 


def potencias_de_dois(n):
    i = 1
    while i < n:
        print(i)
        i *= 2

potencias_de_dois(16)