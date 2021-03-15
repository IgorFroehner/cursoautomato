
class Estado:

	def __init__(self, label, final):
		self.label = label
		self.transicoes = {}
		self.is_final = final

	def __eq__(self, other):
		return self.label==other.label

	def addTransicao(self, estado, simbolo, saida):
		self.transicoes[simbolo] = [estado, saida]

	def toString(self):
		return self.label

