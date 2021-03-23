from graphviz import Digraph


class Grafo:
    def __init__(self, name='fsm', format='png'):
        self.graph = None
        self.name = name
        self.format = format

    def renderDrawMachine(self, estudante, fim=False):
        # Cria um novo diagraph em branco
        self.graph = Digraph(self.name, format=self.format)
        self.graph.attr(rankdir='LR')

        # Estado inicial para o estudante
        self.graph.attr('node', shape='none')
        self.graph.node('')
        self.graph.attr('node', shape='circle')
        self.graph.node(estudante.automato.q0.label)
        self.graph.edge('', estudante.automato.q0.label)

        # Estados finais
        for estado_final in estudante.automato.F:
            self.graph.attr('node', shape='doublecircle')
            self.graph.node(estado_final.label)

        # Outros estados
        self.graph.attr('node', shape='circle')
        for estado in estudante.automato.Q:
            self.graph.node(estado)

        # Transicoes
        for estado in estudante.automato.Q:
            for simbolo, estado_saida in estudante.automato.getTransicoes(estado).items():
                if estado_saida[0].getLabel() == estudante.estado_atual and estado == estudante.estado_antigo and not fim:
                    self.graph.edge(estado, estado_saida[0].getLabel(), label=f'({simbolo}, {estado_saida[1]})', color='blue')
                else:
                    self.graph.edge(estado, estado_saida[0].getLabel(), label=f'({simbolo}, {estado_saida[1]})')

        self.graph.render(f'{estudante.nome}', format=self.format, directory='./images/')



    def drawMachine(self, estudante, fim=False):
        # Cria um novo diagraph em branco
        self.graph = Digraph(self.name, format=self.format)
        self.graph.attr(rankdir='LR')

        # Estado inicial para o estudante
        self.graph.attr('node', shape='none')
        self.graph.node('')
        self.graph.attr('node', shape='circle')
        self.graph.node(estudante.automato.q0.label)
        self.graph.edge('', estudante.automato.q0.label)

        # Estados finais
        for estado_final in estudante.automato.F:
            self.graph.attr('node', shape='doublecircle')
            self.graph.node(estado_final.label)

        # Outros estados
        self.graph.attr('node', shape='circle')
        for estado in estudante.automato.Q:
            self.graph.node(estado)

        # Transicoes
        for estado in estudante.automato.Q:
            for simbolo, estado_saida in estudante.automato.getTransicoes(estado).items():
                if estado_saida[0].getLabel() == estudante.estado_atual and estado == estudante.estado_antigo and not fim:
                    self.graph.edge(estado, estado_saida[0].getLabel(), label=f'({simbolo}, {estado_saida[1]})', color='blue')
                else:
                    self.graph.edge(estado, estado_saida[0].getLabel(), label=f'({simbolo}, {estado_saida[1]})')

        self.graph.view()
