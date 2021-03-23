
class Estado:

	def __init__(self, label, final=False):
		self.label = label
		self.transicoes = {}  # simbolo: [estado_destino, saida_transicao]
		self.eFinal = final  # true se o estado é final

	def __eq__(self, other):
		return self.label == other.label

	def addTransicao(self, estado, simbolo, saida):
		# transicoes[0] é o estado e [1] é a saida dessa transicao
		if simbolo in self.transicoes:
			self.transicoes[simbolo][1] += ' ' + saida
		else:
			self.transicoes[simbolo] = [estado, saida]
	
	def getTransicoes(self):
		return self.transicoes.copy()

	def getLabel(self):
		return self.label


if __name__ == '__main__':

	print(Estado('a', False) == Estado('a', False))
