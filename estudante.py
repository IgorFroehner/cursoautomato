from gera_grafo import Grafo
from automato import Automato
from gera_site import abrir_site


class Estudante:
    '''
    Classe que vai jogar o automato
    ''' 

    def __init__(self, nome, n_automato):
        self.nome = nome
        self.estado_corrente = ''  # uma string contendo a label do estado atual
        self.fita = ''  # palavra de entrada
        self.saida = []  # saida até o momento
        self.automato = None
        if n_automato == 1:
            self.automato = Automato().automatoTeste()
        elif n_automato == 2:
            self.automato = Automato().automatoExe()
        elif n_automato == 3:
            self.automato = Automato().automatoLFA()
        elif n_automato == 4:
            self.automato = Automato().automatoFinal()

        self.grafo = Grafo()  # instacia de grafo

    def jogador(self):
        self.estado_atual = self.automato.getEstadoInicial()
        self.estado_antigo = self.estado_atual
        self.saida = []

        while True:
            print(f'Estado atual: {self.estado_atual}')
            
            print('Transições possíveis:')

            for simbolo, estado_saida in self.automato.getTransicoes(self.estado_atual).items():
                print(f'Transicao com símbolo {simbolo} para {estado_saida[0].getLabel()} com saída {estado_saida[1]}')

            if self.automato.eEstadoFinal(self.estado_atual):
                print('ESTADO FINAL: se deseja encerrar use um símbolo que não pertença ao alfabeto')
            
            simbolo = input('Próximo símbolo da palavra: ')
            
            if not simbolo in self.automato.getTransicoes(self.estado_atual):
                if self.automato.eEstadoFinal(self.estado_atual):
                    print("Leitura concluida, não há mais transições, a saída foi:")
                    print(self.saida)
                    self.grafo.drawMachine(self, True)
                    abrir_site(self.automato.links[self.automato.delta[-1]])
                    break
                else:
                    print('Palavra não reconhecida')
            else:
                self.saida.append(self.automato.getTransicoes(self.estado_atual)[simbolo][1])
                print(f'\nSaída até agora: {self.saida}\n')

                self.estado_atual = self.automato.getTransicoes(self.estado_atual)[simbolo][0].getLabel()

                self.grafo.drawMachine(self)
                abrir_site(self.automato.links[self.automato.getTransicoes(self.estado_atual)[simbolo][1]])

                self.estado_antigo = self.estado_atual

                if len(self.automato.getTransicoes(self.estado_atual)) == 0:
                    if self.automato.eEstadoFinal(self.estado_atual):
                        print("Leitura concluída, não há mais transições, a saída foi:")
                        print(f'\nSaída: {self.saida}\n')
                    else:
                        print("Palavra não reconhecida")
                        # print(f'\nSaída: {self.saida}\n')
                    break


if __name__ == '__main__':

    est = Estudante('teste', 4)

    est.jogador()
