from estado import Estado

class Automato:

    def __init__(self):
        self.sigma = [] # alfabeto
        self.Q = [] # conjunto de estados
        self.q0 = None # estado inicial
        self.F = [] # conjunto de estados finais
        self.delta = [] # alfabeto de símbolos de saída
        # a funcao programa fica definida nos estados e suas transições
        self.saida = ''

    def automatoTeste(self):
        '''
        Retorna um automato mais simples para fazer testes
        exemplo do slide 14 da aula de automatos com saida
        '''
        res = Automato()
        res.sigma = ['a0', 'a1']

        qe = Estado('qe', False)
        q1 = Estado('q1', True)
        q0 = Estado('q0', True)

        qe.addTransicao(q1, 'a1', 'u0u1')
        qe.addTransicao(q0, 'a0', 'u0u0')
        
        q0.addTransicao(q1, 'a1', 'u1')
        q0.addTransicao(q0, 'a0', 'u0')

        res.Q = [qe, q0, q1]
        res.q0 = qe
        res.delta = ['u0u1', 'u0u0', 'u1', 'u0']
        res.F = [q0, q1]
        res.saida = ''
        return res

    def automatoLFA(self):
        pass

    def jogador(self):
        self.estado_atual = self.q0 # acho q essa informação deve ficar no aluno
        while True:
            print(f'estado atual {self.estado_atual.toString()}')
            
            print('Transicoes possiveis:')

            for key, x in self.estado_atual.transicoes.items():
                print(f'simbolo: {key} transicao para {x[0].toString()} com saida {x[1]}')

            if self.estado_atual.is_final:
                print('ESTADO FINAL: se deseja encerrar use um simbolo que não pertence ao alfabeto')
            
            simbolo = input('Proximo simbolo da palavra: ')
            
            if not simbolo in self.estado_atual.transicoes:
                if self.estado_atual.is_final:
                    print("Leitura concluida, nao há mais transições, a saida foi:")
                    print(self.saida)
                    break
                else:
                    print('Palavra não reconhecida')
            else:
                self.saida += self.estado_atual.transicoes[simbolo][1]
                print(f'\nsaida ate agora: {self.saida}\n')

                self.estado_atual = self.estado_atual.transicoes[simbolo][0]

                if len(self.estado_atual.transicoes)==0 and self.estado_atual.is_final:
                    print("Leitura concluida, nao há mais transições, a saida foi:")
                    print(self.saida)
                    break
            


if __name__=='__main__':
    
    a = Automato()
    a = a.automatoTeste()

    a.jogador()
