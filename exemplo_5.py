"""
Exemplo 5
"""

'''
# Modificação 1

#  Python abri o arquivo como um iterable
file = open('tabacaria.txt')

print(file)

print(next(file))
print(next(file))
print(next(file))
print(next(file))
'''

'''
# Modificação 2

def gen(file='tabacaria.txt'):
    """Função geradora."""
    for linha in open(file):
        # yield linha

        # strip retirar o \n no ipython        
        # yield linha.strip()
        
        # linha original e linha corrigida
        yield (linha, linha.strip())

# para usar no ipython comentar prints
# print(gen())

print(next(gen()))
# print(next(gen()))
# print(next(gen()))

# g = gen()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
'''

# Modificação 3

def gen(file='tabacaria.txt'):
    """Função geradora."""
    for linha in open(file):

        # linha original e linha corrigida
        yield (linha, linha.strip())

# ?
# for linha in gen():
#     print(linha)

# carregar como 'eager evalation' em uma lista
a = list(gen())
# print(a)


print(a[0])
print(a[-1])
