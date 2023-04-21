import numpy as np
import matplotlib.pyplot as plt

def plota(F, a, b, fixo=False):

    fig, ax = plt.subplots()
    ax.set_ylabel('f(x)')
    ax.set_xlabel('x')
    ax.grid()

    plt.axhline(0, color='black', linewidth=1)

    x = np.linspace(a,b,100)
    i = 0

    for f in F:
        y = f(x)
        if (fixo):
            ax.plot(x,y,label='g'+str(i))
        else:
            ax.plot(x,y)
        i = i + 1

    if (fixo):
        ax.plot(x,x)
        plt.legend()
    
    plt.xlim([a, b])

    if (fixo):
        plt.ylim([a, b])
    
    plt.show()

def ponto_fixo(g,p0,tol,N,tabela=False):
    """
    Esta função contém uma implementação do método do ponto fixo.
    
    Parâmetros
    ----------
        f : function
            Função definida no intervalo [a,b] com f(a)*f(b) < 0.
        p0 : float
            Chute inicial.
        tol : float
            Tolerância desejada usada como critério de parada.
        N : int
            Número máximo de iterações permitido.
        tabela : bool
            Variável usada para indicar se o usuário deseja ou não imprimir uma
            tabela com informações de cada passo realizado pelo algoritmo.
            (o valor padrão é False)

    Retorno
    -------
        i : int
            Número de iterações realizadas.
        p : float
            Valor aproximado do zero de f com a tolerância desejada,
            caso haja convergência.
    """   
    # Imprime cabeçalho da tabela, caso desejado
    if (tabela):
        print(f"{'i':11s} {'p0':^12s} {'p':^12s} {'|p - p0|':^12s}")
        
    i = 1
    while i <= N:
        p = g(p0)
        
        # Imprime os dados da iteração
        if (tabela):
            print(f"{i:^11d} {p0:+.5e} {p:+.5e} {abs(p - p0):+.5e}")
            
        err = tol*max(1.0, abs(p))
        if abs(p - p0) < err:
            break
        i = i + 1
        p0 = p
        
    if i > N:
        print("Número máximo de iterações atingido!")
        i = i - 1
        
    return i,p


def f(x):
    return 2/x - (1/(x**2))

def g(x):
    return -1 * ( x**2 - 4*x + 2)

print(ponto_fixo(g,0.9,1e-3,100,True))