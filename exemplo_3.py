"""
Exemplo 3
"""
'''
# Modificação 1

def count():
    """Função count."""
    i = 0
    while True:
        yield i
        i += 1

c = count()

print(type(c))

for valor in c:
    print((valor))
'''

# Modificação 2

def count():
    """Função count."""
    i = 0
    while True:
        yield i
        i += 1

c = count()

mults1 = [next(c)*10 for x in range(10)]
mults2 = [next(c)*10 for x in range(10)]

print(mults1)
print(mults2)

print(next(c))
print(next(c))
print([next(c)*10 for x in range(10)])
