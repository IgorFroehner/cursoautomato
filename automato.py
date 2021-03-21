from estado import Estado

class Automato:
    '''
    Automato, todo o gerenciamento deve ser feito usando a label dos 
    '''

    def __init__(self):
        self.sigma = []  # alfabeto
        self.Q = {}  # conjunto de estados {label: estado}
        self.q0 = None  # estado inicial
        self.F = []  # conjunto de estados finais
        self.delta = []  # alfabeto de símbolos de saída
        # a funcao programa fica definida nos estados e suas transições
        self.links = {}  # dicionário de saída: links

    def addEstado(self, label, final=False):
        self.Q[label] = Estado(label, final)
        if final and self.Q[label] not in self.F:
            self.F.append(self.Q[label])

    def setEstadoInicial(self, label_inicial):
        self.q0 = self.Q[label_inicial]

    def addTransicao(self, label_de, label_para, simbolo, saida):
        if not label_de in self.Q and not label_para in self.Q:
            print('Estado com label informada não existe no automato')
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
        res.addTransicao('qe', 'q1', 'a1', 'u0u2')
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

    def automatoFinal(self):
        '''
        Retorna o automato que será apresentado ao professor
        '''

        res = Automato()

        # Todas as aulas
        # Grupo da lista 1
        res.addEstado('aula01')
        res.addEstado('aula02')
        res.addEstado('aula03')
        res.addEstado('aula04')
        res.addEstado('aula05')
        res.addEstado('aula06')
        res.addEstado('aula07')

        # Grupo da lista 2
        res.addEstado('aula08')

        # Grupo sem lista
        res.addEstado('aula09')
        res.addEstado('aula10')
        res.addEstado('aula11')
        res.addEstado('aula12')
        res.addEstado('aula13')
        res.addEstado('aula14')
        res.addEstado('aula15')
        res.addEstado('aula16')
        res.addEstado('aula17')
        res.addEstado('aula18')

        # Estado final
        res.addEstado('concl', True)

        # Estado inicial
        res.setEstadoInicial('aula01')

        # ai - Slides da aula
        res.setSigma([f'a{i}' for i in range(1, 19)])

        # Transições (Relacionar x com o dicionário de links ou com o arquivo html a ser aberto)
        res.addTransicao('aula01', 'aula02', 'a1',
                         'x1')
        res.addTransicao('aula02', 'aula03', 'a2',
                         'x2')
        res.addTransicao('aula02', 'aula02', 'a1',
                         'x1')
        res.addTransicao('aula03', 'aula04', 'a3',
                         'x3')
        res.addTransicao('aula03', 'aula03', 'a2',
                         'x2')
        res.addTransicao('aula04', 'aula05', 'a4',
                         'x4')
        res.addTransicao('aula04', 'aula04', 'a3',
                         'x3')
        res.addTransicao('aula05', 'aula06', 'a5',
                         'x5')
        res.addTransicao('aula05', 'aula05', 'a4',
                         'x4')
        res.addTransicao('aula06', 'aula07', 'a6',
                         'x6')
        res.addTransicao('aula06', 'aula06', 'a5',
                         'x5')
        res.addTransicao('aula07', 'aula08', 'a7',
                         'x7')  # Além do link da aula, incluir o link da primeira e segunda lista
        res.addTransicao('aula07', 'aula07', 'a6',
                         'x6')
        res.addTransicao('aula08', 'aula09', 'a8',
                         'x8')  # Além do link da aula, incluir o link da terceira lista
        res.addTransicao('aula08', 'aula08', 'a7',
                         'x7')
        res.addTransicao('aula09', 'aula10', 'a9',
                         'x9')
        res.addTransicao('aula09', 'aula09', 'a8',
                         'x8')
        res.addTransicao('aula10', 'aula11', 'a10',
                         'x10')
        res.addTransicao('aula10', 'aula10', 'a9',
                         'x9')
        res.addTransicao('aula11', 'aula12', 'a11',
                         'x11')
        res.addTransicao('aula11', 'aula11', 'a10',
                         'x10')
        res.addTransicao('aula12', 'aula13', 'a12',
                         'x12')
        res.addTransicao('aula12', 'aula12', 'a11',
                         'x11')
        res.addTransicao('aula13', 'aula14', 'a13',
                         'x13')
        res.addTransicao('aula13', 'aula13', 'a12',
                         'x12')
        res.addTransicao('aula14', 'aula15', 'a14',
                         'x14')
        res.addTransicao('aula14', 'aula14', 'a13',
                         'x13')
        res.addTransicao('aula15', 'aula16', 'a15',
                         'x15')
        res.addTransicao('aula15', 'aula15', 'a14',
                         'x14')
        res.addTransicao('aula16', 'aula17', 'a16',
                         'x16')
        res.addTransicao('aula16', 'aula16', 'a15',
                         'x15')
        res.addTransicao('aula17', 'aula18', 'a17',
                         'x17')
        res.addTransicao('aula17', 'aula17', 'a16',
                         'x16')
        res.addTransicao('aula18', 'aula18', 'a17',
                         'x17')
        res.addTransicao('aula18', 'concl', 'a18',
                         'x18')
        res.addTransicao('concl', 'concl', 'a18',
                         'x18')

        res.addSaidas([f'x{i}' for i in range(1, 19)])
        res.links['x1'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=6']
        res.links['x2'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=9']
        res.links['x3'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=13']
        res.links['x4'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=15']
        res.links['x5'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=16', 'https://ricardofm.me/index.php?option=com_attachments&task=download&id=25']
        res.links['x6'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=17']
        res.links['x7'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=24', 'https://ricardofm.me/index.php?option=com_attachments&task=download&id=10', 'https://ricardofm.me/index.php?option=com_attachments&task=download&id=26', 'https://ricardofm.me/index.php?option=com_attachments&task=download&id=27']
        res.links['x8'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=45', 'https://ricardofm.me/index.php?option=com_attachments&task=download&id=46', 'https://ricardofm.me/index.php?option=com_attachments&task=download&id=47']
        res.links['x9'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=48']
        res.links['x10'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=49']
        res.links['x11'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=61']
        res.links['x12'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=62']
        res.links['x13'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=63']
        res.links['x14'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=67']
        res.links['x15'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=79']
        res.links['x16'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=80', 'https://ricardofm.me/index.php?option=com_attachments&task=download&id=82']
        res.links['x17'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=81', 'https://ricardofm.me/index.php?option=com_attachments&task=download&id=87']
        res.links['x18'] = ['https://ricardofm.me/index.php?option=com_attachments&task=download&id=85']

        return res


if __name__ == '__main__':
    
    a = Automato()
    a = a.automatoTeste()


