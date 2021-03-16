from graphviz import Digraph


class Grafo:
    def __init__(self, name='fsm', format='png'):
        self.graph = Digraph(name, format=format)
        self.graph.attr(rankdir='LR', size='8,5')

    def drawMachine(self, data):
        print(data)
