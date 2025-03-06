import json

class Funcionario:
    """Classe base para representar um funcionário."""
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def calcular_bonus(self):
        """Método genérico para cálculo de bônus (sobrescrito nas subclasses)."""
        return 0
    
    def detalhes(self):
        return f"Nome: {self.nome}, Salário: R${self.salario:.2f}, Bônus: R${self.calcular_bonus():.2f}"

# Subclasse Gerente herdando de Funcionario
class Gerente(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.20  # 20% de bônus

# Subclasse Desenvolvedor herdando de Funcionario
class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.10  # 10% de bônus

# Subclasse Estagiario herdando de Funcionario
class Estagiario(Funcionario):
    def calcular_bonus(self):
        return self.salario * 0.05  # 5% de bônus

# Classe para gerenciar funcionários
class SistemaFuncionarios:
    def __init__(self, arquivo_dados="funcionarios.json"):
        self.arquivo_dados = arquivo_dados
        self.funcionarios = []
        self.carregar_dados()
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        self.salvar_dados()
    
    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario.detalhes())
    
    def salvar_dados(self):
        with open(self.arquivo_dados, "w") as f:
            json.dump([vars(f) for f in self.funcionarios], f)
    
    def carregar_dados(self):
        try:
            with open(self.arquivo_dados, "r") as f:
                dados = json.load(f)
                for d in dados:
                    if d["__class__"] == "Gerente":
                        self.funcionarios.append(Gerente(d["nome"], d["salario"]))
                    elif d["__class__"] == "Desenvolvedor":
                        self.funcionarios.append(Desenvolvedor(d["nome"], d["salario"]))
                    elif d["__class__"] == "Estagiario":
                        self.funcionarios.append(Estagiario(d["nome"], d["salario"]))
        except FileNotFoundError:
            pass

# Criando e testando o sistema
sistema = SistemaFuncionarios()
sistema.adicionar_funcionario(Gerente("Carlos", 10000))
sistema.adicionar_funcionario(Desenvolvedor("Ana", 6000))
sistema.adicionar_funcionario(Estagiario("João", 2000))

sistema.listar_funcionarios()
