# Q.1

class Data:
#Atributos 
    def __init__(self, dia: int, mes:int, ano:int):
        self.__dia=dia
        self.__mes=mes
        self.__ano=ano

#Construtores e Modificadores
    def get_dia(self):
        return self._dia

    def set_dia(self, dia):
        self.__dia=dia

    def get_mes(self):
        return self.__mes
    
    def set_mes(self, mes):
        self.__mes=mes

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano=ano
#Metodo
    def __str__(self,):
        return f"{self.__dia:02}/{self.__mes:02}/{self.__ano:04}"

# Programa para testar a classe Data
data = Data(8,11,2024)
print(f'Data Inicial: {data}')
data.set_dia(27), data.set_mes(9), data.set_ano(2025)
print(f'Nova data: {data}')

#Q.2
print('------Segunda Class------')
class Aluno:
#Construtor 
    def __init__ (self, matricula: int, nome: str, notas: list=[]):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas 

        if notas is None:
            self.notas = [] 
        else:
            self.notas = notas 
# Metodos                   
    def get_matricula(self):
        return self.matricula

    def get_nome(self):
        return self.nome

    def media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0
#Modificadores
    def set_nome(self, nome: str):
        self.nome = nome  

    def adiciona_notas(self, nota: float):
        self.notas.append(nota)


# Programa para testar a classe Aluno
aluno1 = Aluno(matricula=12345, nome="João Silva") 
print("Nome:", aluno1.get_nome()) 
print("Matrícula:", aluno1.get_matricula())  
aluno1.adiciona_notas(7.5)
aluno1.adiciona_notas(8.0)
aluno1.adiciona_notas(9.0)
print("Média das notas:", aluno1.media())  
aluno1.set_nome("João Pedro")
print("Novo nome:", aluno1.get_nome()) 

#Q.3
