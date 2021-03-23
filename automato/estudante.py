from .gera_grafo import Grafo
from .automato import Automato
from .gera_site import gerar_pagina_links, abrir_links

class Estudante:
    '''
    Classe que vai jogar o automato
    ''' 

    def __init__(self, nome, n_automato):
        self.nome = nome
        self.estado_atual = ''  # uma string contendo a label do estado atual
        self.estado_antigo = ''
        self.fita = ''  # palavra de entrada
        self.saida = []  # saida até o momento
        self.automato = None
        self.links = None
        self.estados_visitados = 0
        if n_automato == 1:
            self.automato = Automato().automatoTeste()
        elif n_automato == 2:
            self.automato = Automato().automatoExe()
        elif n_automato == 3:
            self.automato = Automato().automatoLFA()
        elif n_automato == 4:
            self.automato = Automato().automatoFinal()

        self.grafo = Grafo()  # instacia de grafo

    def getTransicoesAtuais(self):
        return self.automato.getTransicoes(self.estado_atual) # retorna {label_estado: [estado, saida]}

    def initializeWeb(self):
        self.estado_atual = self.automato.getEstadoInicial()
        self.estado_antigo = self.estado_atual
        self.fita = ''
        self.saida = []

    def getEstadoAtual(self):
        return self.estado_atual

    def getProgressoAtual(self):
        return round(self.estados_visitados * 100 / len(self.automato.Q), 2)

    def renderizarAutomato(self):
        self.grafo.renderDrawMachine(self)

    def fazerTransicao(self, simbolo):
        ''' Retorna os links da transição ou None, se retorna None é pq deu erro '''
        self.saida.append(self.automato.getTransicoes(self.estado_atual)[simbolo][1])

        self.estado_atual = self.automato.getTransicoes(self.estado_atual)[simbolo][0].getLabel()

        # self.grafo.renderDrawMachine(self)
        self.links = self.automato.links[self.automato.getTransicoes(self.estado_atual)[simbolo][1]]
        abrir_links(self.links)

        if self.estado_atual != self.estado_antigo:
            self.estados_visitados += 1

        self.fita += simbolo
        self.estado_antigo = self.estado_atual

        if len(self.automato.getTransicoes(self.estado_atual)) == 0:
            return None
        return self.links


    def abrirLinks(self):
        abrir_links(self.links)


    def getLinks(self):
        return self.links

    def jogador(self):
        self.estado_atual = self.automato.getEstadoInicial()
        self.estado_antigo = self.estado_atual
        self.saida = []

        while True:
            print(f'Estado atual: {self.estado_atual}')
            print(f'Porcentagem de conclusão do estudo: {round(self.estados_visitados * 100 / len(self.automato.Q), 2)}%')
            
            print('Transições possíveis:')

            for simbolo, estado_saida in self.automato.getTransicoes(self.estado_atual).items():
                print(f'Transicao com símbolo {simbolo} para {estado_saida[0].getLabel()} com saída {estado_saida[1]}')
                ultimo_simbolo = simbolo

            if self.automato.eEstadoFinal(self.estado_atual):
                print('ESTADO FINAL: se deseja encerrar use um símbolo que não pertença ao alfabeto')

            opcao = int(input("\nSelecione o que deseja: \n1 - Realizar uma transição\n2 - Adicionar um conteúdo personalizado\n"))

            if opcao == 1:
                simbolo = input('Próximo símbolo da palavra: ')

                if not simbolo in self.automato.getTransicoes(self.estado_atual):
                    if self.automato.eEstadoFinal(self.estado_atual):
                        print("Leitura concluida, não há mais transições, a saída foi:")
                        print("".join(self.saida))
                        self.grafo.drawMachine(self, True)
                        gerar_pagina_links(self.automato.links[self.automato.delta[-1]])
                        break
                    else:
                        print('Símbolo não reconhecido, tente novamente.\n')
                else:
                    self.saida.append(self.automato.getTransicoes(self.estado_atual)[simbolo][1])
                    print(f'\nSaída até agora: {"".join(self.saida)}\n')

                    self.estado_atual = self.automato.getTransicoes(self.estado_atual)[simbolo][0].getLabel()

                    self.grafo.drawMachine(self)
                    gerar_pagina_links(self.automato.links[self.automato.getTransicoes(self.estado_atual)[simbolo][1]])

                    if self.estado_atual != self.estado_antigo:
                        self.estados_visitados += 1

                    self.estado_antigo = self.estado_atual

                    if len(self.automato.getTransicoes(self.estado_atual)) == 0:
                        if self.automato.eEstadoFinal(self.estado_atual):
                            print("Leitura concluída, não há mais transições, a saída foi:")
                            print(f'\nSaída: {"".join(self.saida)}\n')
                        else:
                            print("Palavra não reconhecida")
                            # print(f'\nSaída: {self.saida}\n')
                        break
            elif opcao == 2:
                entrada = ultimo_simbolo + 'c'
                saida = 'c' + ultimo_simbolo.split('a')[1]
                self.automato.addTransicao(self.estado_atual, self.estado_atual, entrada, saida)

                self.automato.links[saida] = []
                qtd_links = 0
                while qtd_links < 1:
                    qtd_links = int(input("Entre com a quantidade de links: "))
                    if qtd_links < 1:
                        print("Quantidade de links precisa ser superior a 0")

                for i in range(qtd_links):
                    link = input(f'Entre com o link {i + 1}: ')
                    self.automato.links[saida].extend(link)
            else:
                print("Opção indisponível, tente novamente\n")
        


if __name__ == '__main__':

    est = Estudante('teste', 4)

    est.jogador()
