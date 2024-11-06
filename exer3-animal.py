class Animal:
    def init(self, nome, raca):
        self.nome = nome
        self.raca = raca
    def caminha(self):
        return "O animal está caminhando"

class Cachorro(Animal):
    def init(self, nome, raca):
        super().init(nome, raca)
    def late(self):
        return "O cachorro está latindo"

class Gato(Animal):
    def init(self, nome, raca):
        super().init(nome, raca)
    def mia(self):
        return "O gato está miando"

cachorro = Cachorro("loki", "lulu da pulmerania")
print(cachorro.late())
print(cachorro.caminha())
print(cachorro.nome)
print(cachorro.raca)

gato = Gato("harry", "siames")
print(gato.mia())
print(gato.caminha())
print(gato.nome)
print(gato.raca)
