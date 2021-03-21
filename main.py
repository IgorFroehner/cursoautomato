from estudante import Estudante

if __name__ == '__main__':

    est1 = Estudante('Igor', 4)
    est2 = Estudante('Matheus', 4)

    while True:
        opcao = int(input("Selecione o estudante que irá estudar: \n1 - Igor\n2 - Matheus\n3 - Criar novo estudante\n"))
        if opcao == 1:
            est1.jogador()
            break
        elif opcao == 2:
            est2.jogador()
            break
        elif opcao == 3:
            nome = input("\nEntre com o nome do estudante: ")
            est3 = Estudante(nome, 4)
            est3.jogador()
            break
        else:
            print("Opção indisponível, tente novamente.\n")
