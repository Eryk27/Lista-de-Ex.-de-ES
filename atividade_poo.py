# Q.1
from types import DynamicClassAttribute


class Data:
    def __init__(self, dia: int, mes:int, ano:int):
        self._dia=dia
        self._mes=mes
        self._ano=ano

    def get_dia(self):
        return self._dia

    def set_dia(self, dia):
        self._dia=dia

    def get_mes(self):
        return self._mes
    
    def set_mes(self, mes):
        self._mes=mes

    def get_ano(self):
        return self._ano

    def set_ano(self, ano):
        self._ano=ano

    def __str__(self,):
        return f"{self._dia:02}/{self._mes:02}/{self._ano:04}"

data = Data(8,11,2024)
print(f'Data atual: {data}')
data.set_dia(27)
data.set_mes(9)
data.set_ano(2025)
print(f'Nova data: {data}')

