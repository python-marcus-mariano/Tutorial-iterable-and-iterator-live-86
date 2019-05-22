"""
Exemplo 6
"""

'''
# Modificação 1


def raio_simplificador(lista_composta):
    """Função raio simplificador."""
    for elemento in lista_composta:
        yield elemento


lista_composta = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(raio_simplificador(lista_composta))


# print(next(raio_simplificador(lista_composta)))
# print(next(raio_simplificador(lista_composta)))

g = raio_simplificador(lista_composta)

print(next(g))
print(next(g))
print(next(g))
'''

'''
# Modificação 2

def raio_simplificador(lista_composta):
    """Função raio simplificador."""
    for elemento in lista_composta:
        for elementinho in elemento:
            yield elementinho


lista_composta = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

g = raio_simplificador(lista_composta)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
'''


# Modificação 2

def raio_simplificador(lista_composta):
    """Função raio simplificador."""
    for elemento in lista_composta:
        # yield from tem o mesmo comportamento do for dentro do for
        # yield from add on python 3.3
        yield from elemento


lista_composta = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

g = raio_simplificador(lista_composta)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
