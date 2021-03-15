
class Automato:
    '''
    a funcao programa vai ser definida nas funcoes do automato
    '''

    def __init__(self):
        sigma = [] # alfabeto
        Q = [] # conjunto de estados
        q0 = '' # estado inicial
        F = [] # conjunto de estados finais
        delta = [] # alfabeto de símbolos de saída

    def automatoTeste(self):
        res = Automato()
        res.sigma = ['a', 'b', 'c']
        res.Q = ['n1', 'n2']
        res.q0 = 'n1'
        res.delta = ['c11', 'c12', 'c21', 'c22']
        res.F = ['n2']
        return res

    def automatoLFA(self):
        pass

