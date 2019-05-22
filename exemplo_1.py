"""
Tutorial-iterable-and-iterator-live-86

Live de Python #86 - Iteradores e Geradores

Homepage and documentation:
https://github.com/kivy-tutorial/Tutorial-iterable-and-iterator-live-86

License: GNU GENERAL PUBLIC LICENSE Version 3
"""
'''
# Modificação 1

def gen_exemplo():
    """Função geradora."""
    print('Entrei na função')
    print('Entou na função')
    print('Entou na função p.2')
    print('Sai da função')


g = gen_exemplo()

print(g)
print(type(gen_exemplo))

'''

# Modificação 2

def gen_exemplo():
    """Função geradora."""
    print('Entrei na função')
    yield 'Primeiro'
    print('Entou na função')
    yield 'Segundo'
    print('Entou na função p.2')
    yield 'Ultimo'
    print('Sai da função')


g = gen_exemplo()

print(g)

print(type(gen_exemplo))
print(type(g))

print('-----------------------------------')

print(next(g))
print(next(g))
print(next(g))
# erro StopIteration
print(next(g))
