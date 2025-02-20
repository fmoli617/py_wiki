def cumprimentar(nome):
    """ Função que passa o cumprimento dado um nome. """
    print(f'Seja bem-vindo, {nome}!')

def raizes(a, b, c):
    """ Função que calcula as raízes da equação ax**2 + bx + c """
    delta = b**2 - 4*a*c
    if delta < 0:
        raise ValueError('Delta negativo')

    x1 = (-b + delta**0.5) / 2*a
    x2 = (-b - delta**0.5) / 2*a
    return x1, x2