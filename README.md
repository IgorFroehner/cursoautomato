# Gerenciador de Curso Baseado em Autômato Finito com Saída

Dado um modelo de curso, o estudante pode evoluir nele.

## Requisitos

* graphviz
	- No UBUNTU:
	```SHELL
	sudo apt-get install graphviz
	```

* Pacotes do python:
	- Usar o comando:
	```SHELL
	pip3 install -r requirements.txt
	``` 

## Estrutura do Autômato

Estruturas das "entidadas" envolvolvidas na implementação.

* Estrutura de um Autômato com saída
	* sigma: alfabeto
	* Q: conjunto de estados
	* q0: estado inicial
	* F: conjunto de estados finais
	* delta: conjunto de simbolos de saída
	* funcao_programa: que determina as transições dos estados, nesse caso ela vai ficar definida nos estados e suas transições.

* Estrutura de um Estado:
	* label: label do estado
	* transicoes: um map contendo as transicoes do estado, com a key sendo o símbolo, e listas como intem do map, essa lista é do tipo [proximoEstado, saidaDadaPelaTransicao]

* Estrutura de um Estudante:

	Estudante servirá como o jogador do autômato, com principal objetivo de ser a instância do autômato, guardando as informações de:

    * estado corrente: estado em que o estudante se encontra
	* fita:
	* saida:

selecionado o aluno ele possibilita a escolha entre as transições possíveis

solicitada a transição ele da a saida q são os links para as disciplinas
