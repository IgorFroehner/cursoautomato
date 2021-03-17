from estado import Estado

class Automato:
    '''
    Automato, todo o gerenciamento deve ser feito usando a label dos 
    '''

    def __init__(self):
        self.sigma = [] # alfabeto
        self.Q = {} # conjunto de estados {label: estado}
        self.q0 = None # estado inicial
        self.F = [] # conjunto de estados finais
        self.delta = [] # alfabeto de símbolos de saída
        # a funcao programa fica definida nos estados e suas transições

    def addEstado(self, label, final=False):
        self.Q[label] = Estado(label, final)

    def setEstadoInicial(self, label_inicial):
        self.q0 = self.Q[label_inicial]

    def addTransicao(self, label_de, label_para, simbolo, saida):
        if not label_de in self.Q and not label_para in self.Q:
            print('Estado não label informada não existe no automato')
        else:
            self.Q[label_de].addTransicao(Estado(label_para), simbolo, saida)

    def getTransicoes(self, label):
        return self.Q[label].getTransicoes()

    def addSaida(self, saida):
        self.delta.append(saida)
    
    def addSaidas(self, saidas):
        self.delta.extend(saidas)    
    
    def addEstadoFinal(self, label_estado):
        self.F.append(self.Q[label_estado])

    def addEstadosFinais(self, labels_estados):
        for label_estado in labels_estados:
            self.F.append(self.Q[label_estado])
    
    def getEstadoInicial(self):
        return self.q0.getLabel()

    def eEstadoFinal(self, label_estado):
        return self.Q[label_estado].eFinal

    def automatoTeste(self):
        '''
        Retorna um automato mais simples para fazer testes
        é o automato exemplo do slide 14 da aula de automatos com saida
        '''
        res = Automato()
        res.sigma = ['a0', 'a1']

        res.addEstado('qe')
        res.addEstado('q1', True)
        res.addEstado('q0', True)

        res.addTransicao('qe', 'q1', 'a1', 'u0u1')
        res.addTransicao('qe', 'q0', 'a0', 'u0u0')
        
        res.addTransicao('q0', 'q1', 'a1', 'u1')
        res.addTransicao('q0', 'q0', 'a0', 'u0')

        res.setEstadoInicial('qe')
        res.addSaidas(['u0u1', 'u0u0', 'u1', 'u0'])
        res.addEstadosFinais(['q0', 'q1'])
        return res

    def automatoLFA(self):
        pass


if __name__=='__main__':
    
    a = Automato()
    a = a.automatoTeste()

