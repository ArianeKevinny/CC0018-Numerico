import numpy as np


def bissecao(f,a,b,tol,N,tabela=False):
    """
    Esta função contém uma implementação do método da bisseção para o␣
    cálculo de zeros de funções.
    
    Parâmetros
    ----------
    f : function
        Função definida no intervalo [a,b] com f(a)*f(b) < 0.5
    a : float
        Extremidade esquerda do intervalo de definição de 'f'.
    b : float
        Extremidade direita do intervalo de definição de 'f'.
    tol : float
        Tolerância desejada usada como critério de parada.
    N : int
        Número máximo de iterações permitido.
    tabela : bool
        Variável usada para indicar se o usuário deseja ou não␣
        imprimir uma tabela com informações de cada passo realizado pelo
        algoritmo.
        (o valor padrão é False)
    Retorno
    -------
        i : int
            Número de iterações realizadas.
        p : float
            Valor aproximado do zero de f com a tolerância desejada,
            caso haja convergência.
    """
    # Pré-requisito: a <= b
    assert not (a > b)

    # Pré-requisito: f(a)*f(b) < 0
    fa = f(a)
    fb = f(b)
    assert not (np.sign(fa)*np.sign(fb) >= 0)
    
    # Imprime cabeçalho da tabela, caso desejado
    if (tabela):
        print(f"{'i':11s} {'a':^12s} {'b':^12s} {'p':^12s} {'fa':^12s} ␣{'fb':^12s} {'fp':^12s}")
        
    i = 1 # contador de iterações
    while i <= N:
        p = a + 0.5*(b - a)
        fp = f(p)

        # Imprime cabeçalho da tabela, caso desejado
        if (tabela):
            print(f"{i:^11d} {a:+.5e} {b:+.5e} {p:+.5e} {fa:+.5e} {fb:+.5e} {fp:+.5e}")
        
        if 0.5*(b-a) < tol:
            break
        
        i = i + 1
        if np.sign(fa)*np.sign(fp) > 0:
            a = p
            fa = fp
        else:
            b = p

    if i > N:
        print("Número máximo de iterações atingido!")
        i = i - 1

    return i,p

    
def f(x):
    return np.log(x) + x**2 -3
    
print(bissecao(f,1,2,1e-3,100,True))

    
    
