
class Estado:

	def __init__(self, label, final=False):
		self.label = label
		self.transicoes = {}
		self.eFinal = final

	def __eq__(self, other):
		return self.label==other.label

	def addTransicao(self, estado, simbolo, saida):
		self.transicoes[simbolo] = [estado, saida] 
		# transicoes[0] é o estado e [1] é a saida dessa transicao
	
	def getTransicoes(self):
		return self.transicoes.copy()

	def getLabel(self):
		return self.label


if __name__=='__main__':

	print(Estado('a', False) == Estado('a', False))
