"""
Exemplo gerenciador de contexto
"""

# Modificação 1


from contextlib import contextmanager
from os import getcwd, chdir
from os.path import abspath


@contextmanager
def muda_de_pasta(path):
    """Função muda de pasta."""
    path_original = getcwd()
    chdir(path)
    yield
    chdir(path_original)


print(getcwd())

with muda_de_pasta(abspath('..')):
    print(getcwd())

print(getcwd())
