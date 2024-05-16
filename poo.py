

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Ola, meu nome e {self.nome} e eu tenho {self.idade} anos "

pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Marcelo", idade=43)
mensagem = pessoa2.saudacao()
print(mensagem)