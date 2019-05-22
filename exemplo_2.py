"""
Exemplo 2
"""

# Modificação 1

# eager evalation - avaliação ansiosa - ocupa espaço em memória
# Quando se pede ao pc eu presciso disso, ele já fez (já calculou)
tabulada = [x*2 for x in range(1, 11)]

# lazy evaluation - avaliação preguiçosa - não ocupa espaço em memória
# vc pediu um iterable, se vira com ele
tabulada2 = (x*2 for x in range(1, 11))

print(tabulada)
print(tabulada2)


print(next(tabulada2))
print(next(tabulada2))
print(next(tabulada2))
print(next(tabulada2))
