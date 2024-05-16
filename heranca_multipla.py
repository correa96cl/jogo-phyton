class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome 
    
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} esta amamentando."

class Ave(Animal):
    def voar(self):
        return f"{self.nome} esta voando"

class Morcego(Mamifero, Ave):
    def emitir_som(self):
        super().emitir_som()
        return "Morcegos emitem sons ultrassonicos"

morcego = Morcego(nome="Batman")

print("Nome do morcego:", morcego.nome)
print("Som do morcego:", morcego.emitir_som())

print("M<orcego amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())