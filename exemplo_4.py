"""
Exemplo 4
"""

# Modificação 1

sec = range(10)

def gen(sec):
    """Função gen."""
    for valor in sec:
        yield valor

g = gen(sec)

# print(sec)

# print(g)

print(next(g))
print(next(g))
print(next(g))

print(list(g))
