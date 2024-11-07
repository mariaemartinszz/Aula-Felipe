class Pessoa:
    def _init_(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def imprimeDados(self):
        print(f"Nome: {self.nome}, Matrícula: {self.matricula}")

class AssistenteAdministrativo(Pessoa):
    pass

class Tecnico(Pessoa):
    pass

class Animal:
    def _init_(self, nome):
        self.nome = nome

    def caminhar(self):
        print(f"{self.nome} está caminhando.")

class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} está latindo: Au au!")

class Gato(Animal):
    def miar(self):
        print(f"{self.nome} está miando: Miau!")

class Rica:
    def _init_(self, nome, dinheiro):
        self.nome = nome
        self.dinheiro = dinheiro

    def gastarDinheiro(self):
        print(f"{self.nome} está gastando dinheiro. Saldo: R${self.dinheiro}")

class Pobre:
    def _init_(self, nome):
        self.nome = nome

    def trabalhar(self):
        print(f"{self.nome} está trabalhando muito.")

class Miseravel:
    def _init_(self, nome):
        self.nome = nome

    def mendigar(self):
        print(f"{self.nome} está mendigando.")

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

class CamaroteInferior(VIP):
    def imprimeCamarote(self):
        print("Ingresso VIP - Camarote Inferior")

class CamaroteSuperior(VIP):
    def imprimeCamarote(self):
        print("Ingresso VIP - Camarote Superior")

class Imovel:
    def _init_(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do imóvel: R${self.valor:.2f}")

class Novo(Imovel):
    def valorFinal(self):
        print(f"Imóvel novo. Valor final: R${self.valor * 1.1:.2f}") 

class Velho(Imovel):
    def valorFinal(self):
        print(f"Imóvel velho. Valor final: R${self.valor * 0.9:.2f}") 

class Teste:
    @staticmethod
    def main():
        
        assistente = AssistenteAdministrativo("Maria", "12345")
        tecnico = Tecnico("João", "54321")
        assistente.imprimeDados()
        tecnico.imprimeDados()

        cachorro = Cachorro("Rex")
        gato = Gato("Mimi")
        cachorro.latir()
        gato.miar()
        cachorro.caminhar()
        gato.caminhar()

        rica = Rica("Ana", 100000)
        pobre = Pobre("Carlos")
        miseravel = Miseravel("José")
        rica.gastarDinheiro()
        pobre.trabalhar()
        miseravel.mendigar()

        escolha = int(input("Digite 1 para ingresso Normal e 2 para ingresso VIP: "))
        if escolha == 1:
            ingresso = Ingresso(50)
            ingresso.imprimeValor()
            print("Ingresso Normal")
        elif escolha == 2:
            escolha_vip = int(input("Digite 1 para Camarote Superior e 2 para Camarote Inferior: "))
            if escolha_vip == 1:
                camarote_superior = CamaroteSuperior(50, 30)
                camarote_superior.imprimeCamarote()
                print(f"Valor: R${camarote_superior.valorVIP():.2f}")
            elif escolha_vip == 2:
                camarote_inferior = CamaroteInferior(50, 20)
                camarote_inferior.imprimeCamarote()
                print(f"Valor: R${camarote_inferior.valorVIP():.2f}")

        escolha_imovel = int(input("Digite 1 para imóvel novo e 2 para imóvel velho: "))
        if escolha_imovel == 1:
            imovel_novo = Novo(300000)
            imovel_novo.valorFinal()
        elif escolha_imovel == 2:
            imovel_velho = Velho(300000)
            imovel_velho.valorFinal()

if __name__ == "_main_":
    Teste.main()
