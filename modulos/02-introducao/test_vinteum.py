from vinteum import *

def teste_unitario(function):
    def wrapper():
        func_name = function.__name__

        print(f'{func_name}...', end=' ')

        try:
            result = function()
        except:
            result = False

        print('OK' if result else 'Não passou no teste.')

    return wrapper

@teste_unitario
def test_Baralho_embaralhar_tamanho_final():
    baralho = Baralho()
    return len(baralho._Baralho__cartas) == 52

@teste_unitario
def test_Baralho_embaralhar_embaralhou():
    novodeque = [Carta(v, n) for v in list(Valor) for n in list(Naipe)]
    baralho = Baralho()
    igual = all([novodeque[i] == baralho._Baralho__cartas[i] for i in range(52)])
    return not igual

@teste_unitario
def test_Baralho_embaralhar_duplicados():
    baralho = Baralho()
    strlist = [str(c) for c in baralho._Baralho__cartas]
    set1 = set(strlist)
    return len(set1) == 52

@teste_unitario
def test_Baralho_embaralhar_seed():
    b1 = Baralho()
    b2 = Baralho()
    igual = all([b1._Baralho__cartas[i] == b2._Baralho__cartas[i] for i in range(52)])
    return not igual

@teste_unitario
def test_Jogador_score_soma_simples():
    jogador = Jogador()
    jogador.cartas.append(Carta(Valor.DOIS, Naipe.OURO))
    jogador.cartas.append(Carta(Valor.QUATRO, Naipe.PAUS))
    return jogador.score == 6

@teste_unitario
def test_Jogador_score_soma_simples_com_figuras():
    jogador = Jogador()
    jogador.cartas.append(Carta(Valor.VALETE, Naipe.OURO))
    jogador.cartas.append(Carta(Valor.QUATRO, Naipe.PAUS))
    return jogador.score == 14

@teste_unitario
def test_Jogador_score_1as():
    jogador = Jogador()
    jogador.cartas.append(Carta(Valor.AS, Naipe.OURO))
    return jogador.score == 11

@teste_unitario
def test_Jogador_score_2as():
    jogador = Jogador()
    jogador.cartas.append(Carta(Valor.AS, Naipe.OURO))
    jogador.cartas.append(Carta(Valor.AS, Naipe.ESPADA))
    return jogador.score == 12

@teste_unitario
def test_Jogador_score_1as_1carta():
    jogador = Jogador()
    jogador.cartas.append(Carta(Valor.AS, Naipe.OURO))
    jogador.cartas.append(Carta(Valor.REI, Naipe.OURO))
    return jogador.score == 21

@teste_unitario
def test_Jogador_score_1as_2cartas():
    jogador = Jogador()
    jogador.cartas.append(Carta(Valor.AS, Naipe.OURO))
    jogador.cartas.append(Carta(Valor.REI, Naipe.OURO))
    jogador.cartas.append(Carta(Valor.DAMA, Naipe.ESPADA))
    return jogador.score == 21

@teste_unitario
def test_Jogador_score_2as_2cartas():
    jogador = Jogador()
    jogador.cartas.append(Carta(Valor.AS, Naipe.OURO))
    jogador.cartas.append(Carta(Valor.OITO, Naipe.OURO))
    jogador.cartas.append(Carta(Valor.OITO, Naipe.ESPADA))
    jogador.cartas.append(Carta(Valor.AS, Naipe.ESPADA))
    return jogador.score == 18

@teste_unitario
def test_Jogo_getvencedor_jogador_acima_21():
    jogador = Jogador()
    jogador.cartas.append(Carta(Valor.REI, Naipe.OURO))
    jogador.cartas.append(Carta(Valor.DAMA, Naipe.ESPADA))
    jogador.cartas.append(Carta(Valor.TRES, Naipe.OURO))

    banca = Banca()

    return Jogo().getvencedor(jogador, banca).nome == banca.nome

@teste_unitario
def test_Jogo_getvencedor_jogador_dentro_banca_acima_21():
    jogador = Jogador()
    jogador.cartas.append(Carta(Valor.REI, Naipe.OURO))
    jogador.cartas.append(Carta(Valor.DAMA, Naipe.ESPADA))

    banca = Banca()
    banca.cartas.append(Carta(Valor.SETE, Naipe.OURO))
    banca.cartas.append(Carta(Valor.OITO, Naipe.OURO))
    banca.cartas.append(Carta(Valor.VALETE, Naipe.OURO))

    return Jogo().getvencedor(jogador, banca).nome == jogador.nome

@teste_unitario
def test_Jogo_getvencedor_jogador_dentro_banca_abaixo():
    jogador = Jogador()
    jogador.cartas.append(Carta(Valor.REI, Naipe.OURO))
    jogador.cartas.append(Carta(Valor.DAMA, Naipe.ESPADA))

    banca = Banca()
    banca.cartas.append(Carta(Valor.SETE, Naipe.OURO))
    banca.cartas.append(Carta(Valor.OITO, Naipe.OURO))

    return Jogo().getvencedor(jogador, banca).nome == jogador.nome

@teste_unitario
def test_Jogo_getvencedor_empate():
    jogador = Jogador()
    jogador.cartas.append(Carta(Valor.AS, Naipe.OURO))
    jogador.cartas.append(Carta(Valor.DAMA, Naipe.ESPADA))

    banca = Banca()
    banca.cartas.append(Carta(Valor.SETE, Naipe.OURO))
    banca.cartas.append(Carta(Valor.OITO, Naipe.OURO))
    banca.cartas.append(Carta(Valor.SEIS, Naipe.OURO))

    return Jogo().getvencedor(jogador, banca).nome == banca.nome

if __name__ == '__main__':
    print('Testando método Baralho.embaralhar()')
    test_Baralho_embaralhar_tamanho_final()
    test_Baralho_embaralhar_embaralhou()
    test_Baralho_embaralhar_duplicados()
    test_Baralho_embaralhar_seed()

    print()
    print('Testando propriedade Jogador.score')
    test_Jogador_score_soma_simples()
    test_Jogador_score_soma_simples_com_figuras()
    test_Jogador_score_1as()
    test_Jogador_score_2as()
    test_Jogador_score_1as_1carta()
    test_Jogador_score_1as_2cartas()
    test_Jogador_score_2as_2cartas()

    print()
    print('Testando método Jogo.getvencedor()')
    test_Jogo_getvencedor_jogador_acima_21()
    test_Jogo_getvencedor_jogador_dentro_banca_acima_21()
    test_Jogo_getvencedor_jogador_dentro_banca_abaixo()
    test_Jogo_getvencedor_empate()