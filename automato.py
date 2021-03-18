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
        if final and self.Q[label] not in self.F:
            self.F.append(self.Q[label])

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
        return self.Q[label_estado] in self.F
    
    def setSigma(self, sigma):
        self.sigma.extend(sigma)

    def automatoTeste(self):
        '''
        Retorna um automato mais simples para fazer testes
        é o automato exemplo do slide 14 da aula de automatos com saida
        '''
        res = Automato()
        res.setSigma(['a0', 'a1'])

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
    
    def automatoExe(self):
        '''
        Retorna um automato exemplo que tem no livro do Menezes
        '''
        res = Automato()
        res.addEstado('q', True)
        res.addEstado('p', True)
        
        res.setEstadoInicial('q')
        res.addSaidas(['A', 'B'])
        res.setSigma(['a', 'b'])

        res.addTransicao('q', 'q', 'a', 'A')
        res.addTransicao('q', 'p', 'b', 'B')
        res.addTransicao('p', 'q', 'a', 'B')
        res.addTransicao('p', 'p', 'b', 'B')

        return res


    def automatoLFA(self):
        
        res = Automato()

        res.addEstado('aula01')
        res.addEstado('aula02')
        res.addEstado('aula03')
        res.addEstado('aula04')
        res.addEstado('concl', True)
        res.setSigma(['a', 'b', 'c', 'd'])
        res.setEstadoInicial('aula01')

        res.addTransicao('aula01', 'aula02', 'a', 'https://ricardofm.me/index.php?option=com_attachments&task=download&id=6')
        res.addTransicao('aula02', 'aula03', 'a', 'https://ricardofm.me/index.php?option=com_attachments&task=download&id=9')
        res.addTransicao('aula03', 'aula04', 'a', 'https://ricardofm.me/index.php?option=com_attachments&task=download&id=13')
        res.addTransicao('aula03', 'aula04', 'a', 'https://ricardofm.me/index.php?option=com_attachments&task=download&id=15')

        res.addSaidas(['https://ricardofm.me/index.php?option=com_attachments&task=download&id=6',
                       'https://ricardofm.me/index.php?option=com_attachments&task=download&id=9',
                       'https://ricardofm.me/index.php?option=com_attachments&task=download&id=13',
                       'https://ricardofm.me/index.php?option=com_attachments&task=download&id=15'
        ])

        return res


if __name__=='__main__':
    
    a = Automato()
    a = a.automatoTeste()

