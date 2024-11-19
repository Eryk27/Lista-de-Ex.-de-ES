class Carta:
    def __init__(self, valor, naipe):
        self.__valor = valor
        self.__naipe = naipe

    def getNaipe(self):
        return self.__naipe

    def getValor(self):
        return self.__valor

    def __repr__(self):
        valores = {1: 'Ás', 2: '2', 3: '3', 4: '4', 5: '5',
                   6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
                   11: 'Valete', 12: 'Dama', 13: 'Rei'}
        return f'{valores[self.__valor]} de {self.__naipe}'

import random

class Baralho:
    def __init__(self):
        self.__cartas = []
        self.naipes = ['Paus', 'Ouro', 'Copas', 'Espadas']
        self.valores = list(range(1, 14))

        for naipe in self.naipes:
            for valor in self.valores:
                self.__cartas.append(Carta(valor, naipe))

    def misturar(self):
        random.shuffle(self.__cartas)

    def distribuir_cartas(self, jogadores):
        cartas_por_jogador = len(self.__cartas) // len(jogadores)
        restantes = len(self.__cartas) % len(jogadores)

        mãos = [[] for _ in range(len(jogadores))]
        indice_carta = 0

        for i in range(cartas_por_jogador):
            for j in range(len(jogadores)):
                mãos[j].append(self.__cartas[indice_carta])
                indice_carta += 1

        for i in range(restantes):
            mãos[i].append(self.__cartas[indice_carta])
            indice_carta += 1

        return mãos

class Jogador:
    def __init__(self, nome):
        self._nome = nome
        self._mao = []

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def adicionar_cartas(self, cartas):
        self._mao.extend(cartas)

    def puxar_carta(self):
        if self._mao:
            return self._mao.pop(0)
        else:
            return None

def simular_batalha(jogador1, jogador2):
    batalha = 1
    cartas_jogadas = []

    while jogador1._mao and jogador2._mao:
        print(f"\nBatalha {batalha}:")
        batalha += 1

        carta1 = jogador1.puxar_carta()
        carta2 = jogador2.puxar_carta()

        if not carta1 or not carta2:
            break

        print(f"{jogador1.getNome()} jogou: {carta1}")
        print(f"{jogador2.getNome()} jogou: {carta2}")

        cartas_jogadas.extend([carta1, carta2])

        if isinstance(carta1, Carta) and isinstance(carta2, Carta):
            if carta1.getValor() > carta2.getValor():
                print(f"{jogador1.getNome()} ganhou esta batalha!")
                jogador1.adicionar_cartas(cartas_jogadas)
                cartas_jogadas = []
            elif carta1.getValor() < carta2.getValor():
                print(f"{jogador2.getNome()} ganhou esta batalha!")
                jogador2.adicionar_cartas(cartas_jogadas)
                cartas_jogadas = []
            else:
                print("Empate Puxando mais cartas...")
                while True:
                    if len(jogador1._mao) < 3 or len(jogador2._mao) < 3:
                        break
                    for _ in range(3):
                        carta1 = jogador1.puxar_carta()
                        carta2 = jogador2.puxar_carta()
                        cartas_jogadas.extend([carta1, carta2])
                        print(f"{jogador1.getNome()} jogou: {carta1}")
                        print(f"{jogador2.getNome()} jogou: {carta2}")
                    if isinstance(carta1, Carta) and isinstance(carta2, Carta):
                        if carta1.getValor() > carta2.getValor():
                            print(f"{jogador1.getNome()} ganhou esta batalha!")
                            jogador1.adicionar_cartas(cartas_jogadas)
                            cartas_jogadas = []
                            break
                        elif carta1.getValor() < carta2.getValor():
                            print(f"{jogador2.getNome()} ganhou esta batalha!")
                            jogador2.adicionar_cartas(cartas_jogadas)
                            cartas_jogadas = []
                            break
                        else:
                            print("Empate novamente Puxando mais cartas...")
        else:
            print("Erro: Cartas não são objetos Carta.")
            break

        print(f"Cartas restantes de {jogador1.getNome()}: {len(jogador1._mao)}")
        print(f"Cartas restantes de {jogador2.getNome()}: {len(jogador2._mao)}")

    if len(jogador1._mao) > len(jogador2._mao):
        print(f"{jogador1.getNome()} ganhou o jogo!")
    elif len(jogador1._mao) < len(jogador2._mao):
        print(f"{jogador2.getNome()} ganhou o jogo!")
    else:
        print("Empate no final do jogo!")

def main():
    nome1 = input("Digite o nome do jogador 1: ")
    nome2 = input("Digite o nome do jogador 2: ")

    jogador1 = Jogador(nome1)
    jogador2 = Jogador(nome2)

    baralho = Baralho()
    baralho.misturar()
    mãos = baralho.distribuir_cartas([jogador1, jogador2])

    jogador1.adicionar_cartas(mãos)
    jogador2.adicionar_cartas(mãos[1])

    simular_batalha(jogador1, jogador2)

if __name__ == "__main__":
    main()