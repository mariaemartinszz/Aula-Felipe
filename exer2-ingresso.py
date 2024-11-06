class Ingresso:
    def _init_(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do ingresso: R${self.valor:.2f}")

class VIP(Ingresso):
    def _init_(self, valor, adicional):
        super()._init_(valor)
        self.adicional = adicional

    def valorVIP(self):
        return self.valor + self.adicional

class Normal(Ingresso):
    def imprimeIngresso(self):
        print("Ingresso Normal")


class CamaroteInferior(VIP):
    def _init_(self, valor, adicional, localizacao):
        super()._init_(valor, adicional)
        self.localizacao = localizacao

    def imprimeLocalizacao(self):
        print(f"Localização do ingresso: {self.localizacao}")

class CamaroteSuperior(VIP):
    def _init_(self, valor, adicional, adicionalSuperior):
        super()._init_(valor, adicional)
        self.adicionalSuperior = adicionalSuperior

    def valorCamaroteSuperior(self):
        return self.valorVIP() + self.adicionalSuperior
