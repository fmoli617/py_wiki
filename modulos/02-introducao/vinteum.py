from enum import Enum
from dataclasses import dataclass, field
from typing import List
import random

class Valor(Enum):
    """ Classe enumeradora que define os valores de uma carta de baralho. """
    AS = 'A'
    DOIS = '2'
    TRES = '3'
    QUATRO = '4'
    CINCO = '5'
    SEIS = '6'
    SETE = '7'
    OITO = '8'
    NOVE = '9'
    DEZ = '10'
    VALETE = 'J'
    DAMA = 'Q'
    REI = 'K'

class Naipe(Enum):
    """ Classe enumeradora que define os naipes de uma carta de baralho. """
    OURO = '♦'
    ESPADA = '♠'
    COPAS = '♥'
    PAUS = '♣'

@dataclass(frozen=True)
class Carta:
    """ Classe que define uma carta de baralho. """
    valor: Valor
    naipe: Naipe

    def __eq__(self, other):
        if isinstance(other, Carta):
            return self.valor == other.valor and self.naipe == other.naipe
        elif isinstance(other, Valor):
            return self.valor == other
        else:
            return False

    def __str__(self):
        return self.valor.value + self.naipe.value

    def __repr__(self):
        return self.valor.value + self.naipe.value

class Baralho:
    """ Classe que define um baralho de cartas. """
    def __init__(self):
        self.__cartas = self.__novodeque()

    def __novodeque(self):
        """ Método de geração das cartas de forma ordenada. """
        cartas = [Carta(v, n) for v in list(Valor) for n in list(Naipe)]
        return self.__embaralhar(cartas)

    def __embaralhar(self, cartas):
        """
        [PARA FAZER]
        Método que embaralha as cartas.
        """
        raise NotImplementedError()

    def virar(self):
        """ Retira a carta do topo e remove do baralho. """
        return self.__cartas.pop()

@dataclass
class Jogador:
    """ Classe que define um jogador. """
    nome: str = field(default='')
    cartas: List[Carta] = field(default_factory=list)

    @property
    def score(self):
        return self.__calcularscore()

    def __calcularscore(self):
        """
        [PARA FAZER]
        Método que calcula o melhor score para o jogador.

        Regras:
        - Cartas com valores entre 2 e 10 (inclusive) possuem valor igual associado, ou seja, uma carta de valor 2,
          equivale a 2 pontos.
        - Valete, dama e rei possuem 10 pontos cada.
        - Ás pode valer 1 ou 11.
        - O melhor score deve levar em consideração de que não pode passar de 21 pontos.

        Exemplos:
        1) 2♦ J♦: 12 pontos
        2) A♥ A♦: 12 pontos
        3) A♥ A♦ 2♦ J♦: 14 pontos
        4) A♥ J♦: 21 pontos
        """
        raise NotImplementedError()

    def __str__(self):
        cartas = ' '.join(map(str, self.cartas))
        return f'{self.nome:<10}: {cartas} (score: {self.score})'

    def __repr__(self):
        cartas = ' '.join(map(str, self.cartas))
        return f'{self.nome:<10}: {cartas} (score: {self.score})'

@dataclass
class Banca(Jogador):
    """ Classe que define a banca do jogo. """
    nome: str = 'Banca'

class Jogo:
    """ Classe que define o jogo vinte e um. """
    def __init__(self):
        pass

    def mostrarinfo(self, jogador):
        """ Mostra informações do jogador. """
        print(str(jogador))

    def getvencedor(self, jogador, banca):
        """
        [PARA FAZER]
        Método que retorna quem venceu o jogo.

        Regras:
        - Jogador ou banca com mais de 21 pontos, perde.
        - No empate, a banca ganha.
        """
        raise NotImplementedError()

    def iniciar(self):
        """ Método que inicia o jogo vinte e um. """
        jogador = Jogador()
        banca = Banca()

        print()
        print('|==============================|')
        print('| BEM-VINDO AO JOGO VINTE E UM |')
        print('|==============================|')
        print()

        print('Seu nome:', end=' ')
        jogador.nome = input().capitalize()

        # loop do jogo
        while True:
            baralho = Baralho()
            jogador.cartas.clear()
            banca.cartas.clear()

            print()
            print('Embaralhando as cartas...')

            # loop do jogador
            while True:
                print()
                jogador.cartas.append(baralho.virar())
                self.mostrarinfo(jogador)

                if jogador.score >= 21:
                    break

                print('Deseja virar mais uma carta? [S ou N]', end=' ')
                resposta = input().upper()
                if resposta != 'S':
                    break

            if jogador.score <= 21:
                # loop da banca
                while banca.score < jogador.score:
                    banca.cartas.append(baralho.virar())

                print()
                print('Resultado:')
                self.mostrarinfo(jogador)
                self.mostrarinfo(banca)
                print()

            vencedor = self.getvencedor(jogador, banca)
            print(f'{vencedor.nome} venceu!')
            print('Gostaria de jogar novamente? [S ou N]', end=' ')
            resposta = input().upper()
            if resposta != 'S':
                break

if __name__ == '__main__':
    jogo = Jogo()
    jogo.iniciar()

