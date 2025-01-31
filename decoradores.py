from typing import Any


def meu_decodaror(func):
    def wrapper():
        print("Antes da funcao ser chamada")
        func()
        print("Depois da funcao ser chamado")
    return wrapper

@meu_decodaror
def minha_funcao():
    print("Minha funcao foi chamada")

minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> Any:
        print("Antes da funcao ser chamada (decorador de classe)")
        self.func()
        print("Depois da funcao ser chamada (decorador de classe)")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda funcao foi chamada")

segunda_funcao()