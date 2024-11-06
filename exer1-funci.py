class Funcionario:
    def _init_(self, nome, salario):
        self.nome = nome
        self.salario = salario

        
class Assistente(Funcionario):
    def _init_(self, nome, salario, matricula):
        super()._init_(nome, salario)
        self.matricula = matricula

    def exibe_dados(self):
        super().exibe_dados()
        print(f"Matrícula: {self.matricula}")

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula

    def add_aumento(self, valor):
        self.salario += valor

    def ganho_anual(self):
        return self.salario * 12

    def exibe_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: {self.salario:.2f}")
        print(f"Ganho Anual: {self.ganho_anual():.2f}")


class Tecnico(Assistente):
    def _init_(self, nome, salario, matricula, bonus_salarial):
        super()._init_(nome, salario, matricula)
        self.bonus_salarial = bonus_salarial

    def ganho_anual(self):
        return (self.salario + self.bonus_salarial) * 12

    def exibe_dados(self):
        super().exibe_dados()
        print(f"Bônus Salarial: {self.bonus_salarial:.2f}")
        print(f"Ganho Anual (com bônus): {self.ganho_anual():.2f}")


class Administrativo(Assistente):
    def _init_(self, nome, salario, matricula, turno, adicional_noturno):
        super()._init_(nome, salario, matricula)
        self.turno = turno
        self.adicional_noturno = adicional_noturno

    def ganho_anual(self):
        salario_base = self.salario
        if self.turno.lower() == 'noite':
            salario_base += self.adicional_noturno
        return salario_base * 12

    def exibe_dados(self):
        super().exibe_dados()
        print(f"Turno: {self.turno}")
        if self.turno.lower() == 'noite':
            print(f"Adicional Noturno: {self.adicional_noturno:.2f}")
        print(f"Ganho Anual (com adicional): {self.ganho_anual():.2f}")  
